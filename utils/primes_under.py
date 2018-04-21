from .is_prime import is_prime


def primes_under(limit: int):
    primes = [2]
    tester = 3
    while tester < limit:
        if is_prime(tester):
            primes.append(tester)
        tester += 1
    return primes

