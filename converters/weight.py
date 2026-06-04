def kg_to_lbs(kg):
    if kg < 0:
        raise ValueError("Weight cannot be negative")
    return kg * 2.20462

def lbs_to_kg(lbs):
    if lbs < 0:
        raise ValueError("Weight cannot be negative")
    return lbs / 2.20462

def grams_to_ounces(g):
    if g < 0:
        raise ValueError("Weight cannot be negative")
    return g * 0.035274

def ounces_to_grams(oz):
    if oz < 0:
        raise ValueError("Weight cannot be negative")
    return oz * 28.3495