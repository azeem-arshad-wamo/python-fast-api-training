import os
import csv
import json
from modules.reports import reporter

class Analyzer:
    @reporter
    def analyzer(self, file, column, min):
        type = self._checkFileType(file)

        if not type:
            return

        if type:
            self._analyzeFile(file, column, min, type)
        else:
            return

    def _checkFileType(self, file):
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

    def _csvGenerator(self, file):
        with open(file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                yield row

    def _jsonGenerator(self, file):
        with open(file, "r") as f:
            data = json.load(f)

            for row in data:
                yield row  

    def _analyzeFile(self, file, column, minValue, type):
        if type == "csv":
            rows = self._csvGenerator(file)
        elif type == "json":
            rows = self._jsonGenerator(file)
        else: 
            print("Incorrect File Type Again")
            return

        totalColumns = 0
        totalColumnSum = 0
        filteredColumnSum = 0

        for row in rows:
            try:
                size = int(row[column])
            except KeyError:
                print(f"Column '{column}' not found")
                return
            except ValueError:
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
