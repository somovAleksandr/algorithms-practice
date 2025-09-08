from calculator import calc_area_circle, calc_area_rectangle, calc_area_trapezoid

def test_calc_area_circle():
    assert round(calc_area_circle(1), 2) == 3.14
    assert round(calc_area_circle(2), 2) == 12.57

def test_calc_area_rectangle():
    assert calc_area_rectangle(3, 4) == 12
    assert calc_area_rectangle(2.5, 4) == 10.0

def test_calc_area_trapezoid():
    assert calc_area_trapezoid(3, 5, 2) == 8.0
    assert calc_area_trapezoid(10, 6, 4) == 32.0