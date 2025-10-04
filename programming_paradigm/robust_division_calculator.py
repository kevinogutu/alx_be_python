# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers while handling:
    - Division by zero
    - Non-numeric input
    """

    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
