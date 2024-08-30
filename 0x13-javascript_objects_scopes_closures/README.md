# JavaScript - Objects, Scopes and Closures
## Concepts learnt
- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What `this` means
- What `undefined` means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`

## More Info
### Install Node 14
```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
### Install semi-standard
Documentation
```bash
$ sudo npm install semistandard --global
```
## Tasks
### 0. Rectangle #0
Write an empty class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
```bash
guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
```
### 1. Rectangle #1
Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
```bash
guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$ 
```
### 2. Rectangle #2
Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to `0` or not a positive integer, create an empty object
```bash
guillaume@ubuntu:~/0x13$ cat 2-main.js
guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$ 
``` 
### 3. Rectangle #3
Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to `0` or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`
```bash
guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXXguillaume@ubuntu:~/0x13$ 
```
### 
### 
### 
### 
### 
### 
### 
## Resources
- [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
- [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_programming)(**(read all examples!)**)
- [Class - ES6](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [super](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
- [extends](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
- [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures#emulating_private_methods_with_closures)
- [this/self](https://alistapart.com/article/getoutbindingsituations/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)