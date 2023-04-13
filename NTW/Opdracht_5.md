# IP Addressing

Omdat er meer netwerk apparaten tegenwoordig bestaan dan wat vroeger verwacht was toen IPv4 gemaakt werd, is het aantal bestaande IPv4 adressen niet genoeg voor iedereen. Om hiermee uit te komen, worden privé IP adressen gebruikt en subnetting. Voor de doelen van dit opdracht wordt er op privé adressen in een netwerk gefocust.

Ondertussen is IPv6 uitgekomen, die de kwestie van gebrek aan IP adressen heeft behandeld, omdat er meer dan genoeg IPv6 adressen zijn voor de voorzienbare toekomst. Toch wordt IPv4 nog gebruikt, omdat IPv6 nog niet door alle protocollen ondersteund wordt. Verder zijn veel systemen werledwijd nog steeds georiënteerd op IPv4, wat implementatie van IPv6 moelijk maakt.


## Key-terms

- **IP adres**: Een unieke adres die een apparaat op het internet of op een lokale netwerk identificeert. IP betekent Internet Protocol, de zet regels die beheren de data die verstuurd wordt via Internet of een lokale netwerk.

- **Dynamic Host Configuration Protocol (DHCP)**: Een netwerkbeheer protocol gebruikt om IP adressen toe te wijzen. IP adressen kunnen statisch of dynamisch zijn. Statische IPs zijn permanent, dynamische IPs niet; ze veranderen als hun _lease time_ op is. DHCP is een dinamysche protocol omdat het tijdelijke IP adressen toewijst.

- **Public IP adres**: Een publieke IP adres is het primaire adres aangesloten aan je hele netwerk. Elk verbonden apparaat heeft zijn eigen IP adres, maar die worden allemaal omgevat in de algemene IP adres van een netwerk. 

- **Private IP adres**: Elk apparaat verbonden aan je netwerk heeft een privé IP adres. Alle apparaten moeten apart apart identificeerd kunen worden; daardoor genereert een router privé IP adressen die uniek zijn binnen het netwerk.

- **IP adress conflict**: Een IP adres conflict ontstaat als twee of meer apparaten op hetzelfde netwerk hetzelfde IP adres toegewezen krijgen. Dan kunnen ze niet meer goed verbinden met het internet.

## Opdracht
### Gebruikte bronnen

https://www.makeuseof.com/tag/whats-ip-conflict-resolve/

https://superuser.com/questions/801105/do-two-computers-connected-on-the-same-wi-fi-have-the-same-ip-address

https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address

https://www.whatismyip.com/why-does-wimi-show-a-different-ip-address-than-ipconfig/

https://www.atatus.com/blog/difference-between-ipv4-and-ipv6-why-havent-we-entirely-moved-to-ipv6/


### Ervaren problemen

Tijdens het aanpassen van de IP van mijn mobiel naar die van mijn PC, nadat ik het terug heb gedraaid, wordt mijn mobiel nog steeds met hetzelfde naam als mijn PC getoond.

### Resultaat


### Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi. Zijn de adressen hetzelfde of niet? Leg uit waarom.

Het publieke adres van alle apparaten binnen een netwerk is hetzelfde als die van de router, in dit geval. 


![PC IP](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW05_whatisip.png)
![Mobiel](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW05_Screen.png)


### Ontdek wat je privé IP adres is van je laptop en mobiel op wifi. Zijn de adressen hetzelfde of niet? Leg uit waarom.

![IPs](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW05_IPs.png)

Het privé IP adres van mijn PC is 192.168.68.101, en die van mijn mobiel 192.168.68.103

Ze mogen niet hetzelfde zijn, want anders ontstaat er een _IP adress conflict_.

### Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?

Op mijn scherm was de naam en MAC adres van mijn mobiel verdwenen, omdat het door de router als hetzelfde als mijn PC beschouwd was. In de praktijk, waren ze allebei nog met het Internet verbonden, en zolang er één geen online activiteiten uitvoerde, de andere kon de internet gebruiken. Maar op het moment dat ze allebei online activiteiten gingen uitvoeren, bleven ze vastzitten in de poging tot verbinding. 


### Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?

![Netwerk](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW05_netconfig.png)

Subnet Mask is 255.255.255.0 , wat betekent dat alle adressen binnen het bereik van 192.168.68.0-192.168.68.255 beschikbaar zijn. Als ik dan het volgende octet verander, ben ik wel in de netwerk verbonden, maar dan zonder internet.
