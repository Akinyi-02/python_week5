
# Assignment 1: Design Your Own Class

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def charge(self):
        print(f"{self.model} is charging.")

    def use(self, hours):
        if self.battery_life >= hours:
            self.battery_life -= hours
            print(f"Used {self.model} for {hours} hours. Remaining battery: {self.battery_life} hours.")
        else:
            print(f"Not enough battery to use for {hours} hours. Please charge {self.model}.")

# Subclass with an additional feature
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def game(self, hours):
        if self.battery_life >= hours:
            self.battery_life -= hours
            print(f"Played games for {hours} hours. Remaining battery: {self.battery_life} hours.")
            if self.cooling_system:
                print("Cooling system activated to prevent overheating.")
        else:
            print("Not enough battery to play games. Please charge the phone.")

# Testing Assignment 1
print("Testing Assignment 1: Smartphone Class")
phone = Smartphone("Samsung", "Galaxy S21", 128, 20)
phone.charge()  
phone.use(5)  
phone.use(16)   

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 24, True)
gaming_phone.charge()      
gaming_phone.game(6)      
gaming_phone.use(20)       

print("\n")



# Polymorphism with Vehicles

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Testing the classes
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()

    print("Testing individual classes:")
    car.move()   
    plane.move() 
    boat.move()  

    print("\nTesting polymorphism with a list:")
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()
