import os
from modules.reports import reporter

@reporter
def organizeFiles(path):
    files = retrieveFiles(path)
    
    if not files:
        return
    
    for file in files:
        fullPath = os.path.join(path, file)
        
        if not os.path.isfile(fullPath):
            continue

        _, ext = os.path.splitext(file)

        if ext == "":
            continue

        ext = ext.lstrip(".")

        newPath = os.path.join(path, ext)
        os.makedirs(newPath, exist_ok=True)
        
        lastPath = os.path.join(newPath, file)
        print(f"New Path: {lastPath}")
        os.rename(fullPath, lastPath)


def retrieveFiles(path):
    try:
        files = os.listdir(path)

        if not files:
            print("Foler is empty")
        else: 
            return files
    except FileNotFoundError:
        print("Couldn't find the specified folder path")
    except PermissionError:
        print("You are not allowed to modify the folder path")