"""
Author: Luke Spademan
Calculates answer to project euler problem id14
https://projecteuler.net/problem=14
"""
from module.next_collatz import next_collatz


def calculate():
    ans = 0
    ans_len = 0
    for i in range(1, 1000000):
        n = i
        x = 1
        while n != 1:
            x+= 1
            n = next_collatz(n)
        if x > ans_len:
            ans_len = x
            ans = i

    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
