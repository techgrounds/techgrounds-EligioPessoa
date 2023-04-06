# Cron jobs

Cron is een Linux taakplanner die gebruikt wordt om taken klaar te zetten zodat ze periodiek op een vaste datum of interval plaatsvinden. Cron jobs zijn specifieke commands of shell scripts die door gebruikers gedefinieërd worden in de crontab bestanden. Deze worden dan gemonitort door de Cron daemon en taken worden toegepast op een vooraf ingestelde schema.


## Key-terms

SHELL/MAILTO/PATH - Hoewel deze drie componenten niet strict noodzakelijk zijn om een crontab uit te laten voeren, ze kunnen helpvol zijn.

- De SHELL specifieërt het command of script die uitgevoerd dient te worden.
- De MAILTO is goed voor troubleshooting en monitor doeleinden. Het verstuurt de output van de crontab naar een bepaalde e-mail adres.
- De PATH zorgt ervoor dat de command of script die uitgevoerd wordt kan worden evonden en uitgevoerd.



## Opdracht
### Gebruikte bronnen

ChatGPT query: is shell mailto path really necessary in crontab?

[Display date and time](https://www.cyberciti.biz/faq/linux-display-date-and-time/)

[How to use cron Linux](https://opensource.com/article/17/11/how-use-cron-linux)

[Troubleshooting cron](https://www.cyberithub.com/solved-errors-in-crontab-file-cant-install/)

[Crontab generator](https://crontab-generator.org/)

[How to check disk space](https://www.linuxfoundation.org/blog/blog/classic-sysadmin-how-to-check-disk-space-on-linux-from-the-command-line)


### Ervaren problemen

Ik had nog moeite om te begrijpen dat als ik een output per minuut wil hebben uit de cronjob, dan moet het minuut veld ook op * zitten i.p.v. 1
Ik kon de geen output krijgen uit de crontab, tot ik de command bash wist te zetten in de cron tab

### Resultaat

### Create a Bash script that writes the current date and time to a file in your home directory.

Script time.sh gecreërd
```
#!/bin/bash

date +"%d-%m-%y %T" > $HOME/time.txt
```
![time](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/LNX08-time.png)


### Register the script in your crontab so that it runs every minute.

```
crontab -e

SHELL=/bin/bash
MAILTO=""
PATH=/home/eligio/scripts:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

* * * * * bash $HOME/scripts/time.sh
```

### Create a script that writes available disk space to a log file in ‘/var/logs’.

Script diskspace.sh gecreërd
```
#!/bin/bash


df -H --output=source,size,avail > /var/log/diskspace.log
```

![disk](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/LNX08-disk.png)

### Use a cron job so that it runs weekly.
```
0 9 * * 4 sudo bash $HOME/scripts/diskspace.sh
```
toegevoegd aan eerder aangemaakte cronjob


