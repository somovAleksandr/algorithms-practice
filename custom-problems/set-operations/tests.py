import pytest
from main import (
    union,
    intersection,
    symmetric_difference,
    unique_in_first,
    is_superset,
    is_strict_superset,
)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


def test_union():
    assert union(set1, set2) == {1, 2, 3, 4, 5, 6, 7, 8}


def test_intersection():
    assert intersection(set1, set2) == {4, 5}


def test_symmetric_difference():
    assert symmetric_difference(set1, set2) == {1, 2, 3, 6, 7, 8}


def test_unique_in_first():
    assert unique_in_first(set1, set2) == {1, 2, 3}


def test_is_superset():
    assert is_superset(set2, {4, 5, 7}) is True
    assert is_superset(set2, {8, 3, 4}) is False
    assert is_superset(set2, {4, 5, 6, 7, 8}) is True


def test_is_strict_superset():
    assert is_strict_superset(set2, {4, 5, 6, 7, 8}) is False  # равны
    assert is_strict_superset(set2, {4, 5, 7}) is True  # строго больше


if __name__ == "__main__":
    pytest.main()