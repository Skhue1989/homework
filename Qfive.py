from abc import ABC, abstractmethod


# Abstract Base Class
class FileHandler(ABC):

    @abstractmethod
    def read(self):
        """Read data from the file."""
        pass

    @abstractmethod
    def write(self, data):
        """Write data to the file."""
        pass


# Concrete Class for Text Files
class TextFileHandler(FileHandler):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)


# Concrete Class for Binary Files
class BinaryFileHandler(FileHandler):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)


# Example Usage
if __name__ == "__main__":
    # Handle a text file
    text_handler = TextFileHandler('example.txt')
    text_handler.write('Welcome to the world of JOY')
    print(text_handler.read())

    # Handle a binary file
    binary_handler = BinaryFileHandler('example.bin')
    binary_handler.write(b'\x00\x01\x02\x03')
    print(binary_handler.read())