#!/usr/bin/env python3
"""
Python Learning Quiz - Test Your Knowledge!
Covers Lessons 1-5 from your drug inventory system project
"""

import sys

def ask_question(question, options, correct_answer):
    """Display a question and return True if answered correctly"""
    print("\n" + "="*60)
    print(question)
    print()
    for key, value in options.items():
        print(f"  {key}) {value}")
    print()
    
    while True:
        answer = input("Your answer (or 'skip'): ").strip().lower()
        if answer == 'skip':
            print(f"⏭️  Skipped. Correct answer was: {correct_answer}")
            return False
        if answer in options:
            if answer == correct_answer:
                print("✅ Correct!")
                return True
            else:
                print(f"❌ Wrong. Correct answer was: {correct_answer}) {options[correct_answer]}")
                return False
        print("Invalid choice. Try again.")

def run_quiz():
    """Main quiz function"""
    print("🎓 PYTHON LEARNING QUIZ 🎓")
    print("="*60)
    print("Test your knowledge from Lessons 1-5!")
    print("Type your answer (a, b, c, d) or 'skip' to skip a question")
    input("\nPress Enter to start...")
    
    score = 0
    total = 0
    
    # LESSON 1: Python Basics
    print("\n\n🔹 LESSON 1: Python Basics & Project Setup")
    
    total += 1
    if ask_question(
        "What data structure stores key-value pairs?",
        {"a": "List", "b": "Dictionary", "c": "Tuple", "d": "String"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "Which statement checks if a user is in the authorized_users list?",
        {"a": "user == authorized_users", "b": "user.in(authorized_users)", 
         "c": "if user in authorized_users:", "d": "authorized_users.contains(user)"},
        "c"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What keyword defines a reusable code block?",
        {"a": "function", "b": "def", "c": "create", "d": "block"},
        "b"
    ):
        score += 1
    
    # LESSON 2: Data Structures
    print("\n\n🔹 LESSON 2: Multiple Drugs & Data Structures")
    
    total += 1
    if ask_question(
        "What does enumerate() provide in a loop?",
        {"a": "Only the items", "b": "Only the indexes", 
         "c": "Both index and item", "d": "The length of the list"},
        "c"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "How do you loop through a list called 'drugs'?",
        {"a": "loop drug in drugs:", "b": "for drug in drugs:", 
         "c": "while drug in drugs:", "d": "foreach drug in drugs:"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What is the correct structure for a list of dictionaries?",
        {"a": "[dict1, dict2, dict3]", "b": "{list1, list2, list3}", 
         "c": "(dict1, dict2, dict3)", "d": "dict[list1, list2]"},
        "a"
    ):
        score += 1
    
    # LESSON 3: Program Flow
    print("\n\n🔹 LESSON 3: Transactions & Program Flow")
    
    total += 1
    if ask_question(
        "How do you subtract from a drug's balance in a dictionary?",
        {"a": "drug.balance -= amount", "b": "drug['balance'] -= amount", 
         "c": "balance - amount", "d": "drug.subtract(amount)"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What does strftime do in the datetime module?",
        {"a": "Calculates time differences", "b": "Formats time as a string", 
         "c": "Converts string to time", "d": "Gets current timezone"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What keeps a menu running until the user logs out?",
        {"a": "for loop", "b": "if statement", 
         "c": "while loop with a flag", "d": "def statement"},
        "c"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What is a 'flag' variable typically used for?",
        {"a": "Storing user names", "b": "Controlling program flow with True/False", 
         "c": "Counting transactions", "d": "Storing file paths"},
        "b"
    ):
        score += 1
    
    # LESSON 4: File Persistence
    print("\n\n🔹 LESSON 4: File Persistence")
    
    total += 1
    if ask_question(
        "Which function saves Python objects to a JSON file?",
        {"a": "json.save()", "b": "json.write()", 
         "c": "json.dump()", "d": "json.export()"},
        "c"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "Which function reads Python objects from a JSON file?",
        {"a": "json.read()", "b": "json.load()", 
         "c": "json.import()", "d": "json.get()"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What does 'with open(filename, \"w\") as f:' do?",
        {"a": "Opens file for reading", "b": "Opens file for writing", 
         "c": "Opens file for appending", "d": "Checks if file exists"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "How do you check if 'drugs.json' exists before loading it?",
        {"a": "file.exists('drugs.json')", "b": "os.path.exists('drugs.json')", 
         "c": "json.exists('drugs.json')", "d": "if 'drugs.json':"},
        "b"
    ):
        score += 1
    
    # LESSON 5: Error Handling
    print("\n\n🔹 LESSON 5: Error Handling")
    
    total += 1
    if ask_question(
        "What structure catches errors before they crash the program?",
        {"a": "if/else", "b": "while/break", 
         "c": "try/except", "d": "for/continue"},
        "c"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What error occurs when converting invalid text to a number?",
        {"a": "TypeError", "b": "ValueError", 
         "c": "SyntaxError", "d": "NameError"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What does 'graceful degradation' mean?",
        {"a": "Program crashes with error message", "b": "Program runs faster", 
         "c": "Program continues despite errors", "d": "Program deletes bad data"},
        "c"
    ):
        score += 1
    
    # BONUS: Overall Concepts
    print("\n\n🔹 BONUS: Overall Project Understanding")
    
    total += 1
    if ask_question(
        "What are the two JSON files used in your project?",
        {"a": "data.json and history.json", "b": "drugs.json and transactions.json", 
         "c": "inventory.json and logs.json", "d": "users.json and records.json"},
        "b"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "When should data be saved in your program?",
        {"a": "Only at startup", "b": "Only at logout", 
         "c": "After every transaction and at logout", "d": "Every 5 minutes"},
        "c"
    ):
        score += 1
    
    total += 1
    if ask_question(
        "What's the main purpose of the authorized_users list?",
        {"a": "Store drug names", "b": "Control who can access the system", 
         "c": "Track transactions", "d": "Save file locations"},
        "b"
    ):
        score += 1
    
    # Final Score
    print("\n\n" + "="*60)
    print("🎯 QUIZ COMPLETE! 🎯")
    print("="*60)
    percentage = (score / total) * 100
    print(f"\nYour Score: {score}/{total} ({percentage:.1f}%)")
    
    if percentage == 100:
        print("🏆 PERFECT! You're a Python master!")
    elif percentage >= 90:
        print("🌟 EXCELLENT! You really know your stuff!")
    elif percentage >= 80:
        print("👍 GREAT JOB! You've got a solid understanding!")
    elif percentage >= 70:
        print("✅ GOOD! Just a few areas to review.")
    elif percentage >= 60:
        print("📚 NOT BAD! Review the lessons and try again.")
    else:
        print("🔄 Keep practicing! Review the lessons and retake the quiz.")
    
    print("\n" + "="*60)
    print("Check lessons learned.md to review any topics!")
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\n⏸️  Quiz interrupted. Come back when you're ready!")
        sys.exit(0)
