class Vehicle:
    """
    Base class representing a generic vehicle.
    """

    def __init__(self, make, model):
        """
        Initializes a Vehicle object.

        Args:
            make (str): The make of the vehicle.
            model (str): The model of the vehicle.
        """
        self.make = make
        self.model = model

    def start_engine(self):
        """
        Starts the engine of the vehicle.  This is a generic implementation.
        """
        return "Generic engine start."

    def get_description(self):
        """
        Returns a description of the vehicle.
        """
        return f"This is a {self.make} {self.model}."


class Car(Vehicle):
    """
    Subclass representing a car.
    """

    def __init__(self, make, model, num_doors):
        """
        Initializes a Car object.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            num_doors (int): The number of doors the car has.
        """
        super().__init__(make, model)  # Call the Vehicle class's initializer
        self.num_doors = num_doors

    def start_engine(self):
        """
        Overrides the start_engine method for cars.
        """
        return "Car engine starting... Vroom vroom!"

    def get_description(self):
        """
        Overrides the get_description method for cars.
        """
        return f"This is a {self.make} {self.model} with {self.num_doors} doors."


class Bike(Vehicle):
    """
    Subclass representing a bike.
    """

    def __init__(self, make, model, has_basket=False):
        """
        Initializes a Bike object.

        Args:
            make (str): The make of the bike.
            model (str): The model of the bike.
            has_basket (bool): Whether the bike has a basket (default: False).
        """
        super().__init__(make, model)
        self.has_basket = has_basket

    def start_engine(self):
        """
        Overrides the start_engine method for bikes.
        """
        return "Bike has no engine!"

    def get_description(self):
        """
        Overrides the get_description method for bikes.
        """
        basket_text = "with a basket" if self.has_basket else "without a basket"
        return f"This is a {self.make} {self.model} {basket_text}."


# Example usage
generic_vehicle = Vehicle("Generic Motors", "Base Model")
print(generic_vehicle.get_description())  # Output: This is a Generic Motors Base Model.
print(generic_vehicle.start_engine())  # Output: Generic engine start.


my_car = Car("Toyota", "Corolla", 4)
print(my_car.get_description())  # Output: This is a Toyota Corolla with 4 doors.
print(my_car.start_engine())  # Output: Car engine starting... Vroom vroom!


my_bike = Bike("Schwinn", "Cruiser", True)
print(my_bike.get_description())  # Output: This is a Schwinn Cruiser with a basket.
print(my_bike.start_engine())  # Output: Bike has no engine!