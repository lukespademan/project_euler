"""
Author: Luke Spademan
Calculates answer to project euler problem id2
https://projecteuler.net/problem=2
"""
from utils.fib_generator import fib_generator


def calculate() -> int:
    fib = fib_generator()
    total = 0
    i = 0

    while i < 4_000_000:
        i = next(fib)
        if i % 2 == 0:
            total += i
    return total


if __name__ == "__main__":
    answer = calculate()
    print(answer)
