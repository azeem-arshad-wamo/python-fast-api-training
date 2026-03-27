import requests
import json
import threading
import multiprocessing

def checkWeather(cities, mode):
    cities = cities.split(",")

    if mode == "threading":
        useThreading(cities)
    elif mode == "multiprocessing":
        useMultiprocessing(cities)
    else:
        print("Incorrect Mode")
        return

def fetchWeather(city, results):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

    response = requests.get(url)
    data = response.json()

    longitude = data["results"][0]["longitude"]
    latitude = data["results"][0]["latitude"]

    newUrl = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature"

    response = requests.get(newUrl)
    finalData = response.json()

    print(json.dumps(finalData["current"]["temperature"]))

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

def useThreading(cities):
    threads = []
    results = []

    for city in cities:
        t = threading.Thread(target=fetchWeather, args=(city, results))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

    print(json.dumps(results, indent=4))

def useMultiprocessing(cities):
    print("TEST")