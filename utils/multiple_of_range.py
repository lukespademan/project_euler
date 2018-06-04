def multiple_of_range(num: int, start: int, stop: int, step: int = 1) -> bool:
    for i in range(start, stop, step):
        if num % i != 0:
            return False
    return True
