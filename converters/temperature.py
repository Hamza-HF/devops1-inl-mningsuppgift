def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    if c < -273.15:
        raise ValueError("Temperature below absolute zero")
    return c + 273.15

def kelvin_to_celsius(k):
    if k < 0:
        raise ValueError("Kelvin cannot be negative")
    return k - 273.15