"""
Author: Luke Spademan
Calculates answer to project euler problem id17
https://projecteuler.net/problem=17
"""


def calculate():
    total_len = 0
    ans = 0
    units = ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = "hundred"
    thousand = "thousand"
    for i in range(1, 1001):
        if i < 10:
            word = str(units[i])
        elif i < 20:
            word = teens[i-10]
        elif i < 100:
            word = tens[int(str(i)[0])]+units[int(str(i)[1])]
        elif i < 1000:
            if str(i)[1] == "0" and str(i)[2] == "0":
                word = units[int(str(i)[0])] + hundred
            elif str(i)[1] == "1":
                word = units[int(str(i)[0])] + hundred + "ans" + teens[int(str(i)[2])]
            else:
                word = units[int(str(i)[0])] + hundred + "and" + tens[int(str(i)[1])] + units[int(str(i)[2])]
        else:
            word = "onethousand"
        print(word)
        total_len += len(word)
    ans = total_len

    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
