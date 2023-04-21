# Networking Case Study
In this case study you take the role of a network administrator setting up a network in the new office of a small e-commerce company. Of course there are multiple ways to go about this problem, but this company has specifically said that network security is extremely important to them.
The office contains the following devices:
A web server where our webshop is hosted
A database with login credentials for users on the webshop
5 workstations for the office workers
A printer
An AD server
A file server containing internal documents

As a network administrator you get to choose which networking devices get used.


## Key-terms

- **Demilitarized Zone** (DMZ): Het doel van een DMZ netwerk is om een organisatie toegang tot onbetrouwbare netwerken te laten krijgen zonder haar interne netwerk in gevaar te brengen. In de DMZ worden resources geplaatst die extern toegankelijk moeten zijn, zoals servers voor _mail, DNS, FTP, web_, enz.
- **Active Directory**: De 	hoofdfunctie van AD is om beheerders in staat te stellen permissies en toegang naar netwerk middelen te beheren. Data (inclusief gebruikers, groepen, applicaties en apparaten) is bewaard als _objecten_, en die objecten zijn gecategoriseerd volgens hun naam en attributen.
- **Database Server**: _Database Servers_ worden gebruikt om databases op te slagen en te beheren, en om data toegang aan geautoriseerde gebruikers te verstrekken. Dit soort server houdt de data in een centrale locatie die regelmatig _backupt_ worden. Het laat ook gebruikers en applicaties toegang tot de data te krijgen overal in het netwerk. Een DB Server is elke server die een netwerk database applicatie verricht en databse bestanden onderhoudt, zoals _Microsoft SQL Server_, of _Oracle_.



## Opdracht
### Gebruikte bronnen

https://www.conceptdraw.com/How-To-Guide/active-directory-diagram

https://online.visual-paradigm.com/diagrams/templates/network-diagram/server-network-diagram-template/

https://afteracademy.com/blog/what-is-network-topology-and-types-of-network-topology/



https://www.linkedin.com/pulse/active-directory-dmz-nuts-marcus-rivera

https://www.quest.com/solutions/active-directory/what-is-active-directory.aspx

https://www.sciencedirect.com/topics/computer-science/database-server

https://www.fortinet.com/resources/cyberglossary/what-is-dmz


### Ervaren problemen

Verwarring over wat AD Server precies is, en de plaatsing daarvan in een netwerk.

### Resultaat

Er staat een firewall tussen de router en het Internet om aanvallen te voorkomen, en andere firewall tusssen de router en de switch, om te zorgen dat de interne netwerk niet lijdt als er iets mis gaat met één van de servers, en andersom.

De Web Server en Database Server verbind ik direct met de router, omdat ze allemaal functies uitvoeren voor de algemene buitengebruiker.

De 5 workstations verbind ik met elkaar via een switch, samen met de printer die door die workstations gedeeld wordt. Ik maak er een star topologie van, omdat het weinig workstations zijn.

De File Server blijft in de interne netwerk, omdat het voor interne documenten bestemd is. Hetzelfde gaat voor de AD Server, die gevoelige informatie bevat, en verder niet voor het publiek toegankelijk hoeft te zijn. Ze horen wel apart van de workstations te zijn, om te zorgen dat niemand die ze gebruikt ongeautoriseerde toegang heeft tot de gevoelige data die er in staat.


![Case Study](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW07CaseStudy.drawio.png)
