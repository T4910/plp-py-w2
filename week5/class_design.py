# Assignment 1: Design Your Own Class!
# Creating a Smartphone class with attributes, methods, constructor, and inheritance

class Smartphone:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now on.")
    
    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now off.")
    
    def call(self, number):
        if self.is_on:
            print(f"Calling {number} from {self.brand} {self.model}.")
        else:
            print("Phone is off. Turn it on first.")
    
    def text(self, number, message):
        if self.is_on:
            print(f"Texting {number}: {message}")
        else:
            print("Phone is off. Turn it on first.")

# Inheritance: SmartWatch inherits from Smartphone
class SmartWatch(Smartphone):
    def __init__(self, brand, model, price, storage, has_gps):
        super().__init__(brand, model, price, storage)
        self.has_gps = has_gps
    
    def track_steps(self, steps):
        if self.is_on:
            print(f"Tracked {steps} steps on {self.brand} {self.model}.")
        else:
            print("Watch is off. Turn it on first.")
    
    # Polymorphism: Overriding the turn_on method
    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} smartwatch is now on and ready to track!")

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 15", 999, "128GB")
    phone.turn_on()
    phone.call("123-456-7890")
    phone.text("123-456-7890", "Hello!")
    phone.turn_off()
    
    watch = SmartWatch("Samsung", "Galaxy Watch 6", 399, "32GB", True)
    watch.turn_on()
    watch.track_steps(5000)
    watch.call("987-654-3210")  # Inherited method
