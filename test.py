import pytest
from .hellstriangle import Triangle, TriangleException


def tests_empty_triangle():
    assert Triangle([]).max_sum == 0


def tests_triagle_with_solo_number():
    triangle = [[1337, ]]
    assert Triangle(triangle).max_sum == 1337


def tests_simple_triangle():
    triangle = [[0], [1, 2], [3, 4, 5]]
    assert Triangle(triangle).max_sum == 7


def tests_challenges_example():
    triangle = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]
    assert Triangle(triangle).max_sum == 26


def tests_triangle_with_not_obvious_path():
    triangle = [[1], [2, 3], [4, 5, 6], [93, 8, 9, 10]]
    assert Triangle(triangle).max_sum == 100


def tests_triangle_with_invalid_structure():
    triangle = [[1], [2, 3, 2], ]
    with pytest.raises(TriangleException):
        Triangle(triangle).max_sum
