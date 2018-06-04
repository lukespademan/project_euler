"""
Author: Luke Spademan
Calculates answer to project euler problem id22
https://projecteuler.net/problem=22
"""
from utils.word_value import word_value

def calculate():
    ans = 0
    with open("names.txt") as f:
       names = f.read()
       names = names.replace('"','').replace(',', ' ').split()
       names.sort()
       for i, name in enumerate(names):
           value = (i+1) * word_value(name)
           ans += value

    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
