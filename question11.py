# =============================================================================
# Question 11: API and Database
# =============================================================================

import json
import sqlite3

import requests


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