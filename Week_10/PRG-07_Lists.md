# Lists
A list is an ordered collection of elements enclosed in square brackets []. Each element in a list is separated by a comma. Lists can contain elements of different data types, such as numbers, strings, or even other lists.

You can perform various operations on lists, including adding or removing elements, accessing specific elements by their index, and modifying the values of individual elements. Lists are mutable, which means you can change their contents after they are created. They are commonly used to store and manipulate a collection of related data or a sequence of values.

You can access individual elements by their index, where the index starts from 0 for the first element. Lists also support operations like concatenation (combining two lists) and slicing (extracting a portion of the list).

Lists are commonly used for storing and manipulating collections of data. They provide a convenient way to work with multiple values in a single variable, making it easier to perform tasks such as iterating over elements, sorting, filtering, and more.

## Key-terms

**index**: an `index` is a numeric value that represents the position of an element within a sequence, such as a `string` or a `list`. The `index` starts from 0 for the _first element_, 1 for the _second element_, and so on. By specifying an `index`, you can access or manipulate a specific element within the sequence.

For example, if you have a list my_list with elements [10, 20, 30], my_list[0] would access the first element (10), my_list[1] would access the second element (20), and so on. Indexing allows you to _retrieve, modify_, or _work_ with individual elements of a sequence based on their position within that sequence.

## Opdracht
### Gebruikte bronnen

https://www.w3schools.com/python/python_lists.asp

https://www.tutorialspoint.com/generating-random-number-list-in-python

https://bobbyhadz.com/blog/python-typeerror-cannot-unpack-non-iterable-int-object

https://sparkbyexamples.com/python/python-for-loop-increment/

https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/

https://realpython.com/python-modulo-operator/

### Ervaren problemen
Voor oefening 2, kreeg ik de error "TypeError: cannot unpack non-iterable int object". Ik merkte dat ik `enumerate` aan de functie moest toevoegen. Later merkte ik dat het toch niet werkt, en kwam achter dat de `length` van de lijst moet bijbetrokken worden.

### Resultaat

### Exercise 1:

```

# Create a variable that contains a list of five names.

list=["albert","bernard","cornelius","derick","eduard"]

# Loop over the list using a for loop. Print every individual name in the list on a new line.

for a in list:
    print(a)

```

![ex1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg07ex1.png)

### Exercise 2:

```

# Create a list of five integers.

import random
list=[]
for x in range(0,5):
    n=random.randint(1,100)
    list.append(n)
print(list)

# Use a for loop to do the following for every item in the list:
# Print the value of that item added to the value of the next item in the list. If it is the last item, add it to the value of the first item instead (since there is no next item).

length=len(list)



for a in range(length):
    b=list[a]
    c=list[(a+1)%length]
    d=b+c
    print(d)
```

![ex2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg07ex2.png)
