from datetime import datetime
from display import show_drug_list, show_drug_details
from data import save_data, load_data
from utils import get_int_input
from models import Drug

def handle_withdrawal(inventory, transactions, user_input):
    """Handle the withdrawal process including updating balances and logging."""
    show_drug_list(inventory)
    choice = get_int_input(f"Välj preparat (1 - {len(inventory)}) eller Q för att avbryta: ", 1, len(inventory))
            
    if choice is None:
        return inventory, transactions  # Skip to the next iteration of the loop if input was aborted

    choice = choice - 1  # Adjust for 0-based index

    if 0 <= choice < len(inventory):
        selected_drug = inventory[choice]
        show_drug_details(selected_drug)
        amount_taken = get_int_input("Antal amp att ta ut (eller Q för att avbryta): ", min_value=1, max_value=selected_drug.balance) # Ensure at least 1 amp is taken and not more than balance
    
        if amount_taken is None:
            return inventory, transactions
        
        # withdraw_drugs
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        old_balance = selected_drug.balance
        selected_drug.withdraw(amount_taken)
        location = str(input("till: "))
        new_balance = selected_drug.balance
        # audit
        audit_count = get_int_input("Antal för kontrollräkning: ", min_value=0) # Ensure non-negative audit count
        should_log = False  # Flag to determine if we should log the transaction
        if audit_count is None:
            # User chose to abort
            selected_drug.balance = old_balance
            print("Uttag avbrutet, räkna om?")
            return inventory, transactions
        if new_balance == audit_count:
            print("✓ Kontrollräkning stämmer!")
            should_log = True
        else:
            print(f"⚠️ AVVIKELSE! System: {new_balance}, Räknat: {audit_count}")
            accept_audit = input("Acceptera avvikelse? (j/n): ").lower()
            if accept_audit == 'j':
                selected_drug.balance = audit_count # Update balance to audit count
                new_balance = audit_count # Update new_balance to audit count
                should_log = True
            else:
                selected_drug.balance = old_balance
                print("Uttag avbrutet, räkna om?")
                return inventory, transactions
        
        # Log transaction
        if should_log:
            transaction = {
                "timestamp": timestamp,
                "drug": selected_drug.name,
                "amount": amount_taken,
                "location": location,
                "user": user_input,
                "old_balance": old_balance,
                "new_balance": new_balance,}
            transactions.append(transaction)
            save_data(inventory, transactions)
            # Print confirmation
            print(f"\n✓ REGISTRERAT")
            print(f"{selected_drug.name}: {old_balance} → {new_balance} amp")
            print(f"Tid: {timestamp}")
            print(f"Till: {location}\n")
    return inventory, transactions

def handle_deposit(inventory, transactions):
    """Handle the deposit process"""
    show_drug_list(inventory)
    choice = get_int_input(f"Välj preparat (1 - {len(inventory)}): ", 1, len(inventory)) 
    if choice is None:
        return inventory, transactions  # Skip to the next iteration of the loop if input was aborted
    else:
        choice -= 1  # Adjust for 0-based index
        if 0 <= choice < len(inventory):
            selected_drug = inventory[choice]
            show_drug_details(selected_drug)
            amount_added = get_int_input("Antal amp att lägga till: ", min_value=1) # Ensure at least 1 amp is added
            if amount_added is None:
                return inventory, transactions  # Skip to the next iteration of the loop if input was aborted
            else:
                selected_drug.deposit(amount_added) # Add the specified amount
                save_data(inventory, transactions)
                print(f"{selected_drug.name} har uppdaterats till {selected_drug.balance} amp.")
                return inventory, transactions
