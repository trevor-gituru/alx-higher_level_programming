# 0x0C. Python - Almost a circle
Concepts learnt:

## Tasks
### 
### 1. Base class
Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py`:

- Class `Base`:
    * private class attribute `__nb_objects = 0`
    * class constructor: `def __init__(self, id=None):`:
        + if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
        + otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
```
guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$
``` 
### 2. First Rectangle
Write the class `Rectangle` that inherits from `Base`:

- In the file `models/rectangle.py`
- Class `Rectangle` inherits from `Base`
- Private instance attributes, each with its own public getter and setter:
    * `__width -> width`
    * `__height -> height`
    * `__x -> x`
    * `__y -> y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
    *  Call the super class with `id` - this super call with use the logic of the `__init__` of the Base class
    *  Assign each argument `width`, `height`, `x` and `y` to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
```bash
guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$ 
```
### 3. Validate attributes
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):

- If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
- If `width` or `height` is under or equals `0`, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
- If `x` or `y` is under `0`, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`
```bash
guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
guillaume@ubuntu:~/$ 
```
### 4. Area first
Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.
```bash
guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$ 
```
### 5. Display #0
Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.
```bash
guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$ 
```
### 6. __str__
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
```bash
guillaume@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
guillaume@ubuntu:~/$ 
```
### 7. Display #1
Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`
```bash
guillaume@ubuntu:~/$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
guillaume@ubuntu:~/$ 
``` 
### 8. Update #0
Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:

- 1st argument should be the `id` attribute
- 2nd argument should be the `width` attribute
- 3rd argument should be the `height` attribute
- 4th argument should be the `x` attribute
- 5th argument should be the `y` attribute
This type of argument is called a “no-keyword argument” - Argument order is super important.
```bash
guillaume@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
guillaume@ubuntu:~/$ 
```
### 9. Update #1
Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:

- `**kwargs` can be thought of as a double pointer to a dictionary: key/value
    * As Python doesn’t have pointers, `**kwargs` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
- `**kwargs` must be skipped if `*args` exists and is not empty
- Each key in this dictionary represents an attribute to the instance
This type of argument is called a “key-worded argument”. Argument order is not important.
```bash
guillaume@ubuntu:~/$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
guillaume@ubuntu:~/$ 
```
### 10. And now, the Square!
Write the class `Square` that inherits from `Rectangle`:

- In the file `models/square.py`
- Class `Square` inherits from `Rectangle`
- Class constructor: `def __init__(self, size, x=0, y=0, id=None):`:
    * Call the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the Rectangle class. The `width` and `height` must be assigned to the value of `size`
    * You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height
    * All `width`, `height`, `x` and `y` validation must inherit from Rectangle - same behavior in case of wrong data
- The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in our case, `width` or `height`
As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.
```bash
guillaume@ubuntu:~/$ ./9-main.py
[Square] (1) 0/0 - 5
25
#####
#####
#####
#####
#####
---
[Square] (2) 2/0 - 2
4
  ##
  ##
---
[Square] (3) 1/3 - 3
9



 ###
 ###
 ###
guillaume@ubuntu:~/$ 
```
### 11. Square size
Update the class `Square` by adding the public getter and setter `size`

- The setter should assign (in this order) the `width` and the `height` - with the same value
- The setter should have the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from width)
```bash
guillaume@ubuntu:~/$ ./10-main.py
[Square] (1) 0/0 - 5
5
[Square] (1) 0/0 - 10
[TypeError] width must be an integer
guillaume@ubuntu:~/$ 
```
### 12. Square update
Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:

- `*args` is the list of arguments - no-keyworded arguments
    * 1st argument should be the `id` attribute
    * 2nd argument should be the `size` attribute
    * 3rd argument should be the `x` attribute
    * 4th argument should be the `y` attribute
- `**kwargs` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
- `**kwargs` must be skipped if `*args` exists and is not empty
- Each key in this dictionary represents an attribute to the instance
```bash
guillaume@ubuntu:~/$ ./11-main.py
[Square] (1) 0/0 - 5
[Square] (10) 0/0 - 5
[Square] (1) 0/0 - 2
[Square] (1) 3/0 - 2
[Square] (1) 3/4 - 2
[Square] (1) 12/4 - 2
[Square] (1) 12/1 - 7
[Square] (89) 12/1 - 7
guillaume@ubuntu:~/$ 
```
### 13. Rectangle instance to dictionary representation
Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Rectangle:

This dictionary must contain:

- `id`
- `width`
- `height`
- `x`
- `y`
```bash
guillaume@ubuntu:~/$ ./12-main.py
[Rectangle] (1) 1/9 - 10/2
{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
<class 'dict'>
[Rectangle] (2) 0/0 - 1/1
[Rectangle] (1) 1/9 - 10/2
False
guillaume@ubuntu:~/$ 
```
### 14. Square instance to dictionary representation
Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`:

This dictionary must contain:

- `id`
- `size`
- `x`
- `y`
```bash
guillaume@ubuntu:~/$ ./13-main.py
[Square] (1) 2/1 - 10
{'id': 1, 'x': 2, 'size': 10, 'y': 1}
<class 'dict'>
[Square] (2) 1/0 - 1
[Square] (1) 2/1 - 10
False
guillaume@ubuntu:~/$ 
```
### 
### 
### 
### 
### 
## Resources
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module]()
- [Python test cheatsheet]()
