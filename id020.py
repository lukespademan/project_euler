"""
Author: Luke Spademan
Calculates answer to project euler problem id20
https://projecteuler.net/problem=20
"""
from utils.factorial import factorial
from utils.sum_of_digits import sum_of_digits


def calculate():
    num = factorial(100)
    ans = sum_of_digits(num)
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
