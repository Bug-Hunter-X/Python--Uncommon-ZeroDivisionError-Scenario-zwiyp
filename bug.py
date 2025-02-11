def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a  # ZeroDivisionError: division by zero
    elif b == 0:
        return a / b  # ZeroDivisionError: division by zero
    else:
        return a / b