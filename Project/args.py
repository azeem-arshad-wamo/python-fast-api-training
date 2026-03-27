import argparse

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command")

organizeParser = subparser.add_parser("organize")
organizeParser.add_argument("path", type=str)

args = parser.parse_args()

if(args.command == "organize"):
    pass