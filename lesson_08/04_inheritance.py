"""Lesson 2d — inheritance (similar to Java, no @Override)."""


class Animal:
    species = "animal"  # class attr on parent — lookup: instance → class → parents

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "..."


class Cat(Animal):  # extends Animal
    def speak(self) -> str:  # no @Override needed
        return f"{self.name} says meow"


whiskers = Cat("Whiskers")
print(whiskers.speak())
print(whiskers.species)  # "animal" — from parent class (read fallback chain)
