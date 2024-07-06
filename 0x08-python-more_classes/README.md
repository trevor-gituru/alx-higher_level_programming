# 0x08. Python - More Classes and Objects
## Tasks
### 0. Simple rectangle
Write an empty class `Rectangle` that defines a rectangle:

- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$ 
```
### 1. Real definition of a rectangle
Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

- Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
        + `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
        + if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height(self, value):` to set it:
        + `height` must be an integer, otherwise raise a `TypeError` exception with the `message height must be an integer`
        + if `height` is less than `0`, raise a `ValueError` exception with the `message height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
```
### 2. Area and Perimeter
Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

- Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
        + `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
        + if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height(self, value):` to set it:
        + `height` must be an integer, otherwise raise a `TypeError` exception with the `message height must be an integer`
        + if `height` is less than `0`, raise a `ValueError` exception with the `message height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or `height` is equal to `0`, perimeter is equal to `0`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
```
### 3. String representation
Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

- Private instance attribute: `width`:
    * property `def width(self):` to retrieve it
    * property setter `def width(self, value):` to set it:
        + `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
        + if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    * property `def height(self):` to retrieve it
    * property setter `def height(self, value):` to set it:
        + `height` must be an integer, otherwise raise a `TypeError` exception with the `message height must be an integer`
        + if `height` is less than `0`, raise a `ValueError` exception with the `message height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    * if `width` or `height` is equal to `0`, return an empty string
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/0x08$ 
```
### 
### 
### 
### 
### 
### 

## Resources
- [Object Oriented Programming (Read everything until the paragraph “Inheritance” (excluded))](https://python.swaroopch.com/oop.html)
- [Object-Oriented Programming (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)](https://python-course.eu/oop/object-oriented-programming.php)
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- [Properties vs. Getters and Setters (Mainly the last part “Public instead of Private Attributes”)](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)