"""Operación división entera."""


def floor_divide(a, b):
    """División entera, redondeando hacia abajo."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a // b