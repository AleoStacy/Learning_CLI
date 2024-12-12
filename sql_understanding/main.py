class String:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute
        self.__private_var = None  # Private attribute

    # Setter method for the private variable
    def set_private_var(self, value):
        self.__private_var = value

    # Getter method for the private variable
    def get_private_var(self):
        return self.__private_var


# Example usage of the class
if __name__ == "__main__":
    # Create an instance of the String class
    person = String("Alice", 30)

    # Access public attributes
    print("Name:", person.name)  # Output: Alice
    print("Age:", person.age)    # Output: 30

    # Modify the private variable using the setter method
    person.set_private_var("secret_value")

    # Access the private variable using the getter method
    print("Private Variable:", person.get_private_var())  # Output: secret_value

    # Attempt to directly access the private variable
    try:
        print(person.__private_var)  # This will raise an AttributeError
    except AttributeError:
        print("Cannot directly access private variables!")  # Output: Cannot directly access private variables!
