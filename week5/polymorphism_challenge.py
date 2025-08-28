# Activity 2: Polymorphism Challenge!
# Creating classes with the same method name but different implementations

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass  # Base class method, to be overridden

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print(f"{self.name} is sailing on the water. ⛵")

# Example usage demonstrating polymorphism
if __name__ == "__main__":
    vehicles = [
        Car("Toyota Camry"),
        Plane("Boeing 747"),
        Boat("Yacht")
    ]
    
    for vehicle in vehicles:
        vehicle.move()
