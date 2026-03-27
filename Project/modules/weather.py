import requests
import json

def checkWeather(cities, mode):
    cities = cities.split(",")

    results = []

    for city in cities:
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

    print(json.dumps(results, indent=4))

def useThreading():
    pass

def useMultiprocessing():
    pass