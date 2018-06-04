"""
Author: Luke Spademan
Calculates answer to project euler problem id5
https://projecteuler.net/problem=5
"""
from utils.multiple_of_range import multiple_of_range


def calculate() -> int:
    ans = 0
    i = 0
    while not ans:
        i += 1
        if multiple_of_range(i, 1, 20):
            ans = i
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
