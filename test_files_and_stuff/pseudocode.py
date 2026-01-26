def save_data(inventory, transactions):
    """Save inventory and transactions to JSON files"""
    # TODO: backup existing files before overwriting, atomic write if possible? validate input data before writing?
    
    # TODO: Step 2 - Try to save inventory
        PermissionError
        OSError
        AttributeError
        TypeError
try again and log error. ask user to retry?
        
    # TODO: Step 3 - Try to save transactions
        PermissionError
        OSError
        AttributeError
        TypeError
        try again and log error. ask user to retry?
    # TODO: Step 4 - What ALWAYS needs to happen? (finally block)
        verify file integrity? log success?
    # TODO: Step 5 - How do I know if it worked?
    print("Data saved successfully.")

    User: lets start lesson 10

GitHub Copilot: I'll help you start Lesson 10 on Exception Handling! This is a crucial lesson for making your narcotic inventory system production-ready. Let me first examine your current code to understand what we're working with. Let me check the actual structure of your lesson_10 folder: 

Read [](file:///workspaces/Python-learning/lesson_10)

Read [](file:///workspaces/Python-learning)

I see! The lesson_10 is actually a file (the lesson description), and your project code is in the narkotika_journal directory. Let me check that: 

Read [](file:///workspaces/Python-learning/narkotika_journal)

Read [](file:///workspaces/Python-learning/narkotika_journal/main.py)

Read [](file:///workspaces/Python-learning/narkotika_journal/models.py)

Read [](file:///workspaces/Python-learning/narkotika_journal/inventory_handlers.py)

Read [](file:///workspaces/Python-learning/narkotika_journal/data.py)

Read [](file:///workspaces/Python-learning/narkotika_journal/utils.py)

Perfect! I can see you have a well-structured narcotic inventory system. Now let's make it bulletproof with exception handling! 🎯

## Current State Analysis

Your code already has **some** exception handling:
- ✅ `get_int_input()` handles `ValueError` for invalid integers
- ✅ `save_data()` has some file exception handling
- ✅ `load_data()` has file exception handling

But there are still vulnerabilities:
- ❌ No validation for HSA-ID format
- ❌ No custom exceptions for healthcare-specific errors  
- ❌ No handling for edge cases in withdrawal logic
- ❌ Missing `finally` blocks for critical operations
- ❌ No retry logic for user errors

## Let's Build This Step by Step

I'll create a comprehensive exception handling solution for your system. Let me start by creating custom exceptions and then enhancing each module: 

Created [](file:///workspaces/Python-learning/narkotika_journal/exceptions.py)

Great! Now let's enhance your existing files with robust exception handling. I'll update them systematically: 

Made changes.

User: dont write code for me. use a sochratic teaching style and teach me to write code

GitHub Copilot: Ah, excellent! I apologize for jumping ahead. Let me delete that file and take a teaching approach instead. 🎓 

Ran terminal command:  rm /workspaces/Python-learning/narkotika_journal/exceptions.py

Perfect! Much better approach. Let's learn this together using the Socratic method. 

## Let's Start With Discovery 🔍

Before we write any exception handling, I want you to **think like a hacker** trying to break your system. Look at your main.py file.

### Question 1: Login Vulnerability
```python
user_input = input("Skriv ditt HSA-ID: ").upper()

if user_input in authorized_users:
    print("Välkommen!")
```

**What happens if:**
1. A user types nothing (just hits Enter)?
2. A user types "HA01 OR 1=1" (SQL injection style)?
3. A user types 1000 characters?

Does your current code handle these gracefully? **What could go wrong?** 🤔

### Question 2: Menu Choice Vulnerability
You use `get_int_input()` for menu choices, which is good! But let me ask:

**In your `get_int_input()` function, what happens if:**
- The user presses Ctrl+C?
- The user types `float('inf')`?
- The function is called but the file gets corrupted mid-execution?

### Question 3: File Operations
Look at your data.py `save_data()` function:

**Critical thinking question:** 
What happens if the power goes out **during** the `json.dump()` operation? Could you end up with:
- A half-written file?
- A corrupted inventory?
- Lost data?

**How would you protect against this?**

---

## Your First Task 🎯

Before we fix anything, I want you to **test your current system** and find the breaking points:

1. **Run your program** 
2. **Try to break it** by entering bad data:
   - Empty inputs
   - Text where numbers are expected
   - Negative numbers
   - Numbers way too large
   - Special characters

**Document what breaks.** Tell me:
- What did you try?
- What happened?
- What error message did you get (if any)?
- What SHOULD have happened instead?

Once you've done this detective work, we'll design custom exceptions together. Deal? 🤝

User: 1. login just accepts users in list. every other input leads to "åtkomst nekad - ogiltigt HSA-ID" and program ends. 2. ctrl+c crashes the program. all else leads to  valueerror. 3. yes, I could. should add a finally to write data. TASK. I tried all the ones you suggested and these are the errors i found. I got the error messages I put in and the crash error keyboard interrupt.

GitHub Copilot: Excellent detective work! 🕵️ You've found the key vulnerabilities. Now let's think through **how to fix them** strategically.

## Let's Analyze Your Findings 🧠

### Finding #1: Login System
You said login either accepts valid users OR denies and exits. 

**Critical thinking questions:**
1. Is this the **right behavior** for a production system? 
2. In a real hospital, if a nurse mistypes their HSA-ID, should the whole program shut down? Or should they get another chance?
3. **What would be better?** (Hint: Think about ATMs - how many times can you enter wrong PIN?)

### Finding #2: Ctrl+C Crashes (KeyboardInterrupt)
This is a **special** type of exception. It happens when users hit Ctrl+C.

**Question:** Should we catch `KeyboardInterrupt`? Think carefully:
- **Pro:** Program exits gracefully, saves data
- **Con:** User can't force-quit a stuck program

**What do you think?** When SHOULD we allow Ctrl+C to crash, and when should we catch it?

### Finding #3: Data Corruption Risk
You said "should add a finally to write data" - **good instinct!** But wait...

**Deeper question:** If you put the file write in `finally`, it **always** runs. But what if:
- The withdrawal failed (insufficient stock)?
- The audit check failed?
- The user pressed 'Q' to cancel?

Should we **still save** in those cases? 🤔

---

## Prioritization Exercise 📊

Before we start coding, let's prioritize. Which of these is **MOST dangerous** in a hospital setting?

A. User can't exit with Ctrl+C  
B. File corruption loses all narcotic records  
C. User enters text instead of number  
D. User can withdraw more drugs than exist  

**Rank them 1-4** (1 = most critical to fix) and explain why.

---

## Let's Start With One Problem 🎯

Once you've ranked them, I want you to **start with your #1 priority**. 

For that problem:
1. **Where in your code** does it happen? (Which file, which function?)
2. **What exception** would you catch? (`ValueError`? `KeyError`? Custom exception?)
3. **What should happen** when you catch it? (Retry? Return to menu? Log and continue?)

Tell me your thinking, and then we'll write the code together for that ONE problem first. Then we'll build from there.

**Remember:** Professional code isn't written all at once - it's built incrementally, testing each piece! 💪

User: B. most critical, its the point of a logging system. C. could corrupt database if str save instead of int. A. must be able to force quit a stuck program. D. sometimes the physical storage might have more than in the digital program so this can happen. 1. data.py def save_data line 8. 2. corruption, write errors, load errors. etc 3. retry

GitHub Copilot: Excellent analysis! Your ranking is spot-on - **data integrity is everything** in a narcotic tracking system. 🎯

Now let's tackle **Problem B: File Corruption** together. You identified the right place (data.py, `save_data` function). Let's think through the **solution design** before coding.

## Design Questions for `save_data()` 🏗️

### Question 1: The Backup Strategy
You said "retry" - good! But first, let's think about backups:

**If you're about to overwrite `inventory.json`, and something goes wrong mid-write:**
- Option A: Write directly to `inventory.json` (current approach - risky!)
- Option B: Write to `inventory_temp.json` first, then rename it (atomic operation)
- Option C: Copy `inventory.json` to `inventory_backup.json` BEFORE writing

**Which option is safest? Why?** (Hint: Think about what you have left if the power fails during the write)

### Question 2: Exception Types
You said "corruption, write errors, load errors" - let's be specific.

Look at your current `save_data()`:
```python
with open(INVENTORY_FILE, "w") as d:
    inventory = [drug.to_dict() for drug in inventory]
    json.dump(inventory, d, indent=4)
```

**What exceptions could happen here?**
- `PermissionError` - already caught ✓
- `OSError` - already caught ✓
- What about `AttributeError`? (What if a drug object is corrupted and has no `to_dict()` method?)
- What about `TypeError`? (What if `json.dump()` can't serialize the data?)

**Should you catch these? How would you handle them differently?**

### Question 3: The Finally Block
You mentioned using `finally` for writes. But here's a **tricky question**:

```python
try:
    with open(INVENTORY_FILE, "w") as d:
        json.dump(inventory, d, indent=4)
except OSError as e:
    print(f"Error: {e}")
finally:
    # What goes here???
```

**What should go in `finally`?** 
- The file is already closed (the `with` statement handles that)
- The data might not have saved
- You can't "retry" the save here

**Think:** What does `finally` mean? It means "do this NO MATTER WHAT." What MUST always happen after attempting to save?

### Question 4: Retry Logic
You want to retry on failure - smart! But:

**How many times should you retry?**
- 1 time?
- 3 times?
- Infinite times?

**What should change between retries?**
- Try a different file name?
- Wait a moment (maybe file was locked)?
- Ask the user what to do?

**When should you give up?**
- After X attempts?
- When a specific error occurs?

---

## Your Next Step ✍️

I want you to **write pseudocode** (comments explaining the logic) for a better `save_data()` function. Don't write real Python yet - just describe the logic:

```python
def save_data(inventory, transactions):
    """Save inventory and transactions to JSON files"""
    # TODO: Step 1 - What should I do first? (backup? validate data?)
    
    # TODO: Step 2 - Try to save inventory
        # What exceptions to catch?
        # What to do if it fails?
        
    # TODO: Step 3 - Try to save transactions
        # Same questions...
        
    # TODO: Step 4 - What ALWAYS needs to happen? (finally block)
    
    # TODO: Step 5 - How do I know if it worked?
```

**Fill in those TODOs** with your thoughts. Then we'll turn it into real code together! 🚀

User: 1. option B is safest since data is not touched until operation is finished. option C could still fail the copying. 2. yes, attr error is good. should probably return a "n/a" or "missing". Typeerror is also good. I should be specific and not try to catch all. 3. I forgot that i used with. finally is redundant and wont run save/close. finally could be run with a check/test/read file for corruption. 4. we could set 3 times as a learning moment but it doesnt mattter for me. maybe all three? givve up after 3 attempts.

GitHub Copilot: Created 5 todos

Great progress. Here’s a focused plan and next teaching steps.

- Design atomic save strategy is now in progress. Next, we’ll refine validation, Ctrl+C policy, retries, and testing.

**Atomic Save Design**
- Purpose: Prevent partial writes to data.py.
- Questions:
  - Bold the intent: If write fails halfway, what guarantees keep `inventory.json` intact?
  - Which operation ensures “all-or-nothing” replacement: `os.replace()` vs `os.rename()`? Why choose one?
  - Where would you place a backup step so it’s only used on restore, not every success?

- Exercise:
  - Propose a helper signature: `write_json_atomic(path, payload)`.
  - Outline steps: 
    - Validate `payload` is JSON-serializable.
    - Write to `path + ".tmp"` with `json.dump(...)`.
    - Ensure data hits disk (consider `flush()`/`os.fsync()`).
    - Atomically replace original via `os.replace(tmp, path)`.
  - Identify failure points and which exceptions you’d catch per step.

**Validation + Exceptions**
- Purpose: Prevent bad data from reaching disk.
- Questions:
  - For each `ControlledSubstance`, what fields and types must be guaranteed before save?
  - Where should invalid data be rejected: in model constructors, a `validate_*()` function, or `save_data()`?
  - Which exceptions communicate intent best: `ValueError` vs your own `InvalidDataError`?

- Exercise:
  - Draft a `validate_inventory(inventory)` flow:
    - Ensure list of objects, each convertible via `to_dict()`.
    - Check `name` (str, non-empty), `concentration` (str), `balance` (int ≥ 0), `minimum_stock_level` (int ≥ 0), `schedule` (one of I–V).
    - Decide: raise on first error or accumulate all errors to report?

**Ctrl+C (KeyboardInterrupt) Policy**
- Purpose: Exit safely without hiding user control.
- Questions:
  - Where should `KeyboardInterrupt` be caught: deep inside helpers, or at the outer loop in main.py?
  - On Ctrl+C, should you: save data then exit, or exit without save to avoid racing with user intent?
- Exercise:
  - Describe your top-level `try/except KeyboardInterrupt:` behavior:
    - Print a clear message.
    - Attempt `save_data(...)` once.
    - Exit with a clean status.

**Retry + Post-Save Check**
- Purpose: Handle transient issues and verify integrity.
- Questions:
  - Which errors merit retry (e.g., `PermissionError` rarely transient vs `OSError` file lock)?
  - Do you want fixed retries (3) or a simple backoff (sleep 0.2s, 0.5s, 1s)?
- Exercise:
  - Sketch a loop around `write_json_atomic(...)`:
    - On failure, log the error, attempt again up to 3 times.
    - After success, read the file back and validate shape (e.g., keys present).
    - If read-back fails, restore from backup and report.

**Testing Scenarios**
- Purpose: Prove robustness before changing other modules.
- Propose tests:
  - Corrupt `inventory.json` (write `"{bad json"`), then run `load_data()` and observe recovery.
  - Inject a non-serializable object into `transactions` (e.g., a function), ensure validation catches `TypeError`.
  - Simulate `PermissionError` by changing file permissions; confirm retry behavior and final message.
  - Interrupt flow with `Ctrl+C` in main.py and confirm graceful exit.

**Your Turn**
- In `pseudocode.py`, refine your `save_data` TODOs into a concrete pseudocode flow for:
  - `validate_inventory`, `validate_transactions`
  - `write_json_atomic` (temp write + replace)
  - Retry loop and post-save read-back verification
  - Optional backup/restore decision points
- Share your updated pseudocode for one helper (e.g., `write_json_atomic`) and your planned `KeyboardInterrupt` handling in `main()` for review.