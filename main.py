import argparse
import json

from reports import REPORTS


def main():
    parser = argparse.ArgumentParser(
        description="Parse arguments to generate reports based on logs data"
    )
    parser.add_argument("files", nargs="+", help="Paths to JSON files containing logs")
    parser.add_argument(
        "--report",
        required=True,
        help="Generate reports based on workers data",
        choices=REPORTS,
    )
    parser.add_argument(
        "--date",
        help="Filter logs by specific date (format: YYYY-DD-MM, e.g., 2025-22-06)",
    )
    args: argparse.Namespace = parser.parse_args()

    for filename in args.files:
        if args.report == "average":
            with open(filename, "r", encoding="utf-8") as f:
                logs = [json.loads(line) for line in f if line.strip()]
            print(f"Log file: {filename}")
            print(REPORTS[args.report](logs, args.date))


if __name__ == "__main__":
    main()
