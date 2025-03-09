class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Meow!"

def process_sound(sound_object):
    """
    Processes a sound object by calling its make_sound() method.
    """
    print(f"The object says: {sound_object.make_sound()}")

# Create instances of Dog and Cat
my_dog = Dog("Spot")
my_cat = Cat("Lily")

# Process the sounds of both objects
process_sound(my_dog)
process_sound(my_cat)