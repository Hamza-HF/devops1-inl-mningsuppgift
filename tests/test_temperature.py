import pytest
from converters.temperature import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)


def test_boiling_point_c_to_f():
    assert celsius_to_fahrenheit(100) == 212.0

def test_freezing_point_c_to_f():
    assert celsius_to_fahrenheit(0) == 32.0

def test_negative_celsius_to_f():
    assert celsius_to_fahrenheit(-40) == -40.0

def test_boiling_point_f_to_c():
    assert fahrenheit_to_celsius(212) == 100.0

def test_freezing_point_f_to_c():
    assert fahrenheit_to_celsius(32) == 0.0

def test_celsius_to_kelvin_zero():
    assert celsius_to_kelvin(0) == 273.15

def test_celsius_to_kelvin_boiling():
    assert celsius_to_kelvin(100) == 373.15

def test_celsius_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_kelvin(-300)

def test_kelvin_to_celsius_basic():
    assert kelvin_to_celsius(273.15) == 0.0

def test_kelvin_negative_raises():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)

def test_celsius_to_fahrenheit_float():
    assert round(celsius_to_fahrenheit(36.6), 2) == 97.88

def test_fahrenheit_to_celsius_float():
    assert round(fahrenheit_to_celsius(98.6), 1) == 37.0

def test_celsius_to_kelvin_large_number():
    assert celsius_to_kelvin(1000) == 1273.15

def test_celsius_to_fahrenheit_string_raises():
    with pytest.raises((TypeError, ValueError)):
        celsius_to_fahrenheit("hot")

def test_kelvin_to_celsius_zero():
    assert round(kelvin_to_celsius(0), 2) == -273.15