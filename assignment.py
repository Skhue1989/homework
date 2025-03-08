class Canine:
    pass


class Dog:
    species: "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)

