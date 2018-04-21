from utils.get_divisors import get_divisors

def is_abundent(n):
    divisors = get_divisors(n)
    if sum(divisors) > n:
        return True
    return False
