# Imports
from datetime import datetime
import json
import os

# FUNCTIONS - reusable code
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
        
def handle_withdrawal(inventory, transactions, user_input, choice):
    """Handle the withdrawal process including updating balances and logging."""
    show_drug_list(inventory)
    choice = get_int_input(f"Välj preparat (1 - {len(inventory)}) eller Q för att avbryta: ", 1, len(inventory))
            
    if choice is None:
        return inventory, transactions  # Skip to the next iteration of the loop if input was aborted

    choice = choice - 1  # Adjust for 0-based index

    if 0 <= choice < len(inventory):
        selected_drug = inventory[choice]
        show_drug_details(selected_drug)
        amount_taken = get_int_input("Antal amp att ta ut (eller Q för att avbryta): ", min_value=1, max_value=selected_drug["balance"]) # Ensure at least 1 amp is taken and not more than balance
    
        if amount_taken is None:
            return inventory, transactions
        # withdraw_drugs
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        old_balance = selected_drug["balance"]
        selected_drug["balance"] -= amount_taken
        location = str(input("till: "))
        new_balance = selected_drug["balance"]
        # audit
        audit_count = get_int_input("Antal för kontrollräkning: ", min_value=0) # Ensure non-negative audit count
        should_log = False  # Flag to determine if we should log the transaction
        if audit_count is None:
            # User chose to abort
            selected_drug["balance"] = old_balance
            print("Uttag avbrutet, räkna om?")
            return inventory, transactions
        if new_balance == audit_count:
            print("✓ Kontrollräkning stämmer!")
            should_log = True
        else:
            print(f"⚠️ AVVIKELSE! System: {new_balance}, Räknat: {audit_count}")
            accept_audit = input("Acceptera avvikelse? (j/n): ").lower()
            if accept_audit == 'j':
                selected_drug["balance"] = audit_count # Update balance to audit count
                new_balance = audit_count # Update new_balance to audit count
                should_log = True
            else:
                selected_drug["balance"] = old_balance
                print("Uttag avbrutet, räkna om?")
                return inventory, transactions
        
        # Log transaction
        if should_log:
            transaction = {
                "timestamp": timestamp,
                "drug": selected_drug["name"],
                "amount": amount_taken,
                "location": location,
                "user": user_input,
                "old_balance": old_balance,
                "new_balance": new_balance,}
            transactions.append(transaction)
            save_data(inventory, transactions)
            # Print confirmation
            print(f"\n✓ REGISTRERAT")
            print(f"{selected_drug['name']}: {old_balance} → {new_balance} amp")
            print(f"Tid: {timestamp}")
            print(f"Till: {location}\n")
    return inventory, transactions

def save_data(inventory, transactions):
    """Save inventory and transactions to JSON files"""
    with open("inventory.json", "w") as d: # open file for writing
        try:
            json.dump(inventory, d, indent=4) # write inventory to file in JSON format
        except PermissionError:
            print("Gick inte att spara till fil: Ingen behörighet")
        except OSError as e:
            print(f"Ett fel uppstod vid sparning av inventory.json: {e}")
            
    with open("transactions.json", "w") as t: # open file for writing
        try:
            json.dump(transactions, t, indent=4) # write transactions to file in JSON format (dump=write)
        except PermissionError:
            print("Gick inte att spara till fil: Ingen behörighet")
        except OSError as e:
            print(f"Ett fel uppstod vid sparning av transactions.json: {e}")

def load_data():
    """Load inventory and transactions from JSON files"""
    DEFAULT_INVENTORY = [
            {"name": "Fentanyl", "concentration": "50 μg/ml", "balance": 36},
            {"name": "Sufentanil", "concentration": "5 μg/ml", "balance": 23},
            {"name": "Ketalar", "concentration": "50 mg/ml", "balance": 8},
            {"name": "Morfin", "concentration": "10 mg/ml", "balance": 24},
            {"name": "Remifentanil", "concentration": "5 mg", "balance": 15},
            {"name": "Remifentanil", "concentration": "2mg", "balance": 26},
        ]
    # Load inventory
    if os.path.exists("inventory.json"):
        try:
            with open("inventory.json", "r") as d: # open file for reading
                inventory = json.load(d)   # read inventory from file in JSON format (load=read)
        except json.JSONDecodeError:
            print("Gick inte att läsa från fil: återställer till standardvärden")
            inventory = DEFAULT_INVENTORY
        except FileNotFoundError:
            print("Fil hittades inte: återställer till standardvärden")
            inventory = DEFAULT_INVENTORY
        except PermissionError:
            print("Ingen behörighet att läsa fil: återställer till standardvärden")
            inventory = DEFAULT_INVENTORY

    else:
        # Use default inventory
        inventory = DEFAULT_INVENTORY
            
    # Load transactions
    if os.path.exists("transactions.json"):
        try:
            with open("transactions.json", "r") as t:
                transactions = json.load(t)
        except json.JSONDecodeError:
            print("Gick inte att läsa från fil: återställer till standardvärden")
            transactions = []
        except FileNotFoundError:
            print("Fil hittades inte: återställer till standardvärden")
            transactions = []
        except PermissionError:
            print("Ingen behörighet att läsa fil: återställer till standardvärden")
            transactions = []
    else:
        # Start with empty transaction list
        transactions = []
    
    return inventory, transactions


def show_drug_list(inventory):
    """Display all inventory with their numbers"""
    print("\n=== TILLGÄNGLIGA PREPARAT ===")
    for index, drug in enumerate(inventory, start=1): # start=1 to number from 1 instead of 0
        print(f"{index}. {drug['name']} {drug['concentration']} - {drug['balance']} amp")
    print()


def show_transaction_list(transactions):
    """Display a list of transactions"""
    print("\n=== SENASTE UTTAG ===")
    for tx in transactions:
        print(f"""
Tidpunkt: {tx['timestamp']}
Läkemedel: {tx["drug"]}
Uttaget: {tx["amount"]}
Till: {tx["location"]}
Av: {tx["user"]}
Antal innan uttag: {tx["old_balance"]}
Antal efter uttag: {tx["new_balance"]}""")


def show_drug_details(drug):
    """Display selected drug details"""
    print(f"""
--- VALT PREPARAT ---
Namn: {drug['name']}
Koncentration: {drug['concentration']}
Saldo: {drug['balance']} ampuller
""")
# VARIABLES
# Store single values (`name = "Fentanyl"`)

# LISTS - storing multiple items in order
authorized_users = ["HA01", "HA02", "MA15", "JK22"]

# DICTIONARIES as a LIST

# Load data from files (or use defaults if files don't exist)
inventory, transactions = load_data() #list of dictionaries 

user_input = input("Skriv ditt HSA-ID: ").upper()

if user_input in authorized_users:
    print("Välkommen!")
    running = True
    while running:
        print("\n= MENY =")
        print("1. Nytt uttag")
        print("2. Visa transaktioner")
        print("3. Fyll på")
        print("4. Logga ut")

        menu_choice = get_int_input("Välj: ", 1, 4) # Ensure valid menu choice between 1 and 4
        if menu_choice == 1:
            inventory, transactions = handle_withdrawal(inventory, transactions, user_input, None) # Pass inventory and transactions to the function and get updated values back
           
        elif menu_choice == 2:
            show_transaction_list(transactions)
        elif menu_choice == 3:
            show_drug_list(inventory)
            choice = get_int_input(f"Välj preparat (1 - {len(inventory)}): ", 1, len(inventory)) 
            if choice is None:
                continue  # Skip to the next iteration of the loop if input was aborted
            else:
                choice -= 1  # Adjust for 0-based index
                if 0 <= choice < len(inventory):
                    selected_drug = inventory[choice]
                    show_drug_details(selected_drug)
                    amount_added = get_int_input("Antal amp att lägga till: ", min_value=1) # Ensure at least 1 amp is added
                    if amount_added is None:
                        continue  # Skip to the next iteration of the loop if input was aborted
                    else:
                        selected_drug["balance"] += amount_added
                        save_data(inventory, transactions)
                        print(f"{selected_drug['name']} har uppdaterats till {selected_drug['balance']} amp.")
        elif menu_choice == 4:
            running = False
            save_data(inventory, transactions)
            print("Utloggad!")
else:
    print("Åtkomst nekad - Ogiltigt HSA-ID")