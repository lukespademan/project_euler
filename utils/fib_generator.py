def fib_generator(a: int = 0, b: int = 1) -> int:
    while True:
        yield b
        a, b = b, a + b
