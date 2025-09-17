# =============================================================================
# Question 5: Lambda Functions and Temperature Conversion
# =============================================================================

def temperature_conversion_demo():
    """
    Demonstrates lambda functions with map for temperature conversion.
    """
    # Sample list of Celsius temperatures
    celsius_temps = [0, 10, 20, 25, 30, 37, 40, 100, -10, -40]
    
    # Lambda function to convert Celsius to Fahrenheit
    celsius_to_fahrenheit = lambda c: c * 9/5 + 32
    
    # Use map to convert all temperatures
    fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
    
    print("Temperature Conversion (Celsius to Fahrenheit):")
    print("-" * 50)
    for c, f in zip(celsius_temps, fahrenheit_temps):
        print(f"{c:6.1f}°C = {f:6.1f}°F")
    
    return celsius_temps, fahrenheit_temps
