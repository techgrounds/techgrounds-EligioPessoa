# Key-value pairs

A key-value pair is a way of organizing and storing data in a dictionary, which is a collection of unordered elements. Each key-value pair consists of a key and its associated value, separated by a colon (:) and enclosed in curly braces {}.

The key serves as a unique identifier or label, while the value represents the corresponding data associated with that key. The key-value pairs within a dictionary allow you to access and retrieve values based on their respective keys.

For example, in the dictionary my_dict = {'name': 'John', 'age': 25}, 'name' and 'age' are the keys, while 'John' and 25 are the corresponding values. By using the keys, you can retrieve the associated values using my_dict['name'] or my_dict['age'].



## Key-terms

**dictionary**: a `dictionary` is an unordered collection of _key/value pairs_ enclosed in curly braces {}. Each key in a dictionary is unique and associated with a corresponding value. Dictionaries are used to store and retrieve data based on their keys rather than their position, making them convenient for organizing and accessing data in a flexible manner. You can add, modify, or delete key/value pairs in a dictionary, and you can retrieve the value associated with a specific key. Dictionaries are commonly used when you need to store and access data in a way that is easy to look up and update based on a unique identifier (the key).

## Opdracht
### Gebruikte bronnen

https://www.w3schools.com/python/python_dictionaries.asp

https://www.pythontutorial.net/python-basics/python-dictionary/

https://www.digitalocean.com/community/tutorials/python-add-to-dictionary

https://adamtheautomator.com/read-csv-in-python/

https://www.geeksforgeeks.org/python-concatenate-dictionary-string-values/

https://www.geeksforgeeks.org/how-to-add-values-to-dictionary-in-python/

https://www.geeksforgeeks.org/python-append-multitype-values-in-dictionary/



### Ervaren problemen

Bij oefening 2 wist ik niet hoe ik _values_ moest toevoegen aan de _key/value_ pair. Onderzoek heeft getoond dat met _string values_ moet ik _concatenate_ gebruiken. Later bleek het dat de _concatenate_ methode toch niet geschikt was voor de aanpak die ik koos.

Bij oefening 2 kon ik de _key_ niet toevoegen aan de csv bestand vanuit de script, dus ik heb het voorlopig zelf in de csv bestand ingevuld.

### Resultaat

### Exercise 1:

```

# Create a dictionary

Casper={
    ' First name':' Casper',
    ' Last name':' Velzen',
    ' Job title':' Learning coach',
    ' Company':' Techgrounds'
}

# Loop over the dictionary and print every key-value pair in the terminal.

for a,b in Casper.items():
    print(f"{a}:{b}")

```
![prg08ex1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg08ex1.png)



### Exercise 2:

```

# Use user input to ask for their information (first name, last name, job title, company). Store the information in a dictionary.

user={}

print("Enter your first name:")
user['First name']=' '+input()

print("Enter your last name:")
user['Last name']=' '+input()

print("Enter your job title:")
user['Job title']=' '+input()

print("Enter the company you work for:")
user['Company']=' '+input()



for x,y in user.items():
    print(f"{x},{y}")


# Write the information to a csv file (comma-separated values). The data should not be overwritten when you run the script multiple times.
import csv

key_names=['First name','Last name','Job title','Company']

with open('ex2.csv',mode='a') as csv_file:
    appendedcontent=csv.DictWriter(csv_file, fieldnames=key_names)

    appendedcontent.writerow(user)

with open('ex2.csv', mode='r') as csv_file:
    readingfile=csv.DictReader(csv_file)

    for items in readingfile:
        print(items)

```

![prg08ex2a](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg08ex2a.png)
![prg08ex2b](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg08ex2b.png)
![prg08ex2c](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg08ex2c.png)
![prg08ex2d](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg08ex2d.png)
