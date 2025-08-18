import pytest
from main import (
    merge_sets,
    calc_qty_elements,
    min_element_in_set,
    max_element_in_set
)


# === Тесты merge_sets ===

def test_merge_sets_basic():
    sets = [{1, 2}, {3}, {4, 5}]
    result = merge_sets(sets)
    assert result == {1, 2, 3, 4, 5}

def test_merge_sets_with_overlap():
    sets = [{1, 2}, {2, 3}, {3, 4}]
    result = merge_sets(sets)
    assert result == {1, 2, 3, 4}

def test_merge_sets_empty_input():
    sets = []
    result = merge_sets(sets)
    assert result == set()

def test_merge_sets_with_empty_sets():
    sets = [{1, 2}, set(), {3}]
    result = merge_sets(sets)
    assert result == {1, 2, 3}


# === Тесты calc_qty_elements ===

def test_calc_qty_elements():
    assert calc_qty_elements({1, 2, 3}) == 3
    assert calc_qty_elements(set()) == 0


# === Тесты min_element_in_set ===

def test_min_element_in_set():
    assert min_element_in_set({5, 1, 3}) == 1
    assert min_element_in_set({-10, 0, 10}) == -10

def test_min_element_in_set_empty():
    with pytest.raises(ValueError, match="Множество пусто - невозможно найти минимум."):
        min_element_in_set(set())


# === Тесты max_element_in_set ===

def test_max_element_in_set():
    assert max_element_in_set({5, 1, 3}) == 5
    assert max_element_in_set({-10, 0, 10}) == 10

def test_max_element_in_set_empty():
    with pytest.raises(ValueError, match="Множество пусто - невозможно найти максимум."):
        max_element_in_set(set())