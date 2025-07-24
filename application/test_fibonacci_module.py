import pytest
from application.Fibonacci.fibonacci_module import n_Binet


def test_n_Binet_integer_input():
    assert n_Binet(13)[0] == 7
    assert n_Binet(13)[1] == 7
    assert n_Binet(21)[0] == 8
    assert n_Binet(21)[1] == 8
    assert n_Binet(34)[0] == 9
    assert n_Binet(34)[1] == 9
    assert n_Binet(55)[0] == 10
    assert n_Binet(55)[1] == 10
    

def test_n_Binet_float_input():
    with pytest.raises(ValueError):
        n_Binet(2.5)
    with pytest.raises(ValueError):
        n_Binet(3.14)
    with pytest.raises(ValueError):
        n_Binet(1.61)
    

def test_n_Binet_negative_input():
    with pytest.raises(ValueError):
        n_Binet(-1)
    with pytest.raises(ValueError):
        n_Binet(-4)
    with pytest.raises(ValueError):
        n_Binet(-9)
    

def test_n_Binet_non_numeric_input():
    with pytest.raises(ValueError):
        n_Binet("ten")
    with pytest.raises(ValueError):
        n_Binet([1, 2, 3])
    with pytest.raises(ValueError):
        n_Binet({"a": 1, "b": 2})
    with pytest.raises(ValueError):
        n_Binet(None)
