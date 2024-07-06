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
### 4. Eval is magic
Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

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
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
```
### 5. Detect instance deletion
Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)

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
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 
```
### 6. How many instances
Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)

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
- Public class attribute `number_of_instances`:
    * Initialized to `0`
    * Incremented during each new instance instantiation
    * Decremented during each instance deletion
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    * if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
```
### 7. Change representation
Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

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
- Public class attribute `number_of_instances`:
    * Initialized to `0`
    * Incremented during each new instance instantiation
    * Decremented during each instance deletion
- Public class attribute `print_symbol`:
    * Initialized to `#`
    * Used as symbol for string representation
    * Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` print the rectangle with the character(s) stored in `print_symbol`: 
    * if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
```
### 8. Compare rectangles
Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

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
- Public class attribute `number_of_instances`:
    * Initialized to `0`
    * Incremented during each new instance instantiation
    * Decremented during each instance deletion
- Public class attribute `print_symbol`:
    * Initialized to `#`
    * Used as symbol for string representation
    * Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    * if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` print the rectangle with the character(s) stored in `print_symbol`: 
    * if `width` or `height` is equal to `0`, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    * `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
    * `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
    * Returns `rect_1` if both have the same area value
- You are not allowed to import any module
```bash
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
```
### 

## Resources
- [Object Oriented Programming (Read everything until the paragraph “Inheritance” (excluded))](https://python.swaroopch.com/oop.html)
- [Object-Oriented Programming (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)](https://python-course.eu/oop/object-oriented-programming.php)
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- [Properties vs. Getters and Setters (Mainly the last part “Public instead of Private Attributes”)](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)