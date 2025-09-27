#!/usr/bin/env python3

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    # No need for `global` here since we are only *reading* the global variable
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    # Similarly, just reading the global variable
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    # Prompt the user for a temperature
    temp_input = input("Enter the temperature to convert: ").strip()
    # Validate it's a numeric value (can be float)
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    # Prompt for unit (C or F)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        # Interpret the input value as Fahrenheit; convert to Celsius
        c = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {c}°C")
    elif unit == 'C':
        # Input is Celsius; convert to Fahrenheit
        f = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {f}°F")
    else:
        # Invalid unit
        raise ValueError("Invalid unit. Please specify C or F.")

if __name__ == "__main__":
    main()
