from enum import Enum, auto
from icecream import ic

class MenuOptions(Enum):
    ADD = auto()
    EXIT = auto()
    DELETE = auto()
    PRINT = auto()

animals = []

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def menu():
    print("1 - Add to the list")
    print("2 - Exit")
    print("3 - Delete from the list")
    print("4 - Print the list")

def main():
    while True:
        menu()
        user_selection = input("Choose your option: ")

        if user_selection == str(MenuOptions.ADD.value):
            add_animal()
        elif user_selection == str(MenuOptions.EXIT.value):
            exit_func()
        elif user_selection == str(MenuOptions.DELETE.value):
            delete_animal()
        elif user_selection == str(MenuOptions.PRINT.value):
            print_animals()

def add_animal():
    name = input("Enter animal name: ")
    age = input("Enter animal age: ")

    new_animal = Animal(name, age)
    animals.append(new_animal)
    ic("Added to array")

def exit_func():
    print("Exiting")
    exit()

def print_animals():
    for index, animal in enumerate(animals, start=1):
        print(f"{index}. Name: {animal.name}, Age: {animal.age}")

def delete_animal():
    print_animals()
    
    if not animals:
        print("No animals to delete.")
        return

    try:
        index_to_delete = int(input("Enter the number of the animal to delete: "))
        if 1 <= index_to_delete <= len(animals):
            deleted_animal = animals.pop(index_to_delete - 1)
            print(f"Deleted animal: {deleted_animal.name}, Age: {deleted_animal.age}")
        else:
            print("Invalid index. No animal deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
