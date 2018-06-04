def next_collatz(num: int):
    if num % 2 == 0:
        return num/2
    else:
        return num*3 + 1
