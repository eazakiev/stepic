import pytest
from my_test import sum_divisors, sum_numbers


@pytest.mark.parametrize("number, expected_result", [(10, 18),
                                                     (50, 93),
                                                     (3, 4),
                                                     (1000, 2340),
                                                     (17, 18)
                                                     ])
def test_sum_divisors(number, expected_result):
    assert sum_divisors(number) == expected_result


@pytest.mark.parametrize("number, expected_result", [(1, 1),
                                                  (5, 3),
                                                  (3, 2),
                                                  (2, -1),
                                                  (10, -5),
                                                  (100, -50),
                                                  (9999, 5000)
                                                  ])
def test_sum_numbers(number, expected_result):
    assert sum_numbers(number) == expected_result



