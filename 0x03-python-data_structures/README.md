# 0x03-python-data_structures
Concepts learnt:
- Why Python programming is awesome
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it
## Tasks
### 0. Print a list of integers
Write a function that prints all integers of a list.

- Prototype: `def print_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
```bash
guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```
### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.
- Prototype: `def element_at(my_list, idx):`
- If `idx` is negative, the function should return `None`
- If `idx` is out of range (> of number of element in my_list), the function should return `None`
- You are not allowed to import any module
- You are not allowed to use try/except
```bash
guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```
### 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).

- Prototype: `def replace_in_list(my_list, idx, element):`
- If `idx` is negative, the function should not modify anything, and returns the original list
- If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use `try/except`
```bash
guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```
### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.

- Prototype: `def print_reversed_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
```bash
guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```
### 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
- Prototype: `def new_in_list(my_list, idx, element):`
- If `idx` is negative, the function should return a copy of the original list
- If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original list
- You are not allowed to import any module
- You are not allowed to use `try/except`
```bash
guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```
### 5. Can you C me now?
Write a function that removes all characters `c` and `C` from a string.

- Prototype: `def no_c(my_string):`
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use `str.replace()`
```bash
guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```
### 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.

- Prototype: `def print_matrix_integer(matrix=[[]]):`
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
```bash
guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```
### 7. Tuples addition
Write a function that adds 2 tuples.

- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
- The first element should be the addition of the first element of each argument
- The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers
```bash
guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```
### 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.

- Prototype: `def multiple_returns(sentence):`
- If the `sentence` is empty, the first character should be equal to `None`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$ 
```
### 9. Find the max
Write a function that finds the biggest integer of a list.

- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, return `None`
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin `max()`
```bash
guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 
```
### 10. Only by 2
Write a function that finds all multiples of 2 in a list.
- Prototype: `def divisible_by_2(my_list=[]):`
- Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 
```
### 11. Delete at
Write a function that deletes the item at a specific position in a list.

- Prototype: `def delete_at(my_list=[], idx=0):`
- If `idx` is negative or out of range, nothing change (returns the same list)
- You are not allowed to use `pop()`
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
### 
### 

## Resources
- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures (until 5.3. Tuples and Sequences included)](https://docs.python.org/3/tutorial/datastructures.html)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)