# Base class
class Shape:
    def __init__(self, color):
        self.color = color  # Example of shared initialization logic
        print(f"Shape initialized with color: {self.color}")

    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement the 'calculate_area' method.")

# Derived class
class Rectangle(Shape):
    def __init__(self, color, width, height):
        # Call the base class constructor using super()
        super().__init__(color)
        # Additional initialization specific to Rectangle
        self.width = width
        self.height = height
        print(f"Rectangle initialized with width: {self.width}, height: {self.height}")

    def calculate_area(self):
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    # Create a Rectangle object
    rectangle = Rectangle("red", 10, 17)

    # Calculate and print the area
    area = rectangle.calculate_area()
    print(f"Area of the rectangle: {area}")
