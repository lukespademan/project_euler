"""
Author: Luke Spademan
Calculates answer to project euler problem 25
https://projecteuler.net/problem=25
"""

def calculate():
    ans = 0
    a = 1
    b = 1
    i = 2
    while len(str(b)) < 1000:
        a, b= b, a+b
        i += 1
        print(i, b)
    ans = i
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
