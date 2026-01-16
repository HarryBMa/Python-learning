from models import Drug

def show_drug_list(inventory):
    """Display all inventory with their numbers"""
    print("\n=== TILLGÄNGLIGA PREPARAT ===")
    for index, drug in enumerate(inventory, start=1): # start=1 to number from 1 instead of 0
        print(f"{index}. {drug.name} {drug.concentration} - {drug.balance} amp")
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