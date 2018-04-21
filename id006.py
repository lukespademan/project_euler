"""
Author: Luke Spademan
Calculates answer to project euler problem id6
https://projecteuler.net/problem=6
"""


def calculate():
    sum1 = 0
    sum2 = 0
    for i in range(1, 101):
        sum1 += i
        sum2 += i**2
    sum1 **= 2
    ans = sum1 - sum2
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
