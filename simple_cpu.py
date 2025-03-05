import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--iterations", type=int, default=-1, help="Number of iterations (-1 for infinite)")
args = parser.parse_args()

i = 0
while args.iterations == -1 or i < args.iterations:
    i += 1
    print(f"Iteration {i}")
print("Done!")
