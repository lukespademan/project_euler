"""
Author: Luke Spademan
Calculates answer to project euler problem 23
https://projecteuler.net/problem=23
"""
from utils.is_abundent import is_abundent

def calculate():
    ans = 0
    
    abundent_nums = []
    abundent_sums = []
    for i in range(28123):
        print(i)
        if i not in abundent_sums:
            ans += i
        if is_abundent(i):
            abundent_nums.append(i)

        for j in abundent_nums[:-1]:
            if i+j not in abundent_sums:
                abundent_sums.append(i+j)
            
    return ans


if __name__ == "__main__":
    answer = calculate()
    print(answer)
