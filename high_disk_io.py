import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str, default="test_file.txt", help="Output file")
parser.add_argument("--lines", type=int, default=1000000, help="Number of lines to write")
args = parser.parse_args()

while True:
    with open(args.filename, "a") as f:
        f.write("This is a test line.\n" * args.lines)
    print(f"Wrote {args.lines} lines to {args.filename}.")
    break

print("Disk I/O done.")