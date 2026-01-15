from models import Drug

# Create a drug
fentanyl = Drug("Fentanyl", "50 μg/ml", 100)

# Test it
print(fentanyl)
print(f"Balance: {fentanyl.balance} amp")

# Test successful withdrawal
if fentanyl.withdraw(20):
    print(f"✓ Uttag lyckades! Nytt saldo: {fentanyl.balance} amp")

# Test failed withdrawal
if not fentanyl.withdraw(200):
    print(f"✗ Uttag misslyckades. Saldo oförändrat: {fentanyl.balance} amp")

# Test another successful withdrawal
if fentanyl.withdraw(50):
    print(f"✓ Uttag lyckades! Nytt saldo: {fentanyl.balance} amp")