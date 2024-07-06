# 0x09. Python - Everything is object
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Tasks
### 0. Who am I?
What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.
### 1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.
### 2. Right count
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```bash
>>> a = 89
>>> b = 100
```
### 3. Right count =
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```bash
>>> a = 89
>>> b = 89
```
### 4. Right count =
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```bash
>>> a = 89
>>> b = a
```
### 5. Right count =+
In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.
```bash
>>> a = 89
>>> b = a + 1
```
### 6. Is equal
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
### 7. Is the same
What do these 3 lines print?
```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
### 8. Is really equal
What do these 3 lines print?
```bash
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
### 9. Is really the same
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
### 10. And with a list, is it equal
What do these 3 lines print?
```bash
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
### 11. And with a list, is it the same
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
### 12. And with a list, is it really equal
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
### 13. And with a list, is it really the same
What do these 3 lines print?
```bash
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
### 14. List append
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
### 15. List add
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
### 16. Integer incrementation
What does this script print?
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
### 17. List incrementation
What does this script print?
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
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


## Resources
- [9.10. Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation (Only this chapter)](https://www.composingprograms.com/pages/24-mutable-data.html)
- [9.12. Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

