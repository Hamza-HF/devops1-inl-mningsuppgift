def km_to_miles(km):
    if not isinstance(km, (int, float)):
        raise TypeError("Distance must be a number")
    if km < 0:
        raise ValueError("Distance cannot be negative")
    return km * 0.621371

def miles_to_km(miles):
    if not isinstance(miles, (int, float)):
        raise TypeError("Distance must be a number")
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    return miles * 1.60934

def meters_to_feet(m):
    if not isinstance(m, (int, float)):
        raise TypeError("Distance must be a number")
    if m < 0:
        raise ValueError("Distance cannot be negative")
    return m * 3.28084

def feet_to_meters(ft):
    if not isinstance(ft, (int, float)):
        raise TypeError("Distance must be a number")
    if ft < 0:
        raise ValueError("Distance cannot be negative")
    return ft / 3.28084