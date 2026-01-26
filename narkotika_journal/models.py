class Medication:
    """A class representing a medication in the inventory."""
    def __init__(self, name, concentration, balance, minimum_stock_level):
        """Initialize a Medication instance with name, concentration, and balance."""
        self.name = name
        self.concentration = concentration
        self.balance = balance
        self.minimum_stock_level = minimum_stock_level
    
    def __str__(self):
        """Return a string representation of the Medication instance."""
        return f"{self.name} ({self.concentration}) - {self.balance} amp"
    
    def __repr__(self):
        """Return an unambiguous string representation of the Medication instance."""
        return f"Medication(name={self.name}, concentration={self.concentration}, balance={self.balance}, minimum_stock_level={self.minimum_stock_level})"
    
    def __eq__(self, other):
        """Check if two Medication instances are equal based on their attributes."""
        if not isinstance(other, Medication):
            return NotImplemented
        return (self.name == other.name and
                self.concentration == other.concentration and

    
    def __lt__(self, other):
        """Sorting medications by alphabetical order of name."""
        if not isinstance(other, Medication):
            return NotImplemented
        return self.name < other.name
  
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
  


class ControlledSubstance(Medication):
    """A subclass representing a controlled substance medication."""
    def __init__(self, name, concentration, balance, minimum_stock_level, schedule, logging_requirements):
        """Initialize a ControlledSubstance instance with additional attributes."""
        super().__init__(name, concentration, balance, minimum_stock_level)
        self.schedule = schedule
        self.logging_requirements = logging_requirements
    
    def __repr__(self):
        """Return an unambiguous string representation of the ControlledSubstance instance."""
        return f"ControlledSubstance(name={self.name}, concentration={self.concentration}, balance={self.balance}, minimum_stock_level={self.minimum_stock_level}, schedule={self.schedule}, logging_requirements={self.logging_requirements})"

    def to_dict(self):
        """Convert the ControlledSubstance instance to a dictionary."""
        return {
            "name": self.name,
            "concentration": self.concentration,
            "balance": self.balance,
            "minimum_stock_level": self.minimum_stock_level,
            "schedule": self.schedule,
            "logging_requirements": self.logging_requirements
        }

    @classmethod
    def from_dict(cls, drug_dict):
        """Create a ControlledSubstance instance from a dictionary.
        
        This is a CLASS method, not an instance method.
        - 'cls' represents the ControlledSubstance class itself
        - Can be called without having an object first
        - Usage: ControlledSubstance.from_dict(some_dict)
        """
        return cls(
            drug_dict["name"], 
            drug_dict["concentration"], 
            drug_dict["balance"],
            drug_dict["minimum_stock_level"],
            drug_dict["schedule"],
            drug_dict["logging_requirements"]
        )
