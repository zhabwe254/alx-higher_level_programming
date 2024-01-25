Functions in Python:
1. Defining a Function:
Use the def keyword.
Syntax: def function_name(parameters):
python
Copy code
def greet(name):
    print("Hello, " + name + "!")
2. Function Parameters:
Parameters are variables that are used in the function definition.
Arguments are the values passed to the function when called.
python
Copy code
def add(a, b):
    return a + b

result = add(3, 4)  # result is now 7
3. Return Statement:
Use the return keyword to return a value from a function.
python
Copy code
def square(x):
    return x ** 2

result = square(5)  # result is now 25
4. Default Parameters:
Assign default values to parameters.
python
Copy code
def power(x, exp=2):
    return x ** exp

result = power(3)  # result is 9
5. Variable Scope:
Variables inside a function have local scope, unless declared as global.
Parameters are local variables.
6. Lambda Functions:
Anonymous functions defined using the lambda keyword.
python
Copy code
square = lambda x: x ** 2
Loops in Python:
1. For Loop:
Iterates over a sequence (list, tuple, string, etc.).
Syntax: for variable in sequence:
python
Copy code
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
2. Range Function:
Generates a sequence of numbers.
python
Copy code
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
3. While Loop:
Repeats a block of code while a condition is true.
Syntax: while condition:
python
Copy code
count = 0
while count < 5:
    print(count)
    count += 1
4. Break and Continue:
break exits the loop prematurely.
continue skips the rest of the code inside the loop for the current iteration.
python
Copy code
for i in range(10):
    if i == 5:
        break
    print(i)  # prints 0 to 4
5. Nested Loops:
A loop inside another loop.
python
Copy code
for i in range(3):
    for j in range(2):
        print(i, j)
6. Looping Through Dictionaries:
Iterate through keys, values, or items.
python
Copy code
person = {"name": "John", "age": 30}
for key, value in person.items():
    print(key, value)
These notes cover the basics of functions and loops in Python. Practice is crucial for mastering these concepts, so try implementing them in small programs to reinforce your understanding.
