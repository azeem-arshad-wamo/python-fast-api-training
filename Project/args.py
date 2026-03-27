import argparse
from modules.organizer import organizeFiles

def startProject():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")

    organizeParser = subparser.add_parser("organize")
    organizeParser.add_argument("path", type=str)

    args = parser.parse_args()

    if(args.command == "organize"):
        organizeFiles(args.path)
