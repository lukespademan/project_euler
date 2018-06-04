def is_prime(num: int) -> bool:
    if num == 1:
        return False

    for i in range(2, round(num**0.5)+1):
        if num % i == 0:
            return False

    return True
