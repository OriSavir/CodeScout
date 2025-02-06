import argparse
from typing import Optional, Sequence

def main(argv: Optional[Sequence[str]] = None):
    parser = argparse.ArgumentParser(description="CodeScout CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Scan a directory or file")
    group = scan_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--directory', help="Specify a directory to scan")
    group.add_argument('-f', '--filename', help="Specify a single file to scan")
    #scan_parser.add_argument('--model', '-m', default='openai', help='Which API key and model to use') <--- placeholder for future feature

    key_parser = subparsers.add_parser("set-api-key", help="Set the API key for API access")
    key_parser.add_argument("api_key", help="Your API key to interact with LLM")

    args = parser.parse_args(argv)

    if args.command == "scan":
        scan_code(directory=args.directory, filename=args.filename) ## Placeholder function
    elif args.command == "set-api-key":
        save_api_key(args.api_key) ## Placeholder function

if __name__ == "__main__":
    main()
