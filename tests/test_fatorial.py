import pytest

from app.fatorial import calcular_fatorial


def test_fatorial_zero():
    assert calcular_fatorial(0) == 1


def test_fatorial_um():
    assert calcular_fatorial(1) == 1


def test_fatorial_numero():
    assert calcular_fatorial(5) == 120


def test_fatorial_numero_maior():
    assert calcular_fatorial(10) == 3628800


def test_fatorial_negativo():
    with pytest.raises(ValueError):
        calcular_fatorial(-5)