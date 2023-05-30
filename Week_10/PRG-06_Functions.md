# PRG-06 Functions
A function is a named block of code that performs a specific task. It takes input values (known as arguments or parameters) and produces an output or performs an action. Functions are reusable and modular, allowing you to organize your code into smaller, manageable pieces.

Think of a function as a mini-program within your program. You define the function with a name, specify the input it expects, and write the code inside the function block to achieve a particular goal. By calling the function with the appropriate arguments, you can execute that block of code whenever needed, simplifying your program's structure and promoting code reuse.

## Key-terms

- **return statement**: the `return` statement is used to send a value back from a function. When a function encounters a return statement, it immediately stops executing and returns the specified value or expression to the caller of the function. In simpler terms, the return statement allows a function to provide a result or output that can be used by other parts of the program. It marks the end of the function's execution and passes the desired value back to where the function was called from.
- **package**: a package is a way of organizing and structuring related modules (Python files) into a hierarchical directory structure. A package is typically represented as a directory containing multiple Python modules and a special __init__.py file that indicates it as a package. Packages are used to organize and group related functionality together, making it easier to manage and reuse code. They provide a way to organize modules into a meaningful hierarchy, allowing for better organization, modularization, and encapsulation of code. Packages can be imported and used in other Python scripts to access the functionality contained within them.

## Opdracht
### Gebruikte bronnen

https://www.analyticssteps.com/blogs/working-random-numbers-python

https://www.w3schools.com/python/ref_random_randint.asp

https://www.w3schools.com/python/python_functions.asp

https://www.w3schools.com/python/gloss_python_function_arguments.asp

https://www.w3schools.com/python/ref_stat_mean.asp

https://realpython.com/python-return-statement/

### Ervaren problemen

Mijn code voor oefening 3 werkte niet, tot ik (via een ChatGPT query) achterkwam dat ik een _return statement_ moest toevoegen.

### Resultaat
### Exercise 1:

```

# Import the random package
import random as rand

# Print 5 random integers with a value between 0 and 100.

for a in range(5):
    randnum=rand.randint(0,100)
    print(randnum)

```

![prg06ex1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg06ex1.png)


### Exercise 2:

```

# Write a custom function myfunction() that prints “Hello, world!” to the terminal. Call myfunction.

def my_function():
    print("Hello, world!")

my_function()

# Rewrite your function so that it takes a string as an argument. Then, it should print “Hello, <string>!”.

print("Enter your name:")
name=input()

def my_function(name):
    print("Hello, "+name+"!")

my_function(name)

```

![prg06ex2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg06ex2.png)

### Exercise 3:

```

# Write the custom function avg() so that it returns the average of the given parameters. You are not allowed to edit any code below the second comment.

import statistics as stat

def avg(x,y):
	return stat.mean([x,y])


# you are not allowed to edit any code below here
x = 128
y = 255
z = avg(x,y)
print("The average of",x,"and",y,"is",z)

```

![prg06ex3](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg06ex3.png)
