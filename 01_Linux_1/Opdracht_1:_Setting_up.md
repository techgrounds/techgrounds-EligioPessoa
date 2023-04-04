# Linux

Linux is een open source bestuursysteem. Het wordt vaak gebruikt met servers omdat het stabiel, licht, aanpasbaar en gratis is. Linux wordt meestal met een Command Line Interface gebruikt, en de Graphical User Interface wordt beschouwd als optioneel. Dit maakt het ook stabiel.

## Key-terms

Virtual Machine (VM)- Een VM is een computer resource die software gebruikt om een fisieke computer te emuleren, om programma's en apps te runnen. Elke VM heeft zijn eigen bestuursysteem en werkt onafhankelijk van andere VMs, al zitten ze op dezelfde host

## Opdracht
### Gebruikte bronnen

[VMWare website](https://www.vmware.com/topics/glossary/content/virtual-machine.html)

[Microsoft Documentatie](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)

### Ervaren problemen

Na het volgen van de beschreven stappen in de link, kon ik niet inloggen. Dat kwam omdat ik nog de poort in moest voegen. Na uitzoeken met mijn collega's zijn we op de juiste sysntax gekomen.

### Resultaat

Het is mij gelukt om met OpenSSH in de Linux VM in te loggen, via de code:

```

ssh -i ..\Nest-El-Pessoa.pem eligio@18.157.179.30 -p 52203

```


![LinuxVM Screenshot](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/3248526e59862b52ed01a1f6987d2cdd9fa6c1b7/00_includes/LNX-01SettingUp.PNG)
