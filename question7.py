# =============================================================================
# Question 7: Custom Exception Class
# =============================================================================

class NegativeNumberError(Exception):
    """
    Custom exception raised when a negative number is encountered 
    where only positive numbers are allowed.
    """
    
    def __init__(self, number: float, message: str = None):
        self.number = number
        if message is None:
            message = f"Negative number not allowed: {number}"
        super().__init__(message)


def check_positive(number: float) -> bool:
    """
    Checks if a number is positive and raises NegativeNumberError if negative.
    
    Args:
        number (float): The number to check
        
    Returns:
        bool: True if the number is positive
        
    Raises:
        NegativeNumberError: If the number is negative
    """
    if number < 0:
        raise NegativeNumberError(number, f"Expected positive number, got {number}")
    
    print(f"Number {number} is positive ✓")
    return True


def demonstrate_custom_exception():
    """
    Demonstrates the usage of custom exception in try-catch blocks.
    """
    test_numbers = [5, 10, -3, 0, -15, 7.5]
    
    print("Testing custom exception with various numbers:")
    print("-" * 50)
    
    for num in test_numbers:
        try:
            check_positive(num)
        except NegativeNumberError as e:
            print(f"Caught NegativeNumberError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
