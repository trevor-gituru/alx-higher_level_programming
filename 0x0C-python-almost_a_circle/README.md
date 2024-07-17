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
### 
### 
### 
### 
### 
### 
### 
### 
### 
### 
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
