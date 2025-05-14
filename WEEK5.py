# Define the base class Smartphone
class Smartphone:
    def __init__(self, brand, model, color, storage):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage  # in GB

    def display_info(self):
        return f"{self.brand} {self.model}, Color: {self.color}, Storage: {self.storage}GB"

    def make_call(self, number):
        return f"Calling {number}..."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

# Define a subclass with additional functionality
class CameraPhone(Smartphone):
    def __init__(self, brand, model, color, storage, camera_resolution):
        super().__init__(brand, model, color, storage)
        self.camera_resolution = camera_resolution  # in MP

    def take_picture(self):
        return f"Taking a picture with {self.camera_resolution}MP camera"

# Create an object of Smartphone class
my_phone = Smartphone("Apple", "iPhone 13", "Black", 128)
print(my_phone.display_info())
print(my_phone.make_call("123456789"))

# Create an object of CameraPhone class (which inherits from Smartphone)
my_camera_phone = CameraPhone("Samsung", "Galaxy S21", "Blue", 256, 108)
print(my_camera_phone.display_info())
print(my_camera_phone.take_picture())


# Base class Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Dog class overrides move()
class Dog(Animal):
    def move(self):
        return "Running 🐕"

# Cat class overrides move()
class Cat(Animal):
    def move(self):
        return "Jumping 🐈"

# Base class Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Car class overrides move()
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Plane class overrides move()
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Create instances and demonstrate polymorphism
animals = [Dog(), Cat()]
vehicles = [Car(), Plane()]

for animal in animals:
    print(f"Animal: {animal.move()}")

for vehicle in vehicles:
    print(f"Vehicle: {vehicle.move()}")
