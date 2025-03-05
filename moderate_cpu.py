import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--num", type=int, default=100000, help="Number for factorial calculation")
args = parser.parse_args()


result = math.factorial(args.num)
print(result)

print("Factorial computed.")
