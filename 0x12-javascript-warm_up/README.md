# 0x12. JavaScript - Warm up
## Background Context
JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

- Scripting (same as we did with Python)
- Web front-end
For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

![js](/images/0_12_1)

## Concepts learnt
- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- What are differences between `var`, `const` and `let`
- What are all the data types available in JavaScript
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use `while` and `for` loops
- How to use `break` and `continue` statements
- What is a function and how do you use functions
- What does a function that does not use any `return` statement return
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`

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
### 0. First constant, first print
Write a script that prints `“JavaScript is amazing”`:

- You must create a constant variable called `myVar` with the value `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
```bash
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
```

### 1. 3 languages
Write a script that prints 3 lines:

- The first line: `“C is fun”`
- The second line: `“Python is cool”`
- The third line: `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
```bash
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
```

### 2. Arguments
Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print `“No argument”`
- If only one argument is passed to the script, print `“Argument found”`
- Otherwise, print `“Arguments found”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

Reference: [process.argv]()
```bash
guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
```

### 3. Value of my argument
Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print `“No argument”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`
```bash
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
```

### 4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: `“ is ”`

- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
```bash
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
```

### 
### 
### 
### 
### 
### 
### 
### 
## Resources
- [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Operator precedeence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
-[Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions#function_scope_and_conflicts)
 - [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
 - [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
 - [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
 - [ModernJs](https://github.com/mbeaudru/modern-js-cheatsheet?tab=readme-ov-file#async-await)
- [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/)