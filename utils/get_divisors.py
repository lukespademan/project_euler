def get_divisors(n):
    divisors = []

    for i in range(1, n):  # all nums less than sqrt n
        if n % i == 0:
            divisors.append(i)
    return divisors
