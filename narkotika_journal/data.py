import json
import os
from models import ControlledSubstance
# Get the directory where THIS script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.json")
TRANSACTIONS_FILE = os.path.join(SCRIPT_DIR, "transactions.json")
def save_data(inventory, transactions):
    """Save inventory and transactions to JSON files"""
    try:
        with open(INVENTORY_FILE, "w") as d: # open file for writing
            inventory = [drug.to_dict() for drug in inventory] # write inventory to file in JSON format
            json.dump(inventory, d, indent=4)
    except PermissionError:
        print("Gick inte att spara till fil: Ingen behörighet")
    except OSError as e:
        print(f"Ett fel uppstod vid sparning av inventory.json: {e}")
            
    with open(TRANSACTIONS_FILE, "w") as t: # open file for writing
        try:
            json.dump(transactions, t, indent=4) # write transactions to file in JSON format (dump=write)
        except PermissionError:
            print("Gick inte att spara till fil: Ingen behörighet")
        except OSError as e:
            print(f"Ett fel uppstod vid sparning av transactions.json: {e}")

def load_data():
    """Load inventory and transactions from JSON files"""
    DEFAULT_INVENTORY = [
            ControlledSubstance("Fentanyl", "50 μg/ml", 36, 10, "II", "Log required"),
            ControlledSubstance("Sufentanil", "5 μg/ml", 23, 10, "II", "Log required"),
            ControlledSubstance("Ketalar", "50 mg/ml", 8, 10, "II", "Log required"),
            ControlledSubstance("Morfin", "10 mg/ml", 24, 10, "II", "Log required"),
            ControlledSubstance("Remifentanil", "5 mg", 15, 10, "II", "Log required"),
            ControlledSubstance("Remifentanil", "2mg", 26, 10, "II", "Log required"),
        ]
    # Load inventory
    if os.path.exists(INVENTORY_FILE):
        try:
            with open(INVENTORY_FILE, "r") as d: # open file for reading
                inventory = [ControlledSubstance.from_dict(drug_dict) for drug_dict in json.load(d)]   # read inventory from file in JSON format (load=read)
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
    if os.path.exists(TRANSACTIONS_FILE):
        try:
            with open(TRANSACTIONS_FILE, "r") as t:
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
