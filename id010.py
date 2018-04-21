"""
Author: Luke Spademan
Calculates answer to project euler problem id10
https://projecteuler.net/problem=10
"""
from module.primes_under import primes_under


def calculate():
    ans = sum(primes_under(2000000))
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
