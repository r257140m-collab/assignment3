# =============================================================================
# Question 1: Number Classification with Input Validation
# =============================================================================

def classify_number(number: int) -> str:
    """
    Classifies a number as positive, negative, or zero.
    
    Args:
        number (int): The number to classify
        
    Returns:
        str: "Positive", "Negative", or "Zero"
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


def get_valid_integer() -> int:
    """
    Uses a while loop to repeatedly prompt user for a valid integer.
    
    Returns:
        int: A valid integer input from the user
    """
    while True:
        try:
            user_input = input("Enter an integer: ")
            number = int(user_input)
            return number
        except ValueError:
            print("Invalid input! Please enter a valid integer.")