# =============================================================================
# Question 2: Variable Arguments Function with Docstring
# =============================================================================

from typing import Union


def calculate_average(*args: Union[int, float]) -> float:
    """
    Calculate the average of a variable number of numeric arguments.
    
    This function accepts any number of numeric arguments and returns their
    arithmetic mean. It handles both integers and floating-point numbers.
    
    Args:
        *args: Variable number of numeric arguments (int or float)
        
    Returns:
        float: The arithmetic mean of all provided numbers
        
    Raises:
        ValueError: If no arguments are provided
        TypeError: If any argument is not a number
        
    Examples:
        >>> calculate_average(1, 2, 3, 4, 5)
        3.0
        >>> calculate_average(2.5, 3.5, 4.0)
        3.333333333333333
        >>> calculate_average(10)
        10.0
    """
    if not args:
        raise ValueError("At least one argument is required")
    
    # Validate all arguments are numbers
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"All arguments must be numbers, got {type(arg).__name__}")
    
    return sum(args) / len(args)