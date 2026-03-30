from modules.organizer import Organizer
from modules.analyzer import Analyzer
from modules.weather import Weather

class Orchestrator:
    def __init__(self):
        self.organizer = Organizer()
        self.analyzer = Analyzer()
        self.weather = Weather()

    def run(self, args):
        match args.command:
            case "organize":
                self.organizer.organizeFiles(args.path)
            case "analyze":
                self.analyzer.analyzer(args.file, args.column, args.min)
            case "weather":
                self.weather.checkWeather(args.cities, args.mode)
            case _:
                print("Invalid Command")