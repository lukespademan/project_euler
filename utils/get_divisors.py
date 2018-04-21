def get_divisors(n):
    divisors = []

    for i in range(1, round(n**0.5)+1):  # all nums less than sqrt n
        if n % i == 0:
            divisors.append(i)
            if n / i not in divisors:
                divisors.append(n/i)

    return divisors
