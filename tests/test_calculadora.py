import pytest
from app.calculadora import dividir

def test_ok():
    assert dividir(10, 2) == 5

def test_error():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_edge():
    assert dividir(0, 5) == 0