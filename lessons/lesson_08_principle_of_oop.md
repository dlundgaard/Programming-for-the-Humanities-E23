Object-oriented or OOP we shall call it is one of several different programming paradigms used in order to structure your code in a way that is easier to follow. It receives its name by defining objects you can interface within your Python programs.

## Objects
Objects purposely represent real-world objects or things like a cat or dog. Python objects have a collection of related properties or behaviors like meow() or bark().

## Classes
OOP in Python is class-based and your objects will be defined with the class keyword like the example below:
class Cat:
    pass
## Principle 1 - Abstraction
Abstraction is the concept of hiding all the implementation of your class away from anything outside of the class.
```py
class Dog:

    def __init__(self, name):
        self.name = name
        print(self.name + " was adopted.")

    def bark(self):
        print("woof!")


# we don't care how it works just bark
spot = Dog("spot") #=> spot was adopted.
spot.bark() #=> woof!
```

## Principle 2 - Inheritance
Inheritance is the mechanism for creating a child class that can inherit behavior and properties from a parent(derived) class.

```py
class Animal:

    def __init__(self, name):
        self.name = name
        print(self.name + " was adopted.")

    def run(self):
        print("running!")


class Dog(Animal):

    def __init__(self):
        super().init

    def bark(self):
        print("woof!")


# new dog behavior inherited from Animal parent class
spot = Dog("spot") #=> spot was adopted.
spot.run() #=> running!
```
## Principle 3 - Encapsulation
Encapsulation is the method of keeping all the state, variables, and methods private unless declared to be public.

```py
class Fish:

    def __init__(self):
        self.__size = "big"

    def get_size(self):
        print("I'm a " + self.__size + " fish")

    def set_size(self, new_size):
        self.__size = new_size

# using the getter method
oscar = Fish()
oscar.get_size()  #=> I'm a big fish

# change the size
bert = Fish()
bert.__size = "small"
bert.get_size() #=> I'm a big fish

# using setter method
fin = Fish()
fin.set_size("tiny")
fin.get_size() #=> I'm a tiny fish
```
## Principle 4 - Polymorphism
Polymorphism is a way of interfacing with objects and receiving different forms or results.

```py
class Animal:

    def __init__(self, name):
        self.name = name
        print(self.name + " was adopted.")

    def run(self):
        print("running!")


class Turtle(Animal):

    def __init__(self):
        super().init

    def run(self):
        print("running slowly!")


# we get back an interesting response
tim = Turtle("tim") #=> tim was adopted.
tim.run() #=> running slowly!
```
