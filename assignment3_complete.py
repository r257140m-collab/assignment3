"""
Python Assignment 3 - Complete Solutions
Advanced Python Programming Concepts
"""

import socket
import sqlite3
import random
import re
import requests
from typing import List, Union, Any
import json


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


# =============================================================================
# Question 2: Variable Arguments Function with Docstring
# =============================================================================

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


# =============================================================================
# Question 4: File Operations with Context Managers
# =============================================================================

def file_operations_demo():
    """
    Demonstrates file operations using context managers (with statement).
    """
    # List of names to write to file
    names = [
        "Alice Johnson",
        "Bob Smith", 
        "Charlie Brown",
        "Diana Prince",
        "Edward Norton",
        "Fiona Green"
    ]
    
    filename = "names.txt"
    
    # Write names to file using with statement
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for name in names:
                file.write(f"{name}\n")
        print(f"Successfully wrote {len(names)} names to {filename}")
        
        # Read names from file and print to console
        with open(filename, 'r', encoding='utf-8') as file:
            print("\nReading names from file:")
            for line_number, line in enumerate(file, 1):
                name = line.strip()  # Remove newline character
                print(f"{line_number}. {name}")
                
    except IOError as e:
        print(f"File operation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# =============================================================================
# Question 5: Lambda Functions and Temperature Conversion
# =============================================================================

def temperature_conversion_demo():
    """
    Demonstrates lambda functions with map for temperature conversion.
    """
    # Sample list of Celsius temperatures
    celsius_temps = [0, 10, 20, 25, 30, 37, 40, 100, -10, -40]
    
    # Lambda function to convert Celsius to Fahrenheit
    celsius_to_fahrenheit = lambda c: c * 9/5 + 32
    
    # Use map to convert all temperatures
    fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
    
    print("Temperature Conversion (Celsius to Fahrenheit):")
    print("-" * 50)
    for c, f in zip(celsius_temps, fahrenheit_temps):
        print(f"{c:6.1f}°C = {f:6.1f}°F")
    
    return celsius_temps, fahrenheit_temps


# =============================================================================
# Question 6: Division Function with Multiple Exception Types
# =============================================================================

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


# =============================================================================
# Question 8: Random Number Generation and Statistics
# =============================================================================

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


# =============================================================================
# Question 9: Regular Expressions Demo
# =============================================================================

def regex_demonstrations():
    """
    Comprehensive demonstration of regular expressions.
    """
    
    # Sample text for demonstrations
    sample_text = """
    Contact us at: john.doe@example.com, support@company.org, or info@test-site.net
    Important dates: 2024-03-15, 2023-12-01, 2024-01-30
    Replace all instances of 'Python' with 'Java' in this Python text about Python programming.
    Mixed text with numbers123, symbols@#$, and spaces   between words.
    """
    
    print("Regular Expressions Demonstrations:")
    print("=" * 60)
    
    # I. Extract all email addresses
    print("\n1. Extracting Email Addresses:")
    print("-" * 30)
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, sample_text)
    
    for i, email in enumerate(emails, 1):
        print(f"   {i}. {email}")
    
    # II. Validate dates in YYYY-MM-DD format
    print("\n2. Validating Dates (YYYY-MM-DD):")
    print("-" * 35)
    date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    dates = re.findall(date_pattern, sample_text)
    
    # More strict validation
    strict_date_pattern = r'\b(19|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b'
    
    for date in dates:
        if re.match(strict_date_pattern, date):
            print(f"   ✓ Valid date: {date}")
        else:
            print(f"   ✗ Invalid date format: {date}")
    
    # III. Replace all occurrences of a word
    print("\n3. Word Replacement:")
    print("-" * 20)
    original = "Replace all instances of 'Python' with 'Java' in this Python text about Python programming."
    replaced = re.sub(r'\bPython\b', 'Java', original, flags=re.IGNORECASE)
    
    print(f"   Original: {original}")
    print(f"   Replaced: {replaced}")
    
    # IV. Split by non-alphanumeric characters
    print("\n4. Splitting by Non-Alphanumeric Characters:")
    print("-" * 45)
    text_to_split = "Mixed text with numbers123, symbols@#$, and spaces   between words."
    words = re.split(r'[^A-Za-z0-9]+', text_to_split)
    words = [word for word in words if word]  # Remove empty strings
    
    print(f"   Original: {text_to_split}")
    print(f"   Split result: {words}")
    
    return emails, dates, replaced, words


# =============================================================================
# Question 10: Client-Server Socket Programming
# =============================================================================

class SimpleServer:
    """Simple TCP server implementation."""
    
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.socket = None
    
    def start_server(self):
        """Start the server and listen for connections."""
        try:
            # Create socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Bind to address
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            
            print(f"Server listening on {self.host}:{self.port}")
            
            # Accept connection
            client_socket, client_address = self.socket.accept()
            print(f"Connection from {client_address}")
            
            # Send message
            message = "Hello from server!"
            client_socket.send(message.encode('utf-8'))
            print(f"Sent: {message}")
            
            client_socket.close()
            
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            if self.socket:
                self.socket.close()


class SimpleClient:
    """Simple TCP client implementation."""
    
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
    
    def connect_to_server(self):
        """Connect to server and receive message."""
        try:
            # Create socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to server
            client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
            
            # Receive message
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {message}")
            
            client_socket.close()
            return message
            
        except socket.error as e:
            print(f"Connection error: {e}")
            return None
        except Exception as e:
            print(f"Client error: {e}")
            return None


def socket_demo():
    """
    Demonstrate client-server communication.
    Note: In a real scenario, you'd run server and client in separate processes.
    """
    print("Socket Programming Demo:")
    print("-" * 25)
    print("Note: This demo shows the code structure.")
    print("In practice, run server and client in separate terminals/processes.")
    
    # Show how to create and use server
    server = SimpleServer()
    print(f"Server created for {server.host}:{server.port}")
    
    # Show how to create and use client
    client = SimpleClient()
    print(f"Client created to connect to {client.host}:{client.port}")


# =============================================================================
# Question 11: API and Database Explanations with Examples
# =============================================================================

def api_explanation_and_demo():
    """
    Explains APIs and demonstrates GET requests.
    """
    
    print("=" * 60)
    print("API EXPLANATION")
    print("=" * 60)
    
    explanation = """
    What is an API?
    ===============
    
    API stands for Application Programming Interface. It's a set of protocols, 
    routines, and tools that allows different software applications to communicate 
    with each other. Think of an API as a waiter in a restaurant:
    
    - You (client) make a request from the menu
    - The waiter (API) takes your order to the kitchen
    - The kitchen (server) prepares your food
    - The waiter brings your food back to you
    
    APIs enable:
    - Data sharing between applications
    - Integration of different services
    - Building modular, scalable applications
    - Separating frontend and backend logic
    
    Common API Types:
    - REST APIs (most common)
    - GraphQL APIs
    - SOAP APIs
    - WebSocket APIs
    """
    
    print(explanation)
    
    # Demonstrate GET request
    print("\nAPI GET Request Demo:")
    print("-" * 25)
    
    try:
        # Example with a public API (JSONPlaceholder)
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1', 
                               timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print("✓ GET Request Successful!")
            print(f"Status Code: {response.status_code}")
            print(f"Response Data:")
            print(json.dumps(data, indent=2))
        else:
            print(f"Request failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        print("Showing example of how the code would work:")
        
        # Show example structure
        example_code = '''
        import requests
        
        # Making a GET request
        response = requests.get('https://api.example.com/data')
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            print(data)
        else:
            print(f"Error: {response.status_code}")
        '''
        print(example_code)


def sqlite_explanation_and_demo():
    """
    Explains SQLite database connections and demonstrates usage.
    """
    
    print("\n" + "=" * 60)
    print("SQLITE DATABASE CONNECTION EXPLANATION")
    print("=" * 60)
    
    explanation = """
    SQLite Database Connection in Python:
    ====================================
    
    SQLite is a lightweight, file-based database that's perfect for development
    and small to medium applications. Here are the steps to connect and use it:
    
    Step 1: Import sqlite3 module (built into Python)
    Step 2: Create/Connect to database file
    Step 3: Create a cursor object for executing SQL commands
    Step 4: Execute SQL statements (CREATE, INSERT, SELECT, etc.)
    Step 5: Commit transactions (for write operations)
    Step 6: Close the connection
    
    Key Concepts:
    - Connection: Represents the database connection
    - Cursor: Used to execute SQL commands
    - Commit: Saves changes to the database
    - Context Manager: Automatically handles connection closing
    """
    
    print(explanation)
    
    # Demonstrate SQLite operations
    print("\nSQLite Demo:")
    print("-" * 15)
    
    try:
        # Step 1 & 2: Connect to database (creates file if doesn't exist)
        with sqlite3.connect('demo.db') as conn:
            print("✓ Connected to SQLite database")
            
            # Step 3: Create cursor
            cursor = conn.cursor()
            
            # Step 4: Create table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    age INTEGER
                )
            ''')
            print("✓ Table created/verified")
            
            # Insert sample data
            users_data = [
                ('Alice Johnson', 'alice@example.com', 28),
                ('Bob Smith', 'bob@example.com', 35),
                ('Charlie Brown', 'charlie@example.com', 22)
            ]
            
            cursor.executemany(
                'INSERT OR REPLACE INTO users (name, email, age) VALUES (?, ?, ?)',
                users_data
            )
            print(f"✓ Inserted {len(users_data)} users")
            
            # Query data
            cursor.execute('SELECT * FROM users ORDER BY age')
            results = cursor.fetchall()
            
            print("\nUsers in database:")
            print(f"{'ID':<5} {'Name':<15} {'Email':<25} {'Age':<5}")
            print("-" * 55)
            
            for row in results:
                print(f"{row[0]:<5} {row[1]:<15} {row[2]:<25} {row[3]:<5}")
            
            # Step 5: Commit is automatic with context manager
            print("✓ Changes committed automatically")
        
        # Step 6: Connection closed automatically with context manager
        print("✓ Database connection closed")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# =============================================================================
# MAIN DEMONSTRATION FUNCTION
# =============================================================================

def main():
    """
    Main function to demonstrate all solutions.
    """
    
    print("PYTHON ASSIGNMENT 3 - COMPREHENSIVE SOLUTIONS")
    print("=" * 60)
    
    # Question 1
    print("\n1. NUMBER CLASSIFICATION WITH INPUT VALIDATION")
    print("-" * 50)
    # Simulate user input
    test_numbers = [5, -3, 0, 10]
    for num in test_numbers:
        result = classify_number(num)
        print(f"classify_number({num}) = {result}")
    
    # Question 2
    print("\n2. CALCULATE AVERAGE WITH *ARGS")
    print("-" * 35)
    try:
        avg1 = calculate_average(1, 2, 3, 4, 5)
        avg2 = calculate_average(2.5, 3.7, 1.8)
        avg3 = calculate_average(100)
        
        print(f"Average of (1,2,3,4,5): {avg1}")
        print(f"Average of (2.5,3.7,1.8): {avg2:.2f}")
        print(f"Average of (100): {avg3}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Question 3 - Just show the function exists
    print("\n3. EXCEPTION HANDLING FOR USER INPUT")
    print("-" * 40)
    print("Function get_number_with_exception_handling() is available")
    print("(Skipping interactive input in demo)")
    
    # Question 4
    print("\n4. FILE OPERATIONS WITH CONTEXT MANAGERS")
    print("-" * 45)
    file_operations_demo()
    
    # Question 5
    print("\n5. LAMBDA FUNCTIONS AND TEMPERATURE CONVERSION")
    print("-" * 50)
    temperature_conversion_demo()
    
    # Question 6
    print("\n6. DIVISION WITH EXCEPTION HANDLING")
    print("-" * 38)
    test_cases = [
        (10, 2),
        (15, 0),
        ("abc", 5),
        (20, "xyz"),
        (8, 4)
    ]
    
    for num, den in test_cases:
        print(f"\nTesting divide_numbers({num}, {den}):")
        divide_numbers(num, den)
    
    # Question 7
    print("\n7. CUSTOM EXCEPTION CLASS")
    print("-" * 28)
    demonstrate_custom_exception()
    
    # Question 8
    print("\n8. RANDOM NUMBERS AND STATISTICS")
    print("-" * 35)
    random_numbers_demo()
    
    # Question 9
    print("\n9. REGULAR EXPRESSIONS DEMONSTRATIONS")
    print("-" * 40)
    regex_demonstrations()
    
    # Question 10
    print("\n10. CLIENT-SERVER SOCKET PROGRAMMING")
    print("-" * 40)
    socket_demo()
    
    # Question 11
    print("\n11. API AND DATABASE EXPLANATIONS")
    print("-" * 38)
    api_explanation_and_demo()
    sqlite_explanation_and_demo()
    
    print("\n" + "=" * 60)
    print("ALL SOLUTIONS COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()