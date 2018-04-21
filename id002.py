"""
Author: Luke Spademan
Calculates answer to project euler problem id2
https://projecteuler.net/problem=2
"""


def calculate():
    fib = [1, 1]
    total = 0
    while fib[-1] < 4000000:
        fib.append(fib[-1]+fib[-2])
        if fib[-1] % 2 == 0:
            total += fib[-1]
    return total

if __name__ == "__main__":
    answer = calculate()
    print(answer)
