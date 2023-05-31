# Mini project Python


## Key-terms


## Opdracht
### Gebruikte bronnen

https://flexiple.com/python/python-list-contains/

https://blog.finxter.com/python-typeerror-set-object-is-not-subscriptable/

https://www.w3schools.com/python/ref_random_choice.asp

https://python-reference.readthedocs.io/en/latest/docs/operators/addition_assignment.html

https://www.digitalocean.com/community/tutorials/python-concatenate-string-and-int

https://stackoverflow.com/questions/27802270/how-to-stop-a-function


### Ervaren problemen



### Resultaat

```

# The player plays against a computer opponent typing either a letter (rps) or an entire word (rock paper scissors) to play their move.

print("Let's play ROCK, PAPER, SCISSORS!!!\n\nChoose your first move (rock, paper or scissors):")

options=['rock','paper','scissors']

game1=input()

def inputrps():
    global game1
    game1=input()
    checkgame()

# Create a function that checks whether the move is valid or not.

def checkgame():
    if game1 in options:
        return
    else:
        print("Wrong input, try again!")
        inputrps()

checkgame()


# Create another function to create a computer move.

import random

def inputpc():
    global pcgame1
    pcgame1=random.choice(options)
    print("Computer has chosen "+pcgame1)

inputpc()


# Create a function that keeps track of the score.

plwin=0
pcwin=0

def playerwins():
    global plwin
    plwin+=1
    print("You: "+f'{plwin}'+", PC: "+f'{pcwin}')

def pcwins():
    global pcwin
    pcwin+=1
    print("You: "+f'{plwin}'+", PC: "+f'{pcwin}')


# The game should be played in a predetermined number of rounds.
# Create another function to check who wins the round.
import sys

def gameover():
    if plwin==2:
        #print("The game is over!")
        sys.exit("The game is over!")
    elif pcwin==2:
        #print("The game is over!")
        sys.exit("The game is over!")
    else:
        return



def playing():
    if game1==pcgame1:
        print("It's a draw!")
        print("Play again! Choose your next move (rock, paper or scissors):")
        inputrps()
        inputpc()
        playing()               
    elif game1==options[0]:
        if pcgame1==options[2]:
                print("You win!")
                playerwins()
                gameover()
                print("Play again! Choose your next move (rock, paper or scissors):")
                inputrps()
                inputpc()
                playing()                
        elif pcgame1==options[1]:
            print("You lose!")
            pcwins()
            gameover()
            print("Play again! Choose your next move (rock, paper or scissors):")
            inputrps()
            inputpc()
            playing()            
    elif game1==options[2]:
        if pcgame1==options[0]:
            print("You lose!")
            pcwins()
            gameover()
            print("Play again! Choose your next move (rock, paper or scissors):")
            inputrps()
            inputpc()
            playing()            
        elif pcgame1==options[1]:
            print("You win!")
            playerwins()
            gameover()
            print("Play again! Choose your next move (rock, paper or scissors):")
            inputrps()
            inputpc()
            playing()
    elif game1==options[1]:
        if pcgame1==options[0]:
            print("You win!")
            playerwins()
            gameover()
            print("Play again! Choose your next move (rock, paper or scissors):")
            inputrps()
            inputpc()
            playing()
        elif pcgame1==options[2]:
            print("You lose!")
            pcwins()
            gameover()
            print("Play again! Choose your next move (rock, paper or scissors):")
            inputrps()
            inputpc()
            playing() 

playing()

```

![prg09](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/prg09.png)
