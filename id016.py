"""
Author: Luke Spademan
Calculates answer to project euler problem id16
https://projecteuler.net/problem=16
"""


def calculate():
    num = 2**1000
    digests = [int(i) for i in str(num)]
    ans = sum(digests)
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
