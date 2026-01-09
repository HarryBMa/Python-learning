def get_int_input(prompt, min_value=None, max_value=None):
    """Get integer input from user with error handling"""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Värdet måste vara minst {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Värdet måste vara högst {max_value}.")
                continue
            return value
        except ValueError:
            print("Felaktig inmatning. Vänligen ange ett heltal.")
# Test 1: Basic try/except
print("Test 1: Basic try/except")
try:
    number =  int(input("Enter a number: "))
    print(f"Success! You entered: {number}")
except ValueError:
    print("Error: That's not a valid number.")
print("Program continues...\n")
# Test 2: multiple error types
print("Test 2: Multiple error types")
try:
    value = int(input("Enter a number to divide 100 by: "))
    result = 100 / value
    print(f"Result: {result}")
except ValueError:
    print("Error: Invalid number entered.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
print("Program continues...\n")
# Test 3:
while True:
    print("Test 3: Loop until valid input")
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print(f"Your age is: {age}")
        break
    except ValueError as ve:
        print(f"Error: {ve}. Please try again.")
print("Program continues...\n")# Test 4: File handling with try/except
