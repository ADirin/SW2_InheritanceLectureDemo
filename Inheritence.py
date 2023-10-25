# Parent class (or base class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Child class (or derived class) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Create an instance of the Dog class
dog = Dog("Buddy")

# Call the speak method of the Dog class
print(dog.speak())

print('----------------------------')
# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Parent class inheriting from Animal
class Mammal(Animal):
    def speak(self):
        pass

# Child class inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Woof!"

# Create an instance of the Dog class
dog = Dog("Buddy")

# Call the speak method of the Dog class
print(dog.speak())


print('***************')
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Child class 1 inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Child class 2 inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method of the Dog and Cat instances
print(dog.speak())
print(cat.speak())

print('##########################')
# Grandparent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Parent class inheriting from Animal
class Mammal(Animal):
    def speak(self):
        pass

# Child class 1 inheriting from Mammal
class Dog(Mammal):
    def speak(self):
        return f"{self.name} says Woof!"

# Child class 2 inheriting from Mammal
class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method of the Dog and Cat instances
print(dog.speak())
print(cat.speak())

print("¤¤¤¤¤¤¤¤¤¤¤EXTERNAL API¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
import requests

# Define the base URL of the API
base_url = "https://jsonplaceholder.typicode.com"


# Function to get a list of users from the API
def get_users():
    response = requests.get(f"{base_url}/users")

    if response.status_code == 200:
        users = response.json()
        return users
    else:
        return None


# Call the function to get the list of users
users = get_users()

if users:
    for user in users:
        print(f"User ID: {user['id']}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print("\n")
else:
    print("Failed to retrieve user data from the API.")