import pytest
from converters.weight import (
    kg_to_lbs,
    lbs_to_kg,
    grams_to_ounces,
    ounces_to_grams
)


def test_kg_to_lbs_basic():
    assert round(kg_to_lbs(1), 5) == 2.20462

def test_kg_to_lbs_zero():
    assert kg_to_lbs(0) == 0.0

def test_kg_negative_raises():
    with pytest.raises(ValueError):
        kg_to_lbs(-1)

def test_lbs_to_kg_basic():
    assert round(lbs_to_kg(2.20462), 4) == 1.0

def test_lbs_negative_raises():
    with pytest.raises(ValueError):
        lbs_to_kg(-5)

def test_grams_to_ounces_basic():
    assert round(grams_to_ounces(100), 4) == 3.5274

def test_grams_negative_raises():
    with pytest.raises(ValueError):
        grams_to_ounces(-10)

def test_ounces_to_grams_basic():
    assert round(ounces_to_grams(1), 4) == 28.3495

def test_ounces_negative_raises():
    with pytest.raises(ValueError):
        ounces_to_grams(-1)

def test_kg_to_lbs_float():
    assert round(kg_to_lbs(72.5), 3) == 159.835

def test_lbs_to_kg_large():
    assert round(lbs_to_kg(200), 2) == 90.72

def test_grams_to_ounces_float():
    assert round(grams_to_ounces(250.5), 4) == 8.8361

def test_kg_to_lbs_string_raises():
    with pytest.raises((TypeError, ValueError)):
        kg_to_lbs("heavy")

def test_ounces_to_grams_large():
    assert round(ounces_to_grams(100), 2) == 2834.95