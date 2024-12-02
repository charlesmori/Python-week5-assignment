# Base class representing a general Smartphone
class Smartphone:
    def __init__(self, brand, model, operating_system):
        self.brand = brand
        self.model = model
        self.operating_system = operating_system

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Operating System: {self.operating_system}")

    def make_call(self, number):
        print(f"Calling {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")


# Subclass representing a Smartphone with a camera feature
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, operating_system, camera_quality):
        super().__init__(brand, model, operating_system)
        self.camera_quality = camera_quality  # Attribute specific to the subclass

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} quality camera...")

    def display_info(self):
        super().display_info()
        print(f"Camera Quality: {self.camera_quality}")


# Creating instances and demonstrating functionality
phone1 = Smartphone("Apple", "iPhone 14", "iOS")
phone1.display_info()
phone1.make_call("1234567890")
phone1.send_message("1234567890", "Hello, how are you?")

print("\n")

phone2 = SmartphoneWithCamera("Samsung", "Galaxy S23", "Android", "108MP")
phone2.display_info()
phone2.take_photo()
