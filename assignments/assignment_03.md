# Assignment 3: Object Oriented Design and Programming in Python 3 #

In this assignment you have to use your knowledge of Object-Oriented Design and Object-Oriented Programming to solve the three problems in Python. The assignment has three intergrated problems and you have to _solve all three_ (not just two).

## Format ##

For your assignment you should either submit aa separate report (pdf) combined with `.py' scripts for your code _OR_ in a markdown file with code blocks (similar to our [lessons](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E22/tree/main/lesson)). If you submit a markdown file do not turn it into a pdf.

An example of a markdown code block

```py
print('This is a Python code block')
```

### Submission ###

Again, two options a) text report in pdf accompanied by Python scripts OR b) markdown with text and Python code blocks. __Please remember to hand in individual assignments even though you have developed you solution in a group__.

## Problem 1: Object-Oriented Design ##

This problem in not about code, but about designing templates that can be turned into code. Your task is to design several classes that can instantiate you (or a set of object relevant to you) in a particular user context of, for instance, a community ('Bouldering Club'), a business (e.g. 'Bookstore'), or a profession (e.g., 'BA Student'). Use UML-inspired diagrams to design your object template(s), box-and-pointer diagrams are sufficient.

We define an object as a _collection of data and associated behaviors_ and use dependency relations between types of objects (i.e., classes) to model complex objects. In Python _data_ is implemented as _attributes_ and _behavior_ as _methods_.

### Object-Oriented Analysis ###

Start with (object-oriented) analysis, e.g., identify the objects and tasks that characterize you and your interactions in the specific context (e.g., bouldering amateur, `climb()` or `get_coffee()` ...). Keep attributes (data types) and dependencies (composition, inheritance) in mind , you are going to need them later, e.g., an 'amateur boulder' is also a _person_ and a person's _sex_ may matter in a bouldering competition, but not for a BA Student's exam.

### Object-Oriented Design ###

Convert you OOA into a design of your object templates (classes) using UML. The result of this stage is an implementation specification in UML that can be implemented as a set of classes in Python. Use your knowledge of Python as an inspiration for your visual formalization. Remember that in Python we use _method_ to implement behavior and _attributes_ for data. Methods are functions attached to objects and attributes are variables similarly attacted to objects, a 'BA student', for instance, may have the attribute `enrollment_year: datetime` and method `study(duration: int, intensity: str)`. Use the [slides](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E22/blob/main/slides/slides_07.pdf) from our OOD as a reference.

## Problem 2: Object-Oriented Programming ##

In this problem, you have to implement your object template design from problem 1, using the `class` keyword. The class keyword is used to create a class. A class is like an object constructor. Use our [class implementation](https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E22/blob/main/lesson/lesson_08.md) lesson as a reference.

## Problem 3: Instantiate Class using an Entry Point Function ##

Instantiate your class (create an object) and show what it can do in an entry point function `main()`. The `main()` function is conventionally the entry point, where a Python program starts its execution. It enables high-level organization of the program's functionality, and typically has access to the command arguments given to the program when it was executed. Remember to use the `__main__` special name for the top-level environment of the program or import your class into another driver script.

ex. 

```py
def main():
    myclass.name = 'Kristoffer'

if __name__ == '__main__':
    main()
```
