import math

# -----------------------------
# OOP Exercise 1
# -----------------------------
print("=========== OOP Exercise 1 ===========")


class Vehicle:
    # __init__ runs when you create an object
    # self means "this object"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed  # instance attribute
        self.mileage = mileage  # instance attribute


v1 = Vehicle(180, 12)
print("Max speed:", v1.max_speed)
print("Mileage:", v1.mileage)


# -----------------------------
# OOP Exercise 2
# -----------------------------
print("\n=========== OOP Exercise 2 ===========")


class VehicleEmpty:
    pass  # pass means "do nothing"


obj = VehicleEmpty()
print("Created object:", obj)


# -----------------------------
# OOP Exercise 3
# -----------------------------
print("\n=========== OOP Exercise 3 ===========")


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass  # inherits everything from Vehicle


School_bus = Bus("School Volvo", 180, 12)
print(
    "Vehicle Name:",
    School_bus.name,
    "Speed:",
    School_bus.max_speed,
    "Mileage:",
    School_bus.mileage,
)


# -----------------------------
# OOP Exercise 4
# -----------------------------
print("\n=========== OOP Exercise 4 ===========")


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (
            "The seating capacity of a "
            + self.name
            + " is "
            + str(capacity)
            + " passengers"
        )


class Bus(Vehicle):
    # default capacity is 50 if not provided
    def seating_capacity(self, capacity=50):
        return "The seating capacity of a bus is " + str(capacity) + " passengers"


bus1 = Bus("bus", 180, 12)
print(bus1.seating_capacity())


# -----------------------------
# OOP Exercise 5
# -----------------------------
print("\n=========== OOP Exercise 5 ===========")


class Vehicle:
    color = "White"  # class attribute (same for every object)

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


bus = Bus("School Volvo", 180, 12)
car = Car("Audi Q5", 240, 18)

print(
    "Color:",
    bus.color + ", Vehicle name:",
    bus.name + ", Speed:",
    bus.max_speed,
    ", Mileage:",
    bus.mileage,
)
print(
    "Color:",
    car.color + ", Vehicle name:",
    car.name + ", Speed:",
    car.max_speed,
    ", Mileage:",
    car.mileage,
)


# -----------------------------
# OOP Exercise 6
# -----------------------------
print("\n=========== OOP Exercise 6 ===========")


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        # default fare rule
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        # get the parent fare first
        base_fare = super().fare()
        # add 10% maintenance charge
        return base_fare + (0.10 * base_fare)


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


# -----------------------------
# OOP Exercise 7
# -----------------------------
print("\n=========== OOP Exercise 7 ===========")


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

# type(obj) tells you the class of the object
print("School_bus belongs to:", type(School_bus))


# -----------------------------
# OOP Exercise 8
# -----------------------------
print("\n=========== OOP Exercise 8 ===========")


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)

# isinstance checks if object is an instance of a class (or any of its parents)
print("Is School_bus an instance of Vehicle?", isinstance(School_bus, Vehicle))


# -----------------------------
# OOP Exercise 9
# -----------------------------
print("\n=========== OOP Exercise 9 ===========")


class Animal:
    pass


class Dog(Animal):
    pass


class Puppy(Dog):
    pass


class Cat:
    pass


# issubclass checks class inheritance relationship
print("Dog is a subclass of Animal? ->", issubclass(Dog, Animal))
print("Animal is a subclass of Dog? ->", issubclass(Animal, Dog))
print("Cat is a subclass of Animal? ->", issubclass(Cat, Animal))
print("Puppy is a subclass of Animal ->", issubclass(Puppy, Animal))


# -----------------------------
# OOP Exercise 10
# -----------------------------
print("\n=========== OOP Exercise 10 ===========")


class Shape:
    def area(self):
        # This forces subclasses to implement their own area
        raise NotImplementedError("Area method must be implemented by subclasses")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # area of circle = pi * r^2
        return math.pi * (self.radius**2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # area of square = side * side
        return self.side * self.side


shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())
