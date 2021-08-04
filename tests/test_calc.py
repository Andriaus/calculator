from calculator.calc import *

complex_number_error = "Calculator supports arithmetic only with integers and floats but not with complex numbers\n"
division_by_zero_error = "Division by zero is not allowed\n"
zeroth_root_error = "Taking the zeroth root is not allowed\n"
root_of_negative_number_error = "Taking root of a negative number results in a complex number\n"

def test_add_complex(capsys):
    calc = Calculator()
    calc.add(0j)
    out, error = capsys.readouterr()
    assert out == complex_number_error

def test_add():
    calc = Calculator()
    calc.add(8)
    assert calc.add(-12) == -4

def test_multiply():
    calc = Calculator()
    assert calc.multiply(5) == 0

def test_divide_by_zero(capsys):
    calc = Calculator()
    calc.divide(0)
    out, error = capsys.readouterr()
    assert out == division_by_zero_error

def test_divide():
    calc = Calculator()
    calc.add(8)
    assert calc.divide(-4) == -2

def test_take_root_of_negative_number(capsys):
    calc = Calculator()
    calc.add(-4)
    calc.take_root(2)
    out, error = capsys.readouterr()
    assert out == complex_number_error + root_of_negative_number_error

def test_take_root_0th_root(capsys):
    calc = Calculator()
    calc.take_root(0)
    out, error = capsys.readouterr()
    assert out == zeroth_root_error

def test_take_root():
    calc = Calculator()
    calc.add(4)
    assert calc.take_root(-2) == 0.5

def test_reset_memory():
    calc = Calculator()
    calc.add(5)
    calc.reset_memory()
    assert calc.display_memory() == 0
