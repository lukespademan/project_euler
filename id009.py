"""
Author: Luke Spademan
Calculates answer to project euler problem idx
https://projecteuler.net/problem=x
"""


def calculate():
    ans = 0
    c = 0
    while ans == 0:
        c += 1
        for b in range(c):
            for a in range(b):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    ans = a*b*c
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
