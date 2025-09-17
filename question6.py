# =============================================================================
# Question 6: Division Function with Multiple Exception Types
# =============================================================================

from typing import Any, Union


def divide_numbers(numerator: Any, denominator: Any) -> Union[float, None]:
    """
    Divides two numbers with comprehensive exception handling.
    
    Args:
        numerator: The dividend
        denominator: The divisor
        
    Returns:
        float: Result of division if successful, None otherwise
    """
    try:
        # Attempt to convert to numbers if they're not already
        num = float(numerator)
        den = float(denominator)
        
        result = num / den
        print(f"Division successful: {num} ÷ {den} = {result}")
        return result
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
        
    except (TypeError, ValueError) as e:
        print(f"Error: Invalid input types. Both arguments must be convertible to numbers.")
        print(f"Details: {e}")
        return None
        
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None