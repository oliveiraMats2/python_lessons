class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("O animal está fazendo um som.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("O cachorro está latindo.")


animal = Animal("Animal")
animal.speak()  # Output: O animal está fazendo um som.

dog = Dog("Fido")
dog.speak()  # Output: O cachorro está latindo.
