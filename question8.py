# =============================================================================
# Question 8: Random Number Generation and Statistics
# =============================================================================

from random import random


def random_numbers_demo():
    """
    Generates random numbers and calculates statistics.
    """
    # Generate 10 random integers between 1 and 100
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    
    # Calculate average
    average = sum(random_numbers) / len(random_numbers)
    
    print("Random Numbers Generation Demo:")
    print("-" * 40)
    print(f"Generated numbers: {random_numbers}")
    print(f"Sum: {sum(random_numbers)}")
    print(f"Average: {average:.2f}")
    print(f"Min: {min(random_numbers)}")
    print(f"Max: {max(random_numbers)}")
    
    return random_numbers, average