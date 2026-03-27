import os
import argparse

os.system("clear")

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command")

# Analyze Command Practice
analyzeParser = subparser.add_parser("analyze")
analyzeParser.add_argument("file", type=str)
analyzeParser.add_argument("--column", required=True, type=str)
analyzeParser.add_argument("--size", default=100, type=int)

# Organize Command
organizeParser = subparser.add_parser("organize")
organizeParser.add_argument("path", type=str)

args = parser.parse_args()

if(args.command == "analyze"):
    print(f"File: {args.file}")
    print(f"Column: {args.column}")
    print(f"Size: {args.size}")
if(args.command == "organize"):
    print(f"Path: {args.path}")

