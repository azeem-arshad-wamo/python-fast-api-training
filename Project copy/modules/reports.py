from datetime import datetime
import json
import os

def reporter(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        errors = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            errors = e

        end = datetime.now()
        report = {
            "function": func.__name__,
            "start_time": start.isoformat(),
            "errors": str(errors),
            "duration": (end - start).total_seconds()
        }
        if args:
            report["arguments"] = list(args)

        updateData(report)
        return result
    return wrapper

def updateData(report):
    try:
        os.path.exists("Data/Logs")
    except Exception as e:
        print(f"Error: {e}")
        print("Cannot find Logs folder")
        return

    timestamp = datetime.now().isoformat().replace(":", "-")
    fileName = f"report_{timestamp}.json"
    print(f"File Name: {fileName}")

    cwd = os.getcwd()
    path = os.path.join(cwd, "Data", "Logs", fileName)

    with open(path, "w") as f:
        json.dump(report, f, indent=4)
    
    print("File Saved in logs")