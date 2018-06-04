from .is_prime import is_prime


def nth_prime(n: int) -> int:
    prime_count = 0
    tester = 1
    while prime_count != n:
        if is_prime(tester):
            prime_count += 1
        tester += 1
    return tester-1

