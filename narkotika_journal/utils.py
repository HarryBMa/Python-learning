def get_int_input(prompt, min_value=None, max_value=None):
    """Get validated integer input from user with retry on invalid input.
    Args:
        prompt (str): The input prompt to display to the user.
        min_value (int, optional): Minimum acceptable value (inclusive).
        max_value (int, optional): Maximum acceptable value (inclusive).
    Returns:
        int: The validated integer input from the user within the specified range.
        
    Examples:
        age = get_int_input("Enter your age: ", 0, 120)
        choice = get_int_input("Choose an option (1-5): ", 1, 5)
        """
    while True:
        user_input = input(prompt)
        if user_input.lower() == "q":
            print("Avbryter inmatning.")
            return None
        try:
            value: int = int(user_input)
            if min_value is not None and value < min_value:
                print(f"Värdet måste vara minst {min_value}. Försök igen.")
                continue
            if max_value is not None and value > max_value:
                print(f"Värdet får inte överstiga {max_value}. Försök igen.")
                continue
        except ValueError:
            print("Ogiltigt värde. Ange ett heltal.")
        else:
            # print(f"Inmatat värde: {value}") # for debugging
            return value
   