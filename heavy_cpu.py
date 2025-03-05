import threading
import argparse

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_task(start, count):
    primes = [n for n in range(start, start + count) if is_prime(n)]
    print(f"Found {len(primes)} primes.")

parser = argparse.ArgumentParser()
parser.add_argument("--threads", type=int, default=4, help="Number of threads")
parser.add_argument("--count", type=int, default=5000, help="Range for prime numbers")
args = parser.parse_args()

threads = [threading.Thread(target=prime_task, args=(10**6, args.count)) for _ in range(args.threads)]

for t in threads:
    t.start()
for t in threads:
    t.join()
