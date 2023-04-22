# Passwords

Een wachtwoord is een arbitraire _string van karakters_, inclusief letters, cijfers, of andere sybolen. Het wordt typisch gebruikt om de identiteit van een gebuiker te bevestigen. Vroeger werd het verwacht dat wachtwoorden onthoud zouden worden. Maar omdat de behoefte aan complexe wachtwoorden steeds groter wordt, en het feite dat één enkele persoon meerdere accounts heeft in meerdere apparaten, is het niet praktisch om wachtwoorden te onthouden.


## Key-terms


- **Brute Force Attacks**: Een _brute force attck_ is een _hacking methode_ die _trial and error_ gebruikt om wachtwoorden te kraken. Een hacker probeert een grote aantal combinaties tot hij de goede login of sleutel informatie krijgt. De naam _brute force_ komt van het feite dat aanvallers buitengewone krachtige pogingen maken om toegang te krijgen naar gebruikersaccounts. Al is het een oude methode, het blijft een populaire taktiek tussen hackers.

- **Encryption**: het proces waarbij gegevens worden omgezet in een reeks onleesbare tekens die geen vaste lengte hebben. Data versleuteling gebeurt door het gebruik van cryptografische sleutels. De data is versleuteld voordat het verzonden wordt en gedecodeerd door de gebruiker. Data versleuteling draait vooral om het bevestigen van identiteit en het beschermen van gegevensintegriteit.

  - De oorsprong van versleutelde berichten kan getraceerd worden, waardoor authenticatie van de bron makkelijk wordt.
  - In het geval dat de data gelekt wordt, het is makkelijk om te traceren wie het gedaan heeft en wanneer, waardoor het controleren op verantwoording eenvoudig wordt. Het helpt bij het efficiënt oplossen van veiligheidsinbreuken.
  - Data wordt versleuteld op een manier dat alleen degenen met de juiste sleutel kunnen de data lezen.

- **Hashing**: Een eenzijdig proces die een algoritme gebruikt om data te nemen en om te zetten naar een _hash value_ (ook bekend als _hash digest_). De lengte van de gegenereerde hash is meestal vastgesteld, en kleiner dan de originele tekst; hoewel het sterk varieert met zelfs de kleinste variaties. Het is bijna onmogelijk om een goede _hashing digest_ terug te draaien naar zijn originele form. De toepassingen van _hashing_ zijn:

  - Hashing dient als een _checksum_ om te garanderen dat een bepaalde stuk data of een bestand niet is gewijzigd.
  - Het helpt een gegeven waarde te vergelijken met een die opgeslagen is, en vermijdt daarmee duplicatie.
  - Hashing is gebruikt in verschillende digitale certificaten, inclusief SSL certificaten.
  - Het helpt om specifieke data in een grote database te vinden.
  - Hashing algoritmes worden gebruikt als een digitale certificaat en cryptografische applicaties.

- **Salting**: Een unieke waarde die toegevoegd kan worden aan het einde van een wachtwoord om een andere hash value te creëren. Dit voegt een aditionele laag beveiliging toe aan de _hashing proces_.

- **Rainbow Table**: Een _hacking tool_ die een vooraf berekende tabel gebruikt met omgekeerd wachtwoord hashes om wachtwoorden in een database te kraken. Terwijl ze security beheerders een methode geven om wachtwoord beveiligingsstandaarden te testen, ze geven ook _hackers_ een manier om snel wachtwoorden te kraken en ongeautorizeerde toegang naar computer systemen te krijgen. _Rainbow_ verwijst naar de verschillende kleuren in de tabel om verschillende _hashing_ en reductie functies en stappen te laten zien. Als iedere reductie functie een andere kleur is, dan zien de laatste _plaintexts_ en _hashes_ er uit als een regenboog.


- **Reduction Function**: Een wiskundige functie die een grote aantal mogelijke waarden indeelt naar een kleinere aantal mogelijke waarden, en wordt typisch gebruikt om de output van een _hash functie_ om te zetten naar een specifieke reeks waarden.


![rainbow](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_rainbow_table-536x288.png)


## Opdracht
### Gebruikte bronnen

https://comodosslstore.com/resources/hashing-vs-encryption-simplifying-the-differences/

https://crackstation.net/

https://manpages.ubuntu.com/manpages/bionic/en/man5/passwd.5.html

https://www.techtarget.com/searchsecurity/definition/salt

https://www.thesecurityblogger.com/understanding-rainbow-tables/

https://www.techtarget.com/whatis/definition/rainbow-table

https://www.thesslstore.com/blog/difference-encryption-hashing-salting/

### Ervaren problemen

Geen problemen ervaren.

### Resultaat

### Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.

Het hoofdverschil tussen _encryption_ en _hashing_ ligt in het feite dat, in het geval van versleuteling de data kan gedecodeerd worden om de originele tekst data te tonen met behulp van de juiste _key_; in _hashing_ dit kan helemaal niet. Dus iemand die naar een hash kijkt zal nooit kunnen weten wat de bijbehorende tekst is.


| Hashing | Encryption |
| ------- | ---------- |
| Data is _hashed_ naar een onleesbare _string_ die niet teruggedraaid kan worden naar een leesbare form | De versleutelde data kan gedecodeerd en omgezet worden naar leesbare form met een cryptografische sleutel |
| De onleesbare karakters hebben een vaste lengte | De onleesbare karakters hebben geen vaste lengte |
| Er worden geen sleutels gebruikt in hashing | Versleuteling gebeurt met gebruik van sleutels. Bij symmetrische encryptie, alleen een privé sleutel is gebruikt. Bij asymmetrische encryptie, privé en publieke sleutels worden gebuikt |

### Find out how a Rainbow Table can be used to crack hashed passwords.

_Rainbow Tables_ berekenen de _hash functie_ van iedere _string_ die in de tabel wordt geplaatst. Een rainbow table is gebouwd met ketens van allebei _hashing_ en _reduction_ functies. Gewone _plaintext_ wachtwoorden worden herhaaldelijk geplaatst door een keten van zulke operaties en dan opgeslagen in de tabel naast het bijbehorende hash.

Om een wachtwoord te kraken, of voor rainbow table aanvallen, worden grote aantallen hashes woorden doorgelopen in een dataset en dan door meerdere reductie stages om ze te splitsen in kleinere bestanddelen die gekoppeld aan plaintext karakters zijn. De plaintext wachtwoorden worden dan opgeslagen in de tabel naast de bijbehorende hashes.

Dus Rainbow Tables zijn een manier om het proces van _hashing_ te _reverse engineeren_.

Een programma om wachtwoorden te kraken wordt dan gebruikt om de _rainbow table_ lijst te vergelijken met gehashte wachtwoorden en de database. Als er een overeenkomst is, de plaintext die de _hash_ produceerde wordt opgehaald, en het proces wordt gestopt. 


### Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.

03F6D7D1D9AAE7160C05F71CE485AD31

03D086C9B98F90D628F2D1BD84CFA6CA

![Rainbow Tables](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_rainbowtables.png)

In de afbeelding kunnen we zien dat een Rainbow Table heel groot kan zijn. Elke Rainbow Table kan minstens een paar gigabytes hebben, wat het niet praktisch maakt voor een gewone gebruiker te downloaden. Verder kan het opzoek proces in een rainbow table heel lang duren. Dus ik heb het opgezocht met een online tool. De eerste hash kon gedecodeerd worden; de tweede niet.


![1st hash](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_hash1.png)
![2nd hash](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_hash2.png)


### Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.

![newuser](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_newusr.png)
![new user lookup](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_12345.png)

### Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.


![myshash](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_myshadow.png)
![Curthash](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-07_shadowcurt.png)

