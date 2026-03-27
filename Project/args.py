import argparse
from modules.organizer import organizeFiles
from modules.analyzer import analyzer

def startProject():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")

    organizeParser = subparser.add_parser("organize")
    organizeParser.add_argument("path", type=str)

    analyzeParser = subparser.add_parser("analyze")
    analyzeParser.add_argument("file", type=str)
    analyzeParser.add_argument("--column", type=str, required=True)
    analyzeParser.add_argument("--min", type=int, default=None)

    args = parser.parse_args()

    if args.command == "organize":
        organizeFiles(args.path)
    elif args.command == "analyze":
        analyzer(args.file, args.column, args.min)
    else: 
        print("Incorrect Command")
