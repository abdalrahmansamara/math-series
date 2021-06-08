from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci('s') == 'not an integer'
    assert fibonacci([]) == 'not an integer'
    assert fibonacci(7) == 13

def test_lucas():
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(7) == 29
    assert lucas('s') == 'not an integer'
    assert lucas([]) == 'not an integer'

def test_sum_series():

# testing the default values
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(7) == 13
# testing error values
    assert sum_series('s') == 'not an integer'
    assert sum_series([]) == 'not an integer'
## testing for lucas inputs
    assert sum_series(0,2,1) == 2
    assert sum_series(1,2,1) == 1
    assert sum_series(2,2,1) == 3
    assert sum_series(7,2,1) == 29