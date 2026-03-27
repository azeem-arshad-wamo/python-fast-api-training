import os
import csv
import json

def analyzer(file, column, min):
    type = checkFileType(file)

    if not type:
        return

    if type == "csv":
        analyzeCsv(file, column, min)
    if type == "json":
        analyzeJson(file, column, min)

def checkFileType(file):
    if not os.path.exists(file):
        print("File doesn't exist")
        return
    
    fileName = os.path.basename(file)
    __, ext = os.path.splitext(fileName)

    if ext not in [".csv", ".json"]:
        print("Unsupported File Type!")
        return

    if ext == ".csv":
        return "csv"
    elif ext == ".json":
        return "json"
    else:
        print("Something went wrong")
        return

def csvGenerator(file):
    with open(file, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            yield row

def jsonGenerator(file):
    with open(file, "r") as f:
        data = json.load(f)

        for row in data:
            yield row    


def analyzeCsv(file, column, minValue):
    rows = csvGenerator(file)

    totalColumns = 0
    totalColumnSum = 0
    filteredColumnSum = 0

    for row in rows:
        try:
            size = int(row[column])
        except: 
            continue

        totalColumnSum += size
        
        if minValue is not None and size < minValue:
            continue

        filteredColumnSum += size
        totalColumns += 1
    
    if totalColumns > 0:
        average = filteredColumnSum / totalColumns
    else: 
        average = 0
    
    print(f"Total Columns: {totalColumns}")
    print(f"Total Value: {totalColumnSum}")
    print(f"Column Total: {filteredColumnSum}")
    print(f"Average: {average}")

def analyzeJson(file, column, minValue):
    rows = jsonGenerator(file)

    totalColumns = 0
    totalColumnSum = 0
    filteredColumnSum = 0

    for row in rows:
        try:
            size = int(row[column])
        except: 
            continue

        totalColumnSum += size
        
        if minValue is not None and size < minValue:
            continue

        filteredColumnSum += size
        totalColumns += 1
    
    if totalColumns > 0:
        average = filteredColumnSum / totalColumns
    else: 
        average = 0
    
    print(f"Total Columns: {totalColumns}")
    print(f"Total Value: {totalColumnSum}")
    print(f"Column Total: {filteredColumnSum}")
    print(f"Average: {average}")
