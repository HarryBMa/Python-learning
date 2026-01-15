# Imports
from display import show_drug_list, show_transaction_list, show_drug_details
from inventory_handlers import handle_withdrawal, handle_deposit
from data import save_data, load_data
from utils import get_int_input

# FUNCTIONS - reusable code
def main(inventory, transactions):
    """Main program loop"""
    # Login
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
                inventory, transactions = handle_withdrawal(inventory, transactions, user_input) # Pass inventory and transactions to the function and get updated values back       
            elif menu_choice == 2:
                show_transaction_list(transactions)
            elif menu_choice == 3:
                inventory, transactions = handle_deposit(inventory, transactions) # Pass inventory and transactions to the function and get updated values back
            elif menu_choice == 4:
                running = False
                save_data(inventory, transactions)
                print("Utloggad!")
    else:
        print("Åtkomst nekad - Ogiltigt HSA-ID")
     

# VARIABLES
# Store single values (`name = "Fentanyl"`)

# LISTS - storing multiple items in order
authorized_users = ["HA01", "HA02", "MA15", "JK22"]

# DICTIONARIES as a LIST

# Load data from files (or use defaults if files don't exist)
inventory, transactions = load_data() # load inventory and transactions from JSON files

if __name__ == "__main__":
    main(inventory, transactions)