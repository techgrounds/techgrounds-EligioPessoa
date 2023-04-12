# Protocols

Een protocol is een zet regels die de communicatie tussen computers in een netwerk beheren. Om met elkaar kunnen "praten", moeten twee computers hetzelfde taal spreken. Verschillende netwerk protocols en standaarden zijn vereist om ervoor te zorgen dat een computer (onfhankelijk van bestuursysteem, netwerkkaart of applicatie) met andere computer kan communiceren, wat de afstand tussen hen dan ook is. 


## Key-terms

- **RFC**: documenten die de protocollen en andere aspecten van het internet beschrijven. RFC documenten komen tot stand door een discussie en publicatieproces dat wordt georganizeerd door de RFC Editor. Ze worden uiteindelijk als standaard bekrachtigd door de Internet Engineering Task Force.


## Opdracht
### Gebruikte bronnen

https://www.ietf.org/standards/rfcs/

https://fcit.usf.edu/network/chap2/chap2.htm

https://www.w3schools.com/cybersecurity/cybersecurity_networking.php

https://www.quora.com/How-exactly-are-network-protocols-implemented

https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet/

https://andrewhowdencom.medium.com/writing-up-a-request-for-comments-4a6be864bb8a



### Ervaren problemen

Er was verwarring om te onderscheiden tussen standaard en protocol, omdat deze termen vaak afwisselend met elkaar worden gebruikt. Ook worden protocols bij meer dan één OSI laag gebruikt, vooral in de Lower Layers.

### Resultaat

### Identify several other protocols and their associated OSI layer. Name at least one for each layer.

Layer 1/Physical Layer:

- **RS232**: een standard protocol gebruikt voor serial communication (een communicatie methode dat één of twee transmissie lijnen gebruikt om data te verzenden en ontvangen. De bits worden een voor een continuu door verzonden en ontvangen). Gebruikt om computers en betreffende randapparaten te verbinden.

- **Synchronous Optical Networking (SONET)**: Gebruikt om meerdere data streams te multiplexen over een fiber optic kabel. (Multiplexen is een manier om meerdere signalen of data streams tegelijkertijd te versturen over een enkele, complexe signaal)

- **Controller Area Network (CAN Bus)**: de CAN Bus systeem laat elke ECU (Electronic Control Units) met alle andere ECUs communiceren zonder complexe speciale bedrading.

Layer 2 / Data-Link Layer:


- **Point-to-Point Protocol (PPP)** - een WAN protocol die vaak gebruikt wordt in in breedband communicatie, omdat het hoge volumes dat met hoge snelheid kan overdrachten.
- **Neighbor Discovery Protocol (NDP)**: Identificeert de relatie tussen verschillende dichtbijzijnde apparaten in een IPv6 netwerk. Voert uit functies zoals router discovery en MAC adressen opzoeken in IPv6.

Layer 3 / Network Layer:

- **Network Address Translation (NAT)**: Een manier om meerdere privé-ip adressen in kaart te brengen naar een publieke IP adres voordat de informatie naar het Internet wordt verzonden.
- **Internet Protocol (IP)**: zorgt voor pakket levering vanuit de bron host naar de bestemingshost door naar de IP adressen in de packet headers te kijken. 
- **Internet Control Message Protocol (ICMP)**: het voorziet hosts met informatie over netwerk problemen. Wordt gebruikt om te bepalen of data op de juiste bestemming op de juiste tijd geleverd wordt.


Layer 4 / Transport Layer:

- **TCP (Transport Layer Protocol)**: Applicaties kunnen hiermee op elkaar inwerken alsof ze fysiek met een circuit verbonden zouden zijn. TCP zendt data op een karakter-per-karakter systeem, in plaats van gescheiden pakketten. Een zending heeft een startpunt (die de verbinding maakt), de hele transmissie in byte orde, en een eindpunt (waarmee de verbingen wordt afgesloten).

- **UDP (User Datagram Protocol)**: voert datagram levering. UDP checkt de verbindingen op fouten niet. Wordt gebruikt door applicaties die kleine aantallen data gebruiken, en het proces van verbindingen vaststellen en valideren kunnen overslaan.

- **Quick UDP Internet Connection (QUIC)**: een nieuwe protocol ontworpen door Google om HTTP verkeer meer secuur, efficient en sneller te maken. Gebruikt voor applicaties die snelle online service nodig hebben. Vaak gebruikt door gamers, streamers, en iedereen die VoIP dagelijks gebruikt.


Layer 5 / Session Layer:


- **Session Initiation Protocol (SIP)**: een signalering protocol die Voice over Internet Protocol (VoIP) mogelijk maakt door berichten tussen endpoints te definiëren, en de elementen van een gesprek te beheren. SIP ondersteunt spraakoproepen, video conferenties, instant messaging en media distributie.

- **Socket Secure (SOCKS)**: een protocol die netwerkpakketten uitwisselt tussen een client en een server via een proxy server. Een SOCKS server maakt proxies van TCP verbindingen naar een willekeurige IP adres, en verstrekt een middel om UDP pakketten door te sturen.

Layer 6 / Presentation Layer:

- **American Standard Code for Information Interchange (ASCII)**: een vraag-en-antwoord protocol waar een host ASCII karakters gebruikt om _commands_ naar een apparaat te sturen, en vervolgens antwoord krijgt van die apparaat. De ASCII command is gebruikt om apparaten te configureren, data naar apparaten te sturen, en data en status informatie terug te lezen van apparaten.

- **Secure Sockets Layer (SSL)**: Zorgt ervoor dat data die overgedragen wordt tussen een clien en een server privé blijft. Dit protocol maakt het mogelijk voor de client om de identiteit van de server te autentificeren.



Layer 7 / Application Layer:

- **File Transfer Protocol (FTP)**: Maakt het mogelijk om bestanden over te dragen.

- **Internet Message Access Protocol (IMAP)**: om toegang te krijgen tot email of bulletin board berichten van een mail server of dienst. IMAP laat een e-mail programma afgelegen opgeslagen enericht alsof ze lokaal op schijf zouden staan.


### Figure out who determines what protocols we use and what is needed to introduce your own protocol.

- **World Wide Web Consortium (W3C)**: Veel van de internet standaarden die we kennen, zoals HTML, XHTML, CSS, XML, en veel meer, waren voorgesteld, besproken, bepaald en geformaliseerd door het W3C.
- **Telecommunication Standardization Sector (ITU-T)**: de divisie verantwoordig voor standaarden in de ICT sector.
- **Internet Architecture Board (IAB)**: een organisatie die bestaat als commissie van de Internet Engineering Task Force (IETF) en als adviseur van de Internet Society (ISOC)
- **Internet Society (ISOC)**: een Amerikaanse nonprofit belangenorganisatie gecreërd in 1992 om de ontwerpingsproces van internet standaarden te ondersteunen.
- **Internet Engineering Task Force (IETF)**: de IETF bestaat uit verschillende werkgroepen die toegewijd zijn aan het engineering en standaard creëren met een korte  levensduur. Het ontvangt beslissingen vanuit de werkgroep, identificeert operationele problemen van het internet, stelt oplossingen voor, en ontwerpt en beoordeelt specificaties.
- **Internet Research Task Force (IRTF)**: de IRTF focust op lange termijn onderzoek om internet protocollen, applicaties, architectuur, en technologie te ontwikkelen.
- **Institute of Electrical and Electronic Engineers (IEEE)**: de IEEE is toegewijd aan engineering en electrical engineering.
- **Internet Corporation for AssignedNames and Numbers (ICANN)**: opgestart in California in 1988 om voor de operationele stabiliteit van het internet te zorgen. Het is een technische coordinerende en regelgevende instantie.
- **Internet Assigned Numbers Authority (IANA)**: coordineert DNS, IP adressing, en andere internet protocol bronnen. Alle domein namen en IP adressen zijn zijn toegewezen vanuit de IANA.


Om een nieuwe protocol te introduceren: 

- De relevante organisatie moet identificeerd en uitgezocht worden.
- Daarna moeten de standaarden van de procedures uit die organisatie gevolgd worden voor het indienen van voorstellen.
- Men can deelnemen aan het stardaardizatieproces door vergaderingen bij te wonen, bijdragen aan discussies, en feedback geven tegenover andere voorstellen.
- Antwoorden op feedback en revisies die vereist worden door de standaard organizaties, of andere belanghebbenden.
- Goedkeuring krijgen en adoptie: Als een protocol aanvaard is door de standaarden organisatie, het kan gepubliceerd worden als een standaard en gepromoveerd worden voor adoptie bij leveranciers en andere belanghebbenden.


### Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.

![Wireshark](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW-03_report.png)

Een voorbeeld van een protocol die hier te zien is is Adress Resolution Protocol (ARP). Het zorgt dat een MAC adres verbonden wordt aan een IP, en dat data pakketten naar de juiste adressen worden verstuurd.
