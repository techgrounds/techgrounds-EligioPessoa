# Data types and comments
Data types in Python refer to the different kinds of values that can be stored and manipulated in a program. Examples of data types include numbers (integers, floating-point numbers), strings (text), booleans (True or False), lists (ordered collections), and more. Each data type has its own characteristics and operations that can be performed on it.

Comments in Python are lines of text that are ignored by the Python interpreter when executing the code. They are used to add explanations or notes within the code to make it more readable and understandable for humans. Comments are useful for documenting code, providing context, or disabling specific lines temporarily. They are denoted by the # symbol and can be placed on a line by itself or at the end of a line of code.

## Key-terms

- **concatenate**: Concatenation refers to combining or joining strings together. The concatenate command allows you to merge multiple strings into a single string. This can be done using the + operator, which combines the contents of two or more strings and produces a new string that includes all the combined text.
- **boolean**: Booleans in Python are a data type that represents two values: True and False. Booleans are used to express logical conditions and are often used in decision-making and control flow structures like conditional statements and loops. They help determine the flow of a program based on whether a condition is true or false, enabling you to create dynamic and responsive code.
- **string**: A string is a sequence of characters enclosed in quotation marks (either single quotes or double quotes). Strings are used to represent and manipulate text-based data, such as words, sentences, or even entire paragraphs. You can perform various operations on strings, including concatenation (combining strings), slicing (extracting parts of strings), and accessing individual characters within a string.
- **integer**: An integer is a whole number without any fractional or decimal parts. It represents whole quantities or counts in programming. Integers can be positive, negative, or zero, and they can be used in mathematical calculations and various operations within a Python program.
- **float**: A float is a data type that represents numbers with decimal points. It is used to handle and manipulate real numbers, including both whole numbers and fractional values. Floats allow for more precise calculations and are commonly used when dealing with measurements, scientific calculations, or any situation that requires fractional or decimal values.


## Opdracht
### Gebruikte bronnen

ChatGPT: python: how do i concatenate type() within a printed string?

https://www.simplilearn.com/tutorials/python-tutorial/python-typeof-function

https://www.w3schools.com/python/ref_func_input.asp

https://stackoverflow.com/questions/36452105/python-user-input-data-type

https://stackoverflow.com/questions/57544817/how-to-break-text-into-paragraphs-python

### Ervaren problemen

Ik moest achterkomen hoe ik de functie `type()` kon _ concatenaten_ in een _string_ . ChatGPT heeft me daarin geholpen.

### Resultaat

### Exercise 1:

```
# Copy code into script

a = 'int'
b = 7
c = False
d = "18.5"

# Determine the data types of all four variables (a, b, c, d) using a built in function.

print("a is a "+ str(type(a)))
print("b is a "+ str(type(b)))
print("c is a "+ str(type(c)))
print("d is a "+ str(type(d)))

# Make a new variable x and give it the value b + d. If you print the value of x, this will raise an error. Fix it so that print(x) prints a float.

d=18.5
x=b+d

# Print the value of x. 

print("corrected d is a "+ str(type(d)))

print(x)

```

![prg03ex1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg03ex1.png)

### Exercise 2:

```

# Use the input() function to get input from the user. Store that input in a variable.

print("Enter a value:")
x=input()

# Find out what data type the output of input() is. See if it is different for different kinds of input (numbers, words, etc.).

print(x,"is a",str(type(x)))

print("Every value inserted will be a string, because that's what the type() function converts values into.\nTo modify the script in order to get the right value type would require coding beyond the scope of this exercise.")

```


![prg03ex2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg03ex2.png)
