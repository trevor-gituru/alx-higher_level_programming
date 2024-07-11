# 0x07. Python - Test-driven development
Concepts learnt:
- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Tasks
### 0. Integers addition
Write a function that adds 2 integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$ 
```
### 
### 
### 
### 
### 
## Resources
- [doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)](https://docs.python.org/3.4/library/doctest.html#doctest.NORMALIZE_WHITESPACE)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
- [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
- [Interactive and Non-interactive tests]()
