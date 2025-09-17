# =============================================================================
# Question 3: Exception Handling for User Input
# =============================================================================

def get_number_with_exception_handling() -> float:
    """
    Handles user input with proper exception handling for invalid numbers.
    """
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)
            print(f"You entered: {number}")
            return number
        except ValueError as e:
            print(f"Error: Invalid number format. Please enter a valid number.")
            print(f"Details: {e}")
