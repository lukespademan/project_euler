import os, sys

if len(sys.argv) != 2:
    print("Error: usage %s <id>" % sys.argv[0])

filename = "id" + "0"*(3-len(sys.argv[1]))+sys.argv[1]+".py"

text ='''"""
Author: Luke Spademan
Calculates answer to project euler problem {0}
https://projecteuler.net/problem={0}
"""

def calculate():
    ans = 0
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
'''.format(sys.argv[1])

with open(filename, 'w') as f:
    f.write(text)
    f.close()
