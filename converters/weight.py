def kg_to_lbs(kg):
    if not isinstance(kg, (int, float)):
        raise TypeError("Weight must be a number")
    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg * 2.20462

def lbs_to_kg(lbs):
    if not isinstance(lbs, (int, float)):
        raise TypeError("Weight must be a number")
    if lbs < 0:
        raise ValueError("Weight cannot be negative")
    return lbs / 2.20462

def grams_to_ounces(g):
    if not isinstance(g, (int, float)):
        raise TypeError("Weight must be a number")
    if g < 0:
        raise ValueError("Weight cannot be negative")
    return g * 0.035274

def ounces_to_grams(oz):
    if not isinstance(oz, (int, float)):
        raise TypeError("Weight must be a number")
    if oz < 0:
        raise ValueError("Weight cannot be negative")
    return oz * 28.3495