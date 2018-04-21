"""
Author: Luke Spademan
Calculates answer to project euler problem id3
https://projecteuler.net/problem=3
"""
from utils.is_prime import is_prime


def calculate():
    num = 600851475143
    ans = 0
    for i in range(1, round(num**0.5)):
        if num % i == 0 and is_prime(i):
            ans = i
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
