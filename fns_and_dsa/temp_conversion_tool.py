#!/usr/bin/env python3

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature to convert: ").strip()
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == 'F':
        c = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {c}°C")
    elif unit == 'C':
        f = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {f}°F")
    else:
        raise ValueError("Invalid unit. Please specify C or F.")

if __name__ == "__main__":
    main()
