# 0x05. Python - Exceptions
Concepts learnt:
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

## Tasks
### 0. Safe list printing
Write a function that prints `x` elements of a list.

- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- Returns the real number of elements printed
- You have to use `try: / except`:
- You are not allowed to import any module
- You are not allowed to use `len()`
```bash
guillaume@ubuntu:~/0x05$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
guillaume@ubuntu:~/0x05$ 
```
### 1. Safe printing of an integers list
Write a function that prints an integer with `"{:d}".format()`.

- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if value has been correctly printed (it means the value is an integer)
- Otherwise, returns `False`
- You have to use `try: / except`:
- You have to use `"{:d}".format()` to print as integer
- You are not allowed to import any module
- You are not allowed to use `type()`
```bash
guillaume@ubuntu:~/0x05$ ./1-main.py
89
-89
School is not an integer
guillaume@ubuntu:~/0x05$
``` 
### 2. Print and count integers
Write a function that prints the first `x` elements of a list and only integers.

- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- `x` represents the number of elements to access in my_list
- `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print an integer
- You are not allowed to import any module
- You are not allowed to use `len()`
```bash
guillaume@ubuntu:~/0x05$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
guillaume@ubuntu:~/0x05$ 
```
### 3. Integers division with debug
Write a function that divides 2 integers and prints the result.

- Prototype: `def safe_print_division(a, b):`
- You can assume that `a` and `b` are integers
- The result of the division should print on the `finally:` section preceded by `Inside result:`
- Returns the value of the division, otherwise: `None`
- You have to use `try: / except: / finally:`
- You have to use `"{}".format()` to print the result
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x05$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
guillaume@ubuntu:~/0x05$ 
```
### 
### 
### 
### 
## Resources
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling (starting at minute 7)](https://www.youtube.com/watch?v=7vbgD-3s-w4)
