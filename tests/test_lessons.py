import pytest
from lesson import solution


@pytest.mark.parametrize("num_1, num_2, expected_result", [(77, 62, 77, 75, 73, 71, 69, 67, 65, 63)])
def test_lesson(num_1, num_2, expected_result):
    assert solution(num_1, num_2) == expected_result


