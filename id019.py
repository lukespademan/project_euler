"""
Author: Luke Spademan
Calculates answer to project euler problem id19
https://projecteuler.net/problem=19
"""


def calculate():
    ans = 0
    months = {
        "jan": 31,
        "feb": 28,
        "mar": 31,
        "apr": 30,
        "may": 31,
        "jun": 30,
        "jul": 31,
        "aug": 31,
        "sep": 30,
        "oct": 31,
        "nov": 30,
        "dec": 31,
    }
    i = 1
    for month in months:
        i += months[month]
    for year in range(1901, 2001):
        months["feb"] = 28
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            months["feb"] = 29
        for month in months:
            if i % 7 == 0:
                ans += 1
            i += months[month]
    return ans

if __name__ == "__main__":
    answer = calculate()
    print(answer)
