# ex22

import pytest
import school

@pytest.fixture
def bonus():
    # bonus is currently 5
    return 5


@pytest.mark.average
def test_calculate_average():
    assert school.calculate_average(45, 65, 90, 80) == 70


@pytest.mark.bonus
def test_add_bonus(bonus):
    assert school.add_bonus(70, 85, 80, 95) == [70 + bonus, 85 + bonus, 80 + bonus, 95 + bonus]


@pytest.mark.parametrize("grade, expected", [(100, "Excellent"), (99, "Very Good"), (80, "Very Good"),
                                             (79, "Good"), (70, "Good"), (69, "Pass"), (60, "Pass"),
                                             (59, "Fail")])
def test_get_result(grade, expected):
    assert school.get_result(grade) == expected

