# =============================================================================
# Question 4: File Operations with Context Managers
# =============================================================================

def file_operations_demo():
    """
    Demonstrates file operations using context managers (with statement).
    """
    # List of names to write to file
    names = [
        "Tinashe Moyo",
        "Tanatswa Chikukwa", 
        "Praise Mupfumira",
        "Tadiwa Marufu",
        "Panashe Chigumira",
        "James Chikukwa",
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
