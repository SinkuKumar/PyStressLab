import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--size", type=int, default=10**6, help="Size of each allocation")
args = parser.parse_args()

big_data = []

while True:
    big_data.append([0] * args.size)
    print(f"Allocated {len(big_data)} blocks")
    time.sleep(1)

print("Memory load done.")