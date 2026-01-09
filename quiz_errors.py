"""
Quiz: Error Handling in Python
Test your knowledge of try/except blocks and error handling!
"""

def quiz():
    score = 0
    total_questions = 10
    
    print("=" * 50)
    print("QUIZ: Error Handling in Python")
    print("=" * 50)
    print()
    
    # Question 1
    print("Question 1: Which keyword is used to handle exceptions in Python?")
    print("a) catch")
    print("b) except")
    print("c) error")
    print("d) handle")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'b':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'b) except'\n")
    
    # Question 2
    print("Question 2: What error occurs when you try to convert 'hello' to an integer?")
    print("a) TypeError")
    print("b) ValueError")
    print("c) SyntaxError")
    print("d) AttributeError")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'b':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'b) ValueError'\n")
    
    # Question 3
    print("Question 3: What error occurs when dividing by zero?")
    print("a) ValueError")
    print("b) TypeError")
    print("c) ZeroDivisionError")
    print("d) MathError")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'c':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'c) ZeroDivisionError'\n")
    
    # Question 4
    print("Question 4: Which keyword is used to manually raise an exception?")
    print("a) throw")
    print("b) error")
    print("c) raise")
    print("d) trigger")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'c':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'c) raise'\n")
    
    # Question 5
    print("Question 5: What does the 'as' keyword do in 'except ValueError as e:'?")
    print("a) Converts the error to a string")
    print("b) Stores the error object in variable e")
    print("c) Prevents the error from occurring")
    print("d) Logs the error automatically")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'b':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'b) Stores the error object in variable e'\n")
    
    # Question 6
    print("Question 6: Can you have multiple except blocks for one try block?")
    print("a) Yes")
    print("b) No")
    answer = input("Your answer (a/b): ").lower()
    if answer == 'a':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'a) Yes'\n")
    
    # Question 7
    print("Question 7: What happens if no error occurs in a try block?")
    print("a) The program crashes")
    print("b) The except block runs anyway")
    print("c) The except block is skipped")
    print("d) An error is raised")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'c':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'c) The except block is skipped'\n")
    
    # Question 8
    print("Question 8: Which is the correct way to handle multiple error types?")
    print("a) except ValueError, TypeError:")
    print("b) except (ValueError, TypeError):")
    print("c) except ValueError and TypeError:")
    print("d) except ValueError | TypeError:")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'b':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'b) except (ValueError, TypeError):'\n")
    
    # Question 9
    print("Question 9: What is a common use case for error handling?")
    print("a) Making programs slower")
    print("b) Validating user input")
    print("c) Creating syntax errors")
    print("d) Deleting files")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'b':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'b) Validating user input'\n")
    
    # Question 10
    print("Question 10: What does 'continue' do inside a try/except block in a loop?")
    print("a) Stops the program")
    print("b) Skips to the next iteration of the loop")
    print("c) Exits the loop completely")
    print("d) Raises an error")
    answer = input("Your answer (a/b/c/d): ").lower()
    if answer == 'b':
        print("✓ Correct!\n")
        score += 1
    else:
        print("✗ Incorrect. The correct answer is 'b) Skips to the next iteration of the loop'\n")
    
    # Show final score
    print("=" * 50)
    print(f"QUIZ COMPLETE!")
    print(f"Your score: {score}/{total_questions} ({score*10}%)")
    print("=" * 50)
    
    if score == total_questions:
        print("🌟 Perfect score! You're an error handling expert!")
    elif score >= 8:
        print("👍 Great job! You understand error handling well!")
    elif score >= 6:
        print("👌 Good work! Review the material to improve further.")
    else:
        print("📚 Keep practicing! Review the test_errors.py lesson.")

if __name__ == "__main__":
    quiz()
