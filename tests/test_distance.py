import pytest
from converters.distance import (
    km_to_miles,
    miles_to_km,
    meters_to_feet,
    feet_to_meters
)


def test_km_to_miles_basic():
    assert round(km_to_miles(1), 6) == 0.621371

def test_km_to_miles_zero():
    assert km_to_miles(0) == 0.0

def test_km_negative_raises():
    with pytest.raises(ValueError):
        km_to_miles(-1)

def test_miles_to_km_basic():
    assert round(miles_to_km(1), 5) == 1.60934

def test_miles_negative_raises():
    with pytest.raises(ValueError):
        miles_to_km(-5)

def test_meters_to_feet_basic():
    assert round(meters_to_feet(1), 5) == 3.28084

def test_meters_negative_raises():
    with pytest.raises(ValueError):
        meters_to_feet(-1)

def test_feet_to_meters_basic():
    assert round(feet_to_meters(3.28084), 4) == 1.0

def test_feet_negative_raises():
    with pytest.raises(ValueError):
        feet_to_meters(-10)


def test_km_to_miles_float():
    assert round(km_to_miles(1.5), 6) == 0.932057

def test_miles_to_km_large():
    assert round(miles_to_km(100), 2) == 160.93

def test_meters_to_feet_float():
    assert round(meters_to_feet(1.75), 4) == 5.7414

def test_km_to_miles_string_raises():
    with pytest.raises((TypeError, ValueError)):
        km_to_miles("ten")

def test_feet_to_meters_large():
    assert round(feet_to_meters(100), 4) == 30.4799