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

### 5. An Integer
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print `“Not a number”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`
```bash
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$ 
```

### 6. Loop to languages
Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

- The first line: `“C is fun”`
- The second line: `“Python is cool”`
- The third line: `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop (`while`, `for`, etc.)
```bash
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
```
### 7. I love C
Write a script that prints `x` times `“C is fun”`

- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print `“Missing number of occurrences”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (`while`, `for`, etc.)
```bash
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
```
### 8. Square
Write a script that prints a square

- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print `“Missing size”`
- You must use the character `X` to print the square
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop (`while`, `for`, etc.)
```bash
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
```

### 9. Add
Write a script that prints the addition of 2 integers

- The first argument is the first integer
- The second argument is the second integer
- You have to define a function with this prototype: `function add(a, b)`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
```bash
guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
```

### 10. Factorial
Write a script that computes and prints a factorial

- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- You must do it recursively
- You must use a function
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
```bash
guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
```

### 11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer
- If no argument passed, print `0`
- If the number of arguments is `1`, print `0`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
```bash
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
```

### 12. Object
Update this script to replace the value `12` with `89`:

- You are not allowed to use `var`
```bash
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$ 
```

### 13. Add file
Write a function that returns the addition of 2 integers.

- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`

**Tip**
```bash
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
```
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