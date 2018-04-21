"""
Author: Luke Spademan
Calculates answer to project euler problem id1
https://projecteuler.net/problem=1
"""


def calculate():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == "__main__":
    answer = calculate()
    print(answer)

