# Principle 1: Encapsulation
# Encapsulation is the bundling of data (attributes) and methods that operate on the data within a single unit (class).

class Chicken:
    def __init__(self, name, age):
        # Private attributes (encapsulation)
        self.__name = name
        self.__age = age

    # Public methods to access private attributes (encapsulation)
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:  # Validating input
            self.__age = age
        else:
            print("Age must be positive!")

    # General behavior of a chicken
    def cluck(self):
        return f"{self.__name} says: Cluck cluck!"

# Principle 2: Inheritance
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

class BabyChick(Chicken):  # BabyChick inherits from Chicken
    def __init__(self, name, age, color):
        # Call the parent class constructor
        super().__init__(name, age)
        self.color = color  # Additional attribute for the child class

    # Overriding the parent class method (polymorphism)
    def cluck(self):
        return f"{self.get_name()} says: Peep peep!"

# Principle 3: Polymorphism
# Polymorphism allows methods in a child class to have a different behavior from the parent class.

def make_chicken_sound(chicken):
    # This function works with any object that has a `cluck` method (polymorphism)
    print(chicken.cluck())

# Principle 4: Abstraction
# Abstraction focuses on exposing only the relevant details of an object and hiding the implementation.

class EggLayer:
    def lay_egg(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class LayingChicken(Chicken, EggLayer):  # Multiple inheritance for laying functionality
    def lay_egg(self):
        return f"{self.get_name()} lays an egg."

# Main program to demonstrate the principles

# Encapsulation in action
hen = Chicken("Henrietta", 3)
print(hen.cluck())
hen.set_age(4)
print(f"{hen.get_name()} is now {hen.get_age()} years old.")

# Inheritance and polymorphism
chick = BabyChick("Chirpy", 1, "yellow")
print(chick.cluck())  # Overridden behavior
make_chicken_sound(hen)  # Calls the parent's cluck method
make_chicken_sound(chick)  # Calls the child's cluck method

# Abstraction and multiple inheritance
layer = LayingChicken("Eggsy", 2)
print(layer.lay_egg())
