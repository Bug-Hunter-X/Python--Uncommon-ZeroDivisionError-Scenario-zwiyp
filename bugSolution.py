def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return "Error: Both inputs are zero"  # Handle both zero inputs together
    elif a == 0:
        return "Error: Input 'a' is zero"  # Better error messages
    elif b == 0:
        return "Error: Input 'b' is zero"  # Better error messages
    else:
        return a / b