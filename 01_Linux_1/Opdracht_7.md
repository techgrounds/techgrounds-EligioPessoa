# Bash scripting

Een Bash script is een series van commands die geschreven zijn in een tekstbestand. Je kunt meerdere commands in een rij uitvoeren door de script uit te voeren.
De command line interface in Linux heet de Bash shell




## Key-terms

bashrc bestand - Een script bestand die uitgevoerd wordt als een gebruiker inlogt. Het bestand zelf bevat een serie configuraties voor de terminal sessie.

shebang - Een sequëntie van de karakters #! aan het begin van een script, vervolgd door een path die wijst welke Bash (of Python) interpreter gebruikt moet worden om een uitvoerbare bestand te interpreteren.

variable - Een variable is een tekst "string" waar een waarde aan wordt toegewezen. Die waarde kan een nummer, tekst, bestand, of andere soort data zijn. Een variable is een verwijzer naar de daadwerkelijke data. 


## Opdracht
### Gebruikte bronnen

[Creating scripts](https://www.guru99.com/introduction-to-shell-scripting.html)

[Append line to file](https://linuxhint.com/bash_append_line_to_file/)

[Install httpd Ubuntu](https://www.javatpoint.com/install-httpd-ubuntu)

[httpd vs apache2](https://www.linuxquestions.org/questions/linux-newbie-8/unit-httpd-service-could-not-be-found-4175662430/)

[Ubuntu Apache documentatie](https://ubuntu.com/server/docs/web-servers-apache)

[system start vs system enable](https://askubuntu.com/questions/733469/what-is-the-difference-between-systemctl-start-and-systemctl-enable)

[Generate a random number in bash](https://linuxhint.com/generate-random-number-bash/)

### Ervaren problemen

Ik kreeg “Unary operator expected” error omdat ik aan het einde van de "shebang" sh zette i.p.v. bash. Verder moest ik een paar keer de variabels checken omdat ze niet met elkaar overeenkwamen

Er was verwarring over het feite dat httpd wordt inbegrepen in de apache proces. Verder onderzoek verhelderde dit.

Ik probeerde de variable te definieren en kreeg een error bericht; later kwam ik achter dat de variable met $ getoond moet worden. Na veel trial en error aan de oplossing gekomen.


### Resultaat


### Add the scripts directory to the PATH variable.

Code
```
nano ~/.bashrc
```
uitgevoerd, vervolgens 
```
export PATH="$HOME/scripts:$PATH"
```
in de bashrc bestand.

![PATH](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/LNX07-PATH.png)

### Create a script that appends a line of text to a text file whenever it is executed.
```
mkdir $HOME/scripts
```
uigevoerd. Vervolgens, bestand apptxt.sh gecreërd, met code
```
#! /bin/bash

file="$HOME/linux07.txt"

echo "Type some text to append: "
read text

if [ "$text" != "" ]; then
 echo $text >> $file
fi
```
### Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

Bestand httpd.sh gecreërd, waarin
```
#!/bin/bash

# Update and Install

sudo apt update
sudo apt install apache2
sudo ufw allow Apache

# Starting and Enabling

sudo systemctl start apache2
sudo systemctl enable apache2

# Check status

systemctl status apache2
```
![Uitvoering 1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/LNX07-uitvoering1.png)

![Uitvoering 2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/LNX07-uitvoering2.png)


### Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.

Code in bestand rnbr.sh:
```
#!/bin/bash

# Generate number between 1 and 10 and store it in variable

random="echo $(($RANDOM%10+1))"

# Append number to text file

$random >> $HOME/rnmbr.txt
```
![random](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/LNX07-script.png)
