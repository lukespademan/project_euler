"""
Author: Luke Spademan
Calculates answer to project euler problem id21
https://projecteuler.net/problem=21
"""


def d(n):
    num = 0
    for i in range(1, n):
        if n % i == 0:
            num += i
    return num


def calculate():
    nums = []
    for i in range(1, 10000):
        a = d(i)
        if a != i:
            b = d(a)
            if b == i:
                if a not in nums:
                    nums.append(a)
                if b not in nums:
                    nums.append(b)
    ans = sum(nums)

    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
