import time
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, required=True, help="Target URL")
parser.add_argument("--delay", type=int, default=1, help="Seconds between requests")
parser.add_argument("--count", type=int, default=-1, help="Number of requests (-1 for infinite)")
args = parser.parse_args()

count = 0
while True:
    count += 1
    if args.count != -1 and count >= args.count:
        break
    response = requests.get(args.url)
    print(f"Fetched {len(response.content)} bytes from {args.url}")
    time.sleep(args.delay)

