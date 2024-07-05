# 0x06. Python - Classes and Objects
Concepts learnt:
- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Tasks
### 0. My first square
Write an empty class `Square` that defines a square:

- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/0x06$ 
```
### 1. Square with size
Write a class `Square` that defines a square by: (based on `0-square.py`)

- Private instance attribute: `size`
- Instantiation with size (no type/value verification)
- You are not allowed to import any module
**Why?**

Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```bash
guillaume@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/0x06$ 
```
### 2. Size validation
Write a class `Square` that defines a square by: (based on `1-square.py`)
    
- Private instance attribute: `size`
- Instantiation with optional size: `def __init__(self, size=0):`
`size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * if `size` is less than `0`, raise a `ValueError` exception with the `message size must be >= 0`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/0x06$ 
```
### 3. Area of a square
Write a class `Square` that defines a square by: (based on `2-square.py`)

- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
    * `size` must be an integer, otherwise raise a `TypeError` exception with the message `size` must be an integer
    * if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/0x06$ 
``` 
### 4. Access and update private attribute
Write a class `Square` that defines a square by: (based on `3-square.py`)

- Private instance attribute: `size`:
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        + `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        + if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module
**Why?**

*Why a getter and setter?*

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

```bash
guillaume@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/0x06$ 
```
### 5. Printing a square
Write a class `Square` that defines a square by: (based on `4-square.py`)

- Private instance attribute: `size:`
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        + `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        + if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to `0`, print an empty line
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ ./5-main.py

###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/0x06$ 
```
### 6. Coordinates of a square
Write a class `Square` that defines a square by: (based on `5-square.py`)

- Private instance attribute: `size`:
    * property `def size(self):` to retrieve it
    * property setter `def size(self, value):` to set it:
        + `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        + if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
    * property `def position(self):` to retrieve it
    * property setter `def position(self, value):` to set it:
        + position must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
    * if `size` is equal to `0`, print an empty line
    * `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/0x06$ 
```
## Resources
- [Object Oriented Programming (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet)](https://python.swaroopch.com/oop.html)
- [Object-Oriented Programming (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)](https://python-course.eu/oop/object-oriented-programming.php)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)