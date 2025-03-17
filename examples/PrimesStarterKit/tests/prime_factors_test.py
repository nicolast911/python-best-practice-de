from primes_sk.prime_factors import compute_prime_factors
import pytest

@pytest.mark.parametrize("n, primes", [(1, []), (2, [2]), (3, [3]), (4, [2, 2]),
                                       (5, [5]), (6, [2, 3]), (7, [7])])
def test_compute_prime_factors(n, primes):
    assert compute_prime_factors(n) == primes 