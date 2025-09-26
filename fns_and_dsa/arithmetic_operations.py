# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs an arithmetic operation on num1 and num2.

    Parameters:
        num1 (float): First operand.
        num2 (float): Second operand.
        operation (str): One of 'add', 'subtract', 'multiply', or 'divide'.

    Returns:
        float: Result of the arithmetic operation if successful.
        str: A specific error message if operation is unknown or division by zero.
    """

    op = operation.lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 == 0:
            return "ERROR_DIVISION_BY_ZERO"
        else:
            return num1 / num2
    else:
        return "ERROR_UNKNOWN_OPERATION"

# You may include some simple tests below, or use a separate test suite.

if __name__ == '__main__':
    # Example usages
    print(perform_operation(5.0, 3.0, 'add'))        # 8.0
    print(perform_operation(5.0, 3.0, 'subtract'))   # 2.0
    print(perform_operation(5.0, 3.0, 'multiply'))   # 15.0
    print(perform_operation(5.0, 0.0, 'divide'))     # ERROR_DIVISION_BY_ZERO
    print(perform_operation(5.0, 3.0, 'divide'))     # 1.6666666666666667
    print(perform_operation(5.0, 3.0, 'modulus'))    # ERROR_UNKNOWN_OPERATION
