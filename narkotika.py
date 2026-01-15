# Imports
from datetime import datetime
import json
import os

# Input validation helper
def get_int_input(prompt, min_value=None, max_value=None):
    """Get validated integer input from user"""
    while True:
        try:
            value: int = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Värdet måste vara minst {min_value}. Försök igen.")
                continue
            if max_value is not None and value > max_value:
                print(f"Värdet får inte överstiga {max_value}. Försök igen.")
                continue

        except ValueError:
            print("Ogiltigt värde. Ange ett heltal.")
        
        else:
            print(f"Inmatat värde: {value}") 
            return value
# VARIABLES
# Store single values (`name = "Fentanyl"`)

# LISTS - storing multiple items in order
authorized_users = ["HA01", "HA02", "MA15", "JK22"]

# FUNCTIONS - reusable code
def save_data(drugs, transactions):
    """Save drugs and transactions to JSON files"""
    with open("drugs.json", "w") as d: # open file for writing
        try:
            json.dump(drugs, d, indent=4) # write drugs to file in JSON format
        except Exception as e:
            print("Gick inte att spara till fil:", e)

    with open("transactions.json", "w") as t: # open file for writing
        try:
            json.dump(transactions, t, indent=4) # write transactions to file in JSON format (dump=write)
        except Exception as e:
            print("Gick inte att spara till fil:", e)

def load_data():
    """Load drugs and transactions from JSON files"""
    
    # Load drugs
    if os.path.exists("drugs.json"):
        try:
            with open("drugs.json", "r") as d: # open file for reading
                drugs = json.load(d)   # read drugs from file in JSON format (load=read)
        except Exception as e:
            print("Gick inte att läsa från fil:", e)
    else:
        # Use default drugs
        drugs = [
            {"name": "Fentanyl", "concentration": "50 μg/ml", "balance": 36},
            {"name": "Sufentanil", "concentration": "5 μg/ml", "balance": 23},
            {"name": "Ketalar", "concentration": "50 mg/ml", "balance": 8},
            {"name": "Morfin", "concentration": "10 mg/ml", "balance": 24},
            {"name": "Remifentanil", "concentration": "5 mg", "balance": 15},
            {"name": "Remifentanil", "concentration": "2mg", "balance": 26},
        ]
    
    # Load transactions
    if os.path.exists("transactions.json"):
        try:
            with open("transactions.json", "r") as t:
                transactions = json.load(t)
        except Exception as e:
            print("Gick inte att läsa från fil:", e)
    else:
        # Start with empty transaction list
        transactions = []
    
    return drugs, transactions


def show_drug_list(drugs):
    """Display all drugs with their numbers"""
    print("\n=== TILLGÄNGLIGA PREPARAT ===")
    for index, drug in enumerate(drugs, start=1): # start=1 to number from 1 instead of 0
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


# DICTIONARIES as a LIST

# Load data from files (or use defaults if files don't exist)
drugs, transactions = load_data() #list of dictionaries 


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
            show_drug_list(drugs)
            choice = get_int_input(f"Välj preparat (1 - {len(drugs)}): ", 1, len(drugs)) - 1
            
            if 0 <= choice < len(drugs):
                selected_drug = drugs[choice]
                show_drug_details(selected_drug)
                amount_taken = get_int_input("Antal amp att ta ut: ", min_value=1, max_value=selected_drug["balance"]) # Ensure at least 1 amp is taken and not more than balance
            
                if amount_taken > selected_drug["balance"]:
                    print(f"Uttag för stort! Det finns bara {selected_drug['balance']} amp kvar.")
            
                else:
                    # withdraw_drugs
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                    old_balance = selected_drug["balance"]
                    selected_drug["balance"] -= amount_taken
                    location = str(input("till: "))
                    new_balance = selected_drug["balance"]
                    
                    # audit
                    audit_count = get_int_input("Antal för kontrollräkning: ", min_value=0) # Ensure non-negative audit count
                    should_log = False  # Flag to determine if we should log the transaction

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
                        save_data(drugs, transactions)
                        # Print confirmation
                        print(f"\n✓ REGISTRERAT")
                        print(f"{selected_drug['name']}: {old_balance} → {new_balance} amp")
                        print(f"Tid: {timestamp}")
                        print(f"Till: {location}\n")
        elif menu_choice == 2:
            show_transaction_list(transactions)
        elif menu_choice == 3:
            show_drug_list(drugs)
            choice = get_int_input(f"Välj preparat (1 - {len(drugs)}): ", 1, len(drugs)) - 1 # Adjust for 0-based index and ensure valid choice
            if 0 <= choice < len(drugs):
                selected_drug = drugs[choice]
                show_drug_details(selected_drug)
                amount_added = get_int_input("Antal amp att lägga till: ", min_value=1) # Ensure at least 1 amp is added
                selected_drug["balance"] += amount_added
                save_data(drugs, transactions)
                print(f"{selected_drug['name']} har uppdaterats till {selected_drug['balance']} amp.")
        elif menu_choice == 4:
            running = False
            save_data(drugs, transactions)
            print("Utloggad!")
        else:
            print("ogiltigt val")
else:
    print("Åtkomst nekad - Ogiltigt HSA-ID")