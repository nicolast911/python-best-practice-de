def compute_prime_factors(n):
    result = []
    for factor in range(2, n+1):
        while n % factor == 0:
            result.append(factor)
            n //= factor

    return result 