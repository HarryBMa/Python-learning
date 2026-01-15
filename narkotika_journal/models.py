class Drug:
    """A class representing a narcotics classed drug in the inventory. """
    def __init__(self, name, concentration, balance):
        """Initialize a Drug instance with name, concentration, and balance.
        this runs when you create a new create a new Drug object.
        It sets up the attributes of the object.
        """
        self.name = name
        self.concentration = concentration
        self.balance = balance

    def __str__(self):
        """Return a string representation of the Drug instance.
        This lets you print the object in a readable format."""
        return f"{self.name} ({self.concentration}) - {self.balance} amp"

    def withdraw(self, amount):
        """Withdraw amount from balance. Returns True if successful."""
        if amount > self.balance:
            print(f"Fel: Kan inte ta ut {amount} amp. Endast {self.balance} amp tillgängligt.")
            return False
        self.balance -= amount
        return True
    
    def deposit(self, amount):
        """Add amount to balance. Returns True if successful."""
        if amount < 0:
            print(f"Fel: Kan inte sätta in ett negativt belopp: {amount} amp.")
            return False
        self.balance += amount
        return True        