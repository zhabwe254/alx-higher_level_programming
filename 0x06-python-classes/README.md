Some key points and notes based on the concepts related to Object-Oriented Programming (OOP) in Python.

### Resource 1: Object Oriented Programming (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet)

- **First-Class Everything:**
  - In Python, everything is an object. Functions, classes, and even modules are first-class objects.

- **Class and Object:**
  - A class is a blueprint for creating objects, and an object is an instance of a class.

- **Attributes and Methods:**
  - Attributes are variables that store data within a class or instance.
  - Methods are functions defined within a class.

- **__init__ Method:**
  - The `__init__` method is a special method used for initializing instances of a class.

- **Public, Protected, and Private Attributes:**
  - Attributes in Python can be public, protected, or private.
  - Public attributes can be accessed directly, protected attributes have a single leading underscore, and private attributes have a double leading underscore.

### Resource 2: Object-Oriented Programming (Be careful: in most of the following paragraphs, the author shows things the way you should not use or write a class...)

- **Data Abstraction, Encapsulation, and Information Hiding:**
  - Data abstraction involves exposing only the necessary details of an object.
  - Encapsulation involves bundling the data and methods that operate on the data into a single unit.
  - Information hiding restricts the access to some of an object's components.

- **Properties vs. Getters and Setters:**
  - Properties provide a cleaner way to use getters and setters.

- **Dynamically Creating Attributes:**
  - Python allows dynamically creating new attributes for existing instances of a class.

### Resource 3: Learn to Program 9: Object-Oriented Programming

- **Understanding Classes and Objects:**
  - A class defines a blueprint for creating objects with shared properties and behaviors.

### Resource 4: Python Classes and Objects

- **Introduction to Classes:**
  - Classes are used to create user-defined data structures.

- **__dict__ Attribute:**
  - `__dict__` is a special attribute that contains a dictionary of an object's attributes.

- **getattr Function:**
  - The `getattr` function is used to get the value of an attribute.

### General Notes:

- **Self:**
  - The `self` parameter in a method refers to the instance of the class.
  - It is used to access and modify attributes within the class.

- **Properties:**
  - Properties allow controlled access to attributes using getter and setter methods.

- **Class vs. Instance Attributes:**
  - Class attributes are shared among all instances of a class.
  - Instance attributes are specific to an instance.

- **Documentation:**
  - Ensure that your code has proper documentation (docstrings) explaining the purpose of modules, classes, and methods.

These key points cover the fundamental concepts of OOP in Python, including classes, objects, attributes, methods, encapsulation, and more. Make sure to explore the resources in detail and practice writing code to solidify your understanding.
