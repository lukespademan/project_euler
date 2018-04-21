"""
Author: Luke Spademan
Calculates answer to project euler problem id7
https://projecteuler.net/problem=7
"""
from module.nth_prime import nth_prime


def calculate():
    ans = nth_prime(10001)
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
