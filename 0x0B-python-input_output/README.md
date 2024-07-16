# 0x0B. Python - Input/Output
Concepts learnt:
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Tasks
### 0. Read file
Write a function that reads a text file (`UTF8`) and prints it to stdout:

- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x0B$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!guillaume@ubuntu:~/0x0B$
``` 
**No test cases needed**
### 1. Write to a file
Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x0B$ ./1-main.py
29
guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$ 
```
**No test cases needed**
### 2. Append to a file
Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created
- You must use the `with` statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x0B$ cat file_append.txt
cat: file_append.txt: No such file or directory
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
This School is so cool!
guillaume@ubuntu:~/0x0B$ ./2-main.py
29
guillaume@ubuntu:~/0x0B$ cat file_append.txt
This School is so cool!
This School is so cool!
guillaume@ubuntu:~/0x0B$ 
```
**No test cases needed**
### 3. To JSON string
Write a function that returns the JSON representation of an object (string):

- Prototype: `def to_json_string(my_obj):`
- You don’t need to manage exceptions if the object can’t be serialized.
```bash
guillaume@ubuntu:~/0x0B$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/0x0B$
```
**No test cases needed**
### 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a `JSON` string:

- Prototype: `def from_json_string(my_str):`
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
```bash
guillaume@ubuntu:~/0x0B$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
guillaume@ubuntu:~/0x0B$ 
```
**No test cases needed**
### 5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:

- Prototype: `def save_to_json_file(my_obj, filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.
```bash
guillaume@ubuntu:~/0x0B$ ./5-main.py
[TypeError] {3, 132} is not JSON serializable
guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/0x0B$ cat my_set.json ; echo ""

guillaume@ubuntu:~/0x0B$ 
```
**No test cases needed**
### 6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:

- Prototype: `def load_from_json_file(filename):`
- You must use the `with` statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.
```bash
guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
[1, 2, 3]
guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
guillaume@ubuntu:~/0x0B$ cat my_fake.json ; echo ""
{"is_active": true, 12 }
guillaume@ubuntu:~/0x0B$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
guillaume@ubuntu:~/0x0B$
``` 
**No test cases needed**
### 7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
- The list must be saved as a JSON representation in a file named `add_item.json`
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.
```bash
guillaume@ubuntu:~/0x0B$ cat add_item.json
cat: add_item.json: No such file or directory
guillaume@ubuntu:~/0x0B$ ./7-add_item.py
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
[]
guillaume@ubuntu:~/0x0B$ ./7-add_item.py Best School
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
["Best", "School"]
guillaume@ubuntu:~/0x0B$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
guillaume@ubuntu:~/0x0B$
``` 
**No test cases needed**
### 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x0B$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
guillaume@ubuntu:~/0x0B$ 
guillaume@ubuntu:~/0x0B$ cat 8-my_class_2.py 
guillaume@ubuntu:~/0x0B$ cat 8-main_2.py 
guillaume@ubuntu:~/0x0B$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
guillaume@ubuntu:~/0x0B$
```
**No test cases needed**

### 
### 
### 
### 
## Resources
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html#json-to-py-table)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/)
- [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)
