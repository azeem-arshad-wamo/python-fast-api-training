import json

data = {"name": "Azeem", "score": 40}

with open("file.json", "w") as f:
    json.dump(data, f, indent=4)

fileData = {}

with open("file.json", "r") as f:
    fileData = json.load(f)

print(fileData)

with open("file.json", "r") as f:
    data = json.load(f)

data["score"] = 100

with open("file.json", "w") as f:
    json.dump(data, f, indent=4)