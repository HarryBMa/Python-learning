import json
import os
from models import Drug

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
            Drug("Fentanyl", "50 μg/ml", 36),
            Drug("Sufentanil", "5 μg/ml", 23),
            Drug("Ketalar", "50 mg/ml", 8),
            Drug("Morfin", "10 mg/ml", 24),
            Drug("Remifentanil", "5 mg", 15),
            Drug("Remifentanil", "2mg", 26),
        ]
    # Load inventory
    if os.path.exists("inventory.json"):
        try:
            with open("inventory.json", "r") as d: # open file for reading
                inventory = [Drug.from_dict(drug_dict) for drug_dict in json.load(d)]   # read inventory from file in JSON format (load=read)
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
