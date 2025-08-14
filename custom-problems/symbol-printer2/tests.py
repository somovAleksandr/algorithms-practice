import pytest
from solution import generate_pattern


def test_generate_pattern_basic():
    assert generate_pattern(5, 'A', 'B') == 'ABABA'
    assert generate_pattern(4, 'X', 'O') == 'XOXO'
    assert generate_pattern(1, '+', '-') == '+'
    assert generate_pattern(2, '1', '2') == '12'


def test_generate_pattern_length_0():
    with pytest.raises(ValueError):
        generate_pattern(0, 'A', 'B')


def test_generate_pattern_negative_length():
    with pytest.raises(ValueError):
        generate_pattern(-5, 'A', 'B')


def test_generate_pattern_single_char():
    assert generate_pattern(3, 'Z', 'Y') == 'ZYZ'


def test_generate_pattern_long():
    expected = '+-+-+-+'
    assert generate_pattern(7, '+', '-') == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])