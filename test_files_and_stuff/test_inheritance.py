"""
Test file for exploring inheritance and special methods
Lesson 9: Class Inheritance and Special Methods
"""

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
        return f"{self.name} ({self.concentration}) - {self.balance} units"
    
    def __repr__(self):
        """Return an unambiguous string representation of the Medication instance."""
        return f"Medication(name={self.name}, concentration={self.concentration}, balance={self.balance}, minimum_stock_level={self.minimum_stock_level})"
    
    def __eq__(self, other):
        """Check if two Medication instances are equal based on their attributes."""
        if not isinstance(other, Medication):
            return NotImplemented
        return (self.name == other.name and
                self.concentration == other.concentration and
                self.balance == other.balance and
                self.minimum_stock_level == other.minimum_stock_level)
    
    def __lt__(self, other):
        """Sorting medications by alphabetical order of name."""
        if not isinstance(other, Medication):
            return NotImplemented
        return self.name < other.name


class EmergencyMedication(Medication):
    """A subclass representing an emergency medication."""
    def __init__(self, name, concentration, balance, minimum_stock_level, emergency_use):
        """Initialize an EmergencyMedication instance with additional attributes."""
        super().__init__(name, concentration, balance, minimum_stock_level)
        self.emergency_use = emergency_use
    def __repr__(self):
        """Return an unambiguous string representation of the Medication instance."""
        return f"EmergencyMedication(name={self.name}, concentration={self.concentration}, balance={self.balance}, minimum_stock_level={self.minimum_stock_level}, emergency_use={self.emergency_use})"

class ControlledSubstance(Medication):
    """A subclass representing a controlled substance medication."""
    def __init__(self, name, concentration, balance, minimum_stock_level, schedule, logging_requirements):
        """Initialize a ControlledSubstance instance with additional attributes."""
        super().__init__(name, concentration, balance, minimum_stock_level)
        self.schedule = schedule
        self.logging_requirements = logging_requirements
    def __repr__(self):
        """Return an unambiguous string representation of the Medication instance."""
        return f"ControlledSubstance(name={self.name}, concentration={self.concentration}, balance={self.balance}, minimum_stock_level={self.minimum_stock_level}, schedule={self.schedule}, logging_requirements={self.logging_requirements})"

# ============= TESTS =============
if __name__ == "__main__":
    print("=== Testing Basic Medication ===")
    morphine = Medication("Morfin", "10 mg/ml", 24, 10)
    
    # Test __str__ (user-friendly)
    print(f"Using print (calls __str__): {morphine}")
    
    # Test __repr__ (developer-friendly)
    print(f"Using repr (calls __repr__): {repr(morphine)}")
    
    
    print("\n=== Testing ControlledSubstance (Inheritance) ===")
    fentanyl = ControlledSubstance(
        name="Fentanyl",
        concentration="50 μg/ml",
        balance=36,
        minimum_stock_level=10,
        schedule="II",
        logging_requirements="Strict double-lock, signature required"
    )
    print(f"Using repr on ControlledSubstance: {repr(fentanyl)}")
    print(f"Fentanyl: {fentanyl}")
    print(f"Schedule: {fentanyl.schedule}")
    print(f"Logging: {fentanyl.logging_requirements}")
    
    # Check if fentanyl is also a Medication (inheritance test)
    print(f"\nIs fentanyl a ControlledSubstance? {isinstance(fentanyl, ControlledSubstance)}")
    print(f"Is fentanyl also a Medication? {isinstance(fentanyl, Medication)}")
    
    print("\n=== Testing __eq__ (Equality) ===")
    drug1 = Medication("Ketalar", "50 mg/ml", 8, 5)
    drug2 = Medication("Ketalar", "50 mg/ml", 8, 5)
    drug3 = Medication("Ketalar", "50 mg/ml", 10, 5)  # Different balance
    
    print(f"drug1 == drug2 (same values): {drug1 == drug2}")
    print(f"drug1 == drug3 (different balance): {drug1 == drug3}")
    print(f"drug1 is drug2 (same object in memory?): {drug1 is drug2}")
    
    print("\n=== Testing __lt__ (Sorting) ===")
    medications = [
        Medication("Sufentanil", "5 μg/ml", 23, 10),
        Medication("Fentanyl", "50 μg/ml", 36, 10),
        Medication("Morfin", "10 mg/ml", 24, 10),
        Medication("Ketalar", "50 mg/ml", 8, 5),
    ]
    
    print("Before sorting:")
    for med in medications:
        print(f"  - {med.name}")
    
    medications.sort()  # Uses __lt__ to sort
    
    print("\nAfter sorting (alphabetically by name):")
    for med in medications:
        print(f"  - {med.name}")
    
    print("\n=== Testing EmergencyMedication ===")
    epinephrine = EmergencyMedication(
        name="Adrenalin",
        concentration="1 mg/ml",
        balance=12,
        minimum_stock_level=5,
        emergency_use="Anaphylaxis, cardiac arrest"
    )
    print("\n=== Testing Method Resolution ===")
    print(f"Medication repr: {repr(morphine)}")
    print(f"ControlledSubstance repr: {repr(fentanyl)}")
    print(f"EmergencyMedication repr: {repr(epinephrine)}")
    print(f"Emergency med: {epinephrine}")
    print(f"Emergency use: {epinephrine.emergency_use}")
    print(f"Is also a Medication? {isinstance(epinephrine, Medication)}")
