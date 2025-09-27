# arithmetic_operations.py

def perform_operation(num1, num2, operation):
  
    operation = operation.lower()

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "ERROR_DIVISION_BY_ZERO"
        else:
            return num1 / num2
    else:
        return "ERROR_UNKNOWN_OPERATION"

# You may include some simple tests below, or use a separate test suite.

# if __name__ == '__main__':
#     # Example usages
#     print(perform_operation(5.0, 3.0, 'add'))        # 8.0
#     print(perform_operation(5.0, 3.0, 'subtract'))   # 2.0
#     print(perform_operation(5.0, 3.0, 'multiply'))   # 15.0
#     print(perform_operation(5.0, 0.0, 'divide'))     # ERROR_DIVISION_BY_ZERO
#     print(perform_operation(5.0, 3.0, 'divide'))     # 1.6666666666666667
#     print(perform_operation(5.0, 3.0, 'modulus'))    # ERROR_UNKNOWN_OPERATION
