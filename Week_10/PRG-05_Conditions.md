# PRG-05 Conditions
Conditions are used to make decisions in your code based on certain criteria. Conditions are typically expressed using comparison operators such as == (equal to), != (not equal to), < (less than), > (greater than), <= (less than or equal to), and >= (greater than or equal to).

By using conditions, you can specify different paths or actions to take based on whether a certain condition is true or false. For example, you can use an if statement to execute a block of code only if a particular condition evaluates to true, or you can use if-else statements to choose between two different blocks of code based on a condition. Conditions allow you to control the flow of your program and make it responsive to different situations.

## Key-terms

- **if statement**: the `if` statement is used to execute a block of code only if a specific condition is true. It is a way to check whether a condition is met; and if it is, the code inside the if block is executed. If the condition is not true, the code inside the if block is skipped, and the program continues to the next section of code.
- **elif statement**: the `elif` statement is short for "else if", and is used as a _conditional statement_ in conjunction with an `if` statement. It allows you to specify additional conditions to check if the initial `if` condition is not met. When an `if` condition is evaluated to `False`, the program moves to the `elif` statement and checks its _condition_. If the `elif` condition is `True`, the corresponding block of code associated with that condition is executed. If the `elif` condition is also `False`, the program can continue to check subsequent `elif` statements or proceed to the `else` statement if it exists. The `elif` statement is useful when you have multiple _conditions_ to check, and you want to provide different actions or outcomes depending on which condition is met.
- **else statement**:  the `else` statement is used in conjunction with _conditional statements_ like `if` or `while`. It provides a block of code that is executed when the condition of the preceding `if` or `while` statement evaluates to `False` or becomes `False` during the execution of a loop. You can think of the `else` statement as an alternative branch of code that is executed when the condition of the preceding statement is not met. It allows you to specify what should happen if the condition is `False` or the loop completes without encountering a _break statement_.

## Opdracht
### Gebruikte bronnen

https://www.w3schools.com/python/gloss_python_if_statement.asp

https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/

https://www.w3schools.com/python/python_while_loops.asp

https://www.w3schools.com/python/gloss_python_elif.asp



### Ervaren problemen

Mijn script stopte na de tweede maal dat ik een waarde inputte. Het toevoegen van de `while` command lostte dit op.

### Resultaat

### Exercise 1:

```

# Use the input() function to ask the user of your script for their name. If the name they input is your name, print a personalized welcome message. If not, print a different personalized message.

print("Enter your name:")
a=input()

b="Elígio"
if a == b:
    print("Welcome, Elígio!")
else:
    print(a+", please bring "+b+" here.")

```

![prg05ex1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg05ex1.png)

### Exercise 2:

```

# Ask the user of your script for a number. Give them a response based on whether the number is higher than, lower than, or equal to 100.
# Make the game repeat until the user inputs 100

print("Please enter a full number:")
a=int(input())

b=100

while a!=b:
    if a<b:
        print("That's too low!")
        print("Try again:")
        a=int(input())
    elif a>b:
        print("That's too high!!")
        print("Try again:")
        a=int(input())
else:
    print("You got the right number!!!")

```

![prg05ex2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg05ex2.png)
