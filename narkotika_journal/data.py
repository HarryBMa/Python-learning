import json
import os

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
