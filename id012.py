"""
Author: Luke Spademan
Calculates answer to project euler problem id12
https://projecteuler.net/problem=12
"""


def calculate():
    ans = 0
    triangle_nums = []
    while ans == 0:
        next_num = 0
        for i in range(1, len(triangle_nums)+2):
            next_num += i
        triangle_nums.append(next_num)
        factors = 0
        for i in range(1, round(triangle_nums[-1]**0.5)+1):
            if triangle_nums[-1] % i == 0:
                factors += 1
        if factors*2 > 500:
            ans = triangle_nums[-1]
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
