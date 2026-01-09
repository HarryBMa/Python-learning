# Imports
from datetime import datetime
import json
import os
# VARIABLES


# LISTS - storing multiple items in order
authorized_users = ["HA01", "HA02", "MA15", "JK22"]

# FUNCTIONS - reusable code
def save_data(drugs, transactions):
	"""Save drugs and transactions to JSON files"""
	with open("drugs.json", "w") as d:
		json.dump(drugs, d, indent=4)
	with open("transactions.json", "w") as t:
		json.dump(transactions, t, indent=4)

def load_data():
    """Load drugs and transactions from JSON files"""
    
    # Load drugs
    if os.path.exists("drugs.json"):
        with open("drugs.json", "r") as d:
            drugs = json.load(d)
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
        with open("transactions.json", "r") as t:
            transactions = json.load(t)
    else:
        # Start with empty transaction list
        transactions = []
    
    return drugs, transactions
       
def show_drug_list(drugs):
    """Display all drugs with their numbers"""
    print("\n=== TILLGÄNGLIGA PREPARAT ===")
    for index, drug in enumerate(drugs, start=1):
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

def withdraw_drugs():
    """Withdraw input amount from selected drug"""
  #  old_balance = selected_drug["balance"]
#    selected_drug["balance"] -= amount_taken
#    if old_balance > 0:
#        new_balance = selected_drug["balance"]
#        transaction = {
#	           "timestamp": timestamp,
#	           "drug": selected_drug["name"],
#	           "amount": amount_taken,
#	           "location": location,
#	           "user": user_input,
#	           "old_balance": old_balance,
#	           "new_balance": new_balance,}
#        transactions.append(transaction)
#    else:
#        print("Uttag för stort")

def deposit_drugs():
    """Deposit input amount to selected drug"""
    pass
    
# DICTIONARIES as a LIST

# Load data from files (or use defaults if files don't exist)
drugs, transactions = load_data()

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
		
		menu_choice = input("Välj: ")
		if menu_choice == "1":
			show_drug_list(drugs)
			choice = int(input(f"Välj preparat (1 - {len(drugs)}): ")) - 1
			
			if 0 <= choice < len(drugs):
				selected_drug = drugs[choice]
				show_drug_details(selected_drug)
				amount_taken = int(input("Antal amp att ta ut: "))
			
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
					audit_count = int(input("Antal för kontrollräkning: "))
					should_log = False
		
					if new_balance == audit_count:
						print("✓ Kontrollräkning stämmer!")
						should_log = True
					else:
						print(f"⚠️ AVVIKELSE! System: {new_balance}, Räknat: {audit_count}")
						accept_audit = input("Acceptera avvikelse? (j/n): ").lower()
						if accept_audit == 'j':
							selected_drug["balance"] = audit_count
							new_balance = audit_count
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
		elif menu_choice == "2":
			show_transaction_list(transactions)
		elif menu_choice == "3":
			show_drug_list(drugs)
			choice = int(input(f"Välj preparat (1 - {len(drugs)}): ")) - 1
			if 0 <= choice < len(drugs):
				selected_drug = drugs[choice]
				show_drug_details(selected_drug)
				amount_added = int(input("Antal amp att lägga till: "))
				selected_drug["balance"] += amount_added
				save_data(drugs, transactions)
				print(f"{selected_drug['name']} har uppdaterats till {selected_drug['balance']} amp.")
		elif menu_choice == "4":
			running = False
			save_data(drugs, transactions)
			print("Utloggad!")
		else:
			print("ogiltigt val")
else:
	print("Åtkomst nekad - Ogiltigt HSA-ID")