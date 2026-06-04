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