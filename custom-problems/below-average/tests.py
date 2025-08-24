from main import below_average


def test_below_average():
    # Normal case
    assert below_average(1, 2, 3, 4, 5, 6, 7, 8, 9) == [1, 2, 3, 4], "Test 1 failed"

    # All equal
    assert below_average(5, 5, 5) == [], "Test 2 failed"

    # With non-int (string)
    assert below_average(1, 2, 'hello', 4) == [1], "Test 3 failed"  # sum=7, len=4 → avg=1.75

    # Only one int
    assert below_average(10, 'a', 'b') == [], "Test 4 failed"  # sum=10, len=3 → avg≈3.33 → 10 not < 3.33

    # Empty
    assert below_average() == [], "Test 5 failed"

    # Negative numbers
    assert below_average(-3, -1, 0, 2) == [-3, -1], "Test 6 failed"  # sum=-4, len=4 → avg=-1.0

    # Floats are ignored in sum
    assert below_average(1, 2.5, 3) == [1], "Test 7 failed"  # sum=4, len=3 → avg≈1.33

    print("🎉 All tests passed!")


if __name__ == "__main__":
    test_below_average()