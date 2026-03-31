import requests
import json
import os
import threading
import multiprocessing
from modules.reports import reporter

class Weather:
    @reporter
    def checkWeather(self, cities, mode):
        cities = cities.split(",")

        if mode == "threading":
            self._useThreading(cities)
        elif mode == "multiprocessing":
            self._useMultiprocessing(cities)
        else:
            print("Incorrect Mode")
            return

    def _fetchWeather(self, city, results):
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

        response = requests.get(url)
        data = response.json()

        longitude = data["results"][0]["longitude"]
        latitude = data["results"][0]["latitude"]

        newUrl = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature"

        response = requests.get(newUrl)
        finalData = response.json()

        item = {
            "city": city,
            "time": finalData["current"]["time"],
            "temperature": finalData["current"]["temperature"],
            "coordinates": {
                "longitude": finalData["longitude"],
                "latitude": finalData["latitude"]
            },
        }

        results.append(item)

    def _displayData(self, data):
        os.system("clear")
        for city in data:
            print("===========================")
            print(f"City: {city['city']}")
            print(f"Time: {city['time']}")
            print(f"Temperature: {city['temperature']} C")

    def _useThreading(self, cities):
        threads = []
        results = []

        for city in cities:
            t = threading.Thread(target=self._fetchWeather, args=(city, results))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()

        self._displayData(results)

    def _useMultiprocessing(self, cities):
        manager = multiprocessing.Manager()
        results = manager.list()

        processes = []

        for city in cities:
            p = multiprocessing.Process(target=self._fetchWeather, args=(city, results))
            processes.append(p)
            p.start()
        
        for p in processes:
            p.join()

        self._displayData(results)
