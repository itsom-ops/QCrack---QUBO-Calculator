import pytest
from src.shor_algorithm import factor_integer

@pytest.mark.parametrize("n, expected_factors", [
    (15, [3, 5]),
    (21, [3, 7]),
])
def test_shor_factorization(n, expected_factors):
    result = factor_integer(n)
    for factor in expected_factors:
        assert factor in result
