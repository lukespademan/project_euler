"""
Author: Luke Spademan
Calculates answer to project euler problem id15
https://projecteuler.net/problem=15
"""
from module.factorial import factorial


def calculate():
    grid_size = 20
    ans = factorial(grid_size*2)/(factorial(grid_size)**2)
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
