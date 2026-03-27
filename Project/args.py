import argparse
from modules.organizer import organizeFiles
from modules.analyzer import analyzer
from modules.weather import checkWeather

def startProject():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")

    organizeParser = subparser.add_parser("organize")
    organizeParser.add_argument("path", type=str)

    analyzeParser = subparser.add_parser("analyze")
    analyzeParser.add_argument("file", type=str)
    analyzeParser.add_argument("--column", type=str, required=True)
    analyzeParser.add_argument("--min", type=int, default=None)

    weatherParser = subparser.add_parser("weather")
    weatherParser.add_argument("--cities", type=str, default="lahore")
    weatherParser.add_argument("--mode", default="threading")

    args = parser.parse_args()

    if args.command == "organize":
        organizeFiles(args.path)
    elif args.command == "analyze":
        analyzer(args.file, args.column, args.min)
    elif args.command == "weather":
        checkWeather(args.cities, args.mode)
    else: 
        print("Incorrect Command")
