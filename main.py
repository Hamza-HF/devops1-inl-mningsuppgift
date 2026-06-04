# Unit Converter — temperature, distance and weight

from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin
from converters.distance import km_to_miles, miles_to_km, meters_to_feet
from converters.weight import kg_to_lbs, lbs_to_kg, grams_to_ounces

if __name__ == "__main__":
    print("=== Unit Converter ===")

    print("\n-- Temperature --")
    print(f"100°C  -> {celsius_to_fahrenheit(100)}°F")
    print(f"212°F  -> {fahrenheit_to_celsius(212)}°C")
    print(f"0°C    -> {celsius_to_kelvin(0)}K")

    print("\n-- Distance --")
    print(f"10 km      -> {km_to_miles(10):.4f} miles")
    print(f"10 miles   -> {miles_to_km(10):.4f} km")
    print(f"180 cm     -> {meters_to_feet(1.80):.4f} ft")

    print("\n-- Weight --")
    print(f"80 kg      -> {kg_to_lbs(80):.4f} lbs")
    print(f"100 g      -> {grams_to_ounces(100):.4f} oz")