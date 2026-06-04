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