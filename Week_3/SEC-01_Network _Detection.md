# Network detection


## Key-terms

-**Nmap (Network Mapper)**: Een _open source tool_ die je in staat stelt om scans uit te voeren in zowel _lokale_ als _remote netwerken_. Nmap wordt gebruikt door netwerkbeheerders om _netwerkapparaten_ te inventariseren, de status van een _remote host_ te monitoren, enz. 

## Opdracht
### Gebruikte bronnen

https://www.redhat.com/sysadmin/quick-nmap-inventory

### Ervaren problemen

Geen problemen ervaren

### Resultaat

### Scan the network of your Linux machine using nmap. What do you find?

Na het vinden van de ip van mijn VM, heb ik de nmap command uitgevoerd op die IP. Daar krijg ik _latency_ te zien, de hoeveelheid ports die nog gesloten zijn, en de beschrijving van de ports die open zijn.

Verder heb ik nog de broadcast address en de server ip geprobeerd te scannen. Bij broadcast address was er geen aanvullende informatie te zien; bij de server IP kreeg ik informatie over ports te zien die niet horen bij de port lijst van mijn groep, wat wel interessant te merken was.

![Nmap1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC01ifconnmap.png)
![Nmap2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC01ifconnmap2.png)
![Nmap3](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC01ifconnmap3.png)

### Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser. (Tip: you will find that Zoom is constantly sending packets over the network. You can either turn off Zoom for a minute, or look for the packets sent by the browser between the packets sent by Zoom.)


Voordat ik Zoom uitdeed, merkte ik dat de grote meerderheid aan netwerkverkeer gebeurde op UDP, wat logisch is, UDP geschikt voor streamen is.

Zodra Zoom uit was en ik de internet browser aandeed, waren er diverse soorten netwerkverkeer te zien. Om een statistische overzicht te krijgen, heb ik de tab "Statistics" gecheckt. Daar kan informatie over de capture gesorteerd worden, zoals welke protocollen allemaal in gebruik waren, hoeveel data erdoor werd behandeld, de percentage tijd dat iedere protocol bezig is geweest, enz..


![B4 Zoom](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC01wireshark1.png)
![After Zoom](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC01wireshark2.png)
