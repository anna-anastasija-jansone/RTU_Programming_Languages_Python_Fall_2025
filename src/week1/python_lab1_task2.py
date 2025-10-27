"""
Task 2 – Greeting Function with String Manipulation
--------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""

def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    clean_name = name.strip().capitalize() #implement cleaning and formatting
    return f"Hello, {clean_name}! Be not afraid this is Python."

if __name__ == "__main__":
    user_name = input("Enter your name: ") #read name from input and print greeting
    print(greet_user(user_name))
