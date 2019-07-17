def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for _ in range(3, n // 2, 2):
        if n % _ == 0:
            return False
    return True


def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1
