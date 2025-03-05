import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--seconds", type=int, default=5, help="Sleep time in seconds")
args = parser.parse_args()

while True:
    print(f"Sleeping for {args.seconds} seconds...")
    time.sleep(args.seconds)
    print(f"Awake after {args.seconds} seconds!")
    break
