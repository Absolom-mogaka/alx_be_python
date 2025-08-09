from programming_paradigm.simple_calculator import SimpleCalculator

def test_addition():
    calc = SimpleCalculator()
    assert calc.add(2, 3) == 5

def test_subtraction():
    calc = SimpleCalculator()
    assert calc.subtract(5, 3) == 2