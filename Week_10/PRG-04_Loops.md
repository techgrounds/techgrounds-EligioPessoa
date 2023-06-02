# Loops

Loops are used to repeat a set of instructions multiple times. They allow you to automate repetitive tasks and iterate over collections of data. There are two main types of loops: for loops, which iterate over a sequence of items, and while loops, which continue executing as long as a certain condition remains true. By using loops, you can perform actions repeatedly without the need to write the same code over and over again.

## Key-terms

- **'for' loops**: a for loop is used to iterate over a sequence of items, such as a list, string, or range of numbers. It allows you to perform a set of instructions for each item in the sequence. You can think of a for loop as a way to go through each item, one by one, and execute a block of code for each item. This makes it convenient for tasks like accessing each element in a list, processing characters in a string, or performing a specific action a certain number of times.
- **'while' loops**: a type of loop that continues executing a block of code as long as a specific condition remains true. It repeatedly checks the condition before each iteration and stops when the condition becomes false. This allows you to perform actions repeatedly until a desired outcome or condition is met.

## Opdracht
### Gebruikte bronnen

https://www.w3schools.com/python/python_while_loops.asp

https://www.w3schools.com/python/python_for_loops.asp

https://discovery.cs.illinois.edu/learn/Simulation-and-Distributions/For-Loops-in-Python/

### Ervaren problemen

Geen problemen ervaren.

### Resultaat

### Exercise 1:

```

# Create a variable x and give it the value 0.

x=0

# Use a while loop to print the value of x in every iteration of the loop. After printing, the value of x should increase by 1. The loop should run as long as x is smaller than or equal to 10.

while x<=10:
    print(x)
    x+=1

```

![prg04ex1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex1.png)

### Exercise 2:

```

# Add a variable x with value 5 at the top of your script.

x=5

# Paste code in script. Print the value of i in the for loop. You did not manually assign a value to i. Figure out how its value is determined.

for i in range(10):
	print(i)

print("The value of i is determined by the type of sequence. In this case, it's an an iterable sequence")

# Using the for loop, print the value of x multiplied by the value of i, for up to 50 iterations.

for i in range(50):
	print(x*i)

```

![prg04ex2a](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex2a.png)

![prg04ex2b1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex2b1.png) ![prg04ex2b2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex2b2.png) ![prg04ex2b3](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex2b3.png) ![prg04ex2b4](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex2b4.png) ![prg04ex2b5](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex2b5.png)


### Exercise 3:

![prg04ex3](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg04ex3.png)
