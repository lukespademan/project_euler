"""
Author: Luke Spademan
Calculates answer to project euler problem 24
https://projecteuler.net/problem=24
"""
from utils.factorial import factorial
import math

def calculate():
    ans = []

    didgets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    target_perm = 1000000
    combs_per_didget = [factorial(i) for i in range(len(didgets), 0, -1)]
    print(combs_per_didget)
    for i, combs in enumerate(combs_per_didget):
        if i == 0:
            continue
        index = math.ceil(target_perm / combs)
        print(index)
        didget = didgets.pop(index)
        ans.append(didget)
        target_perm -= combs * (index)

    ans = "".join(ans)
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
