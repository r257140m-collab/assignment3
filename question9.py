# =============================================================================
# Question 9: Regular Expressions Demo
# =============================================================================

import re


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