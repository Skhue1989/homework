from abc import ABC, abstractmethod

class FileHandler(ABC):
    """
    Abstract base class for file handlers.
    Defines the required interface for all file handler classes.
    """

    @abstractmethod
    def read(self):
        """
        Abstract method to read data from the file.
        Subclasses must implement this method.
        """
        pass

    @abstractmethod
    def write(self, data):
        """
        Abstract method to write data to the file.
        Subclasses must implement this method.
        """
        pass

class TextFileHandler(FileHandler):
    """
    Concrete class for handling text files.
    Implements the read() and write() methods for text files.
    """

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """
        Reads text data from the file.
        """
        try:
            with open(self.filename, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "File not found."

    def write(self, data):
        """
        Writes text data to the file.
        """
        try:
            with open(self.filename, 'w') as f:
                f.write(data)
            return "Data written successfully."
        except Exception as e:
            return f"Error writing to file: {e}"

class BinaryFileHandler(FileHandler):
    """
    Concrete class for handling binary files.
    Implements the read() and write() methods for binary files.
    """

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        """
        Reads binary data from the file.
        """
        try:
            with open(self.filename, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            return "File not found."

    def write(self, data):
        """
        Writes binary data to the file.
        """
        try:
            with open(self.filename, 'wb') as f:
                f.write(data)
            return "Data written successfully."
        except Exception as e:
            return f"Error writing to file: {e}"

# Example usage
text_handler = TextFileHandler("my_text_file.txt")
text_handler.write("This is some text data.")
print(text_handler.read())

binary_handler = BinaryFileHandler("my_binary_file.bin")
binary_data = b'\x00\x01\x02\x03'  # Example binary data
binary_handler.write(binary_data)
print(binary_handler.read())