"""
Author: Luke Spademan
Calculates answer to project euler problem id4
https://projecteuler.net/problem=4
"""
from utils.reverse import reverse


def calculate():
    ans = 0
    for i in range(100, 999):
        for j in range(100, 999):
            prod = i*j
            if prod > ans and prod == reverse(prod):
                ans = prod
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
