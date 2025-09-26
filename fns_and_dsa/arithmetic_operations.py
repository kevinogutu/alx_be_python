def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs an arithmetic operation on num1 and num2.

    Parameters:
        num1 (float): The first operand.
        num2 (float): The second operand.
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: The result of the operation.
        str: A special error message if division by zero is attempted.
    """

    # Normalize operation input
    op = operation.lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 == 0:
            # Return a recognizable value or message for division by zero
            return "ERROR_DIVISION_BY_ZERO"
        else:
            return num1 / num2
    else:
        # If operation is invalid
        return "ERROR_UNKNOWN_OPERATION"
