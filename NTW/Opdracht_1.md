# OSI Stack


## Key-terms
**OSI Model** - OSI betekent Open Systems Interconnection. Het beschrijft seven theoretische lagen die computer systemen gebruiken om over een netwerk te communiceren. Het is een netwerk architectuur model die geïntroduceerd was in 1983 door representanten van de grotere computer en telecom bedrijven, en werd geadopteerd door de ISO (International Organization for Standardization) in 1984.


**TCP/IP Model** - Het moderne internet is niet op OSI gebaseerd, maar op de TCP/IP model, die als eerste kwam. Omdat het de standaard beschrijft waarop het Internet gebouwd is, het is een meer realistische model.
- De originele TCP/IP model bestond uit 4 lagen: Link Layer, Internet Layer, Transport Layer, Application Layer.
- Tegenwoordig bestaat het uit 5 lagen: Physical Layer, Data-Link Layer, Network Layer, Transport Layer en Application Layer.

## Opdracht
### Gebruikte bronnen
https://www.imperva.com/learn/application-security/osi-model/

https://www.geeksforgeeks.org/layers-of-osi-model/

https://www.geeksforgeeks.org/tcp-ip-model/

https://www.ccnahub.com/ip-fundamentals/understanding-tcp-ip-and-osi-models/

https://docs.oracle.com/cd/E19253-01/816-4554/ipov-10/index.html

### Ervaren problemen
Het sorteren voor de juiste informatie, en het begrijpen van de verschillen tussen modellen.

### Resultaat

### The OSI model and its uses.


**Layer 1 - Physical Layer:**

De Physical Layer heeft de taak om een fysieke connectie tussen apparaten te vestigen. Informatie is opgeslagen in _bits_. Het heeft de taak om individuele bits van een node naar de andere te sturen. Wanner deze laag data ontvangt, de ontvangen signaal is omgezet naar 0s en 1s, en verstuurd naar de Data_link Layer, die ze allemaal weer in elkaar zet.

Functies van de Physical Layer:

- **Bit Synchronisatie**: de Physical Layer sychroniseert de bits met een klok, die controleert de zender en de ontvanger, en zorgt dat synchronisatie op bit-niveau ontstaat.
- **Bit Rate controle**: de Physical Layer bepaalt de snelheid van bits per seconde die overgedragen wordt.
- **Fysieke Topologie**: de Physical layer specificeert hoe verschillende apparaten/nodes in een netwerk met elkaar gesteld worden: bus, star of mesh topologie.
- **Transmission Mode**: de Physical Layer bepaalt ook hoe data tussen twee verbonden apparaten vloeit. De verschillende modes transmissie zijn: simplex, half-duplex en duplex.

Apparaten van de Physical Layer: _Hub, Repeater, Modem_.


**Layer 2- Data Link Layer (DLL)**:

De Data Link Layer zorgt voor het leveren van data tussen knooppunten (nodes). De algemene functie van deze laag is om te zorgen dat de overdracht van data foutloos gebeurt van een knooppunt naar de andere. Als een data pakket in een netwerk komt, de DLL moet het overdragen naar de MAC adres van de netwerkhost.
De Data Link Layer is gedeeld in twee onderlagen:

- **Logical Link Control (LLC)**
- **Media Access Control (MAC)**

De pakket die van de Network Layer is ontvangen wordt in _frames_ gedeeld, afhankelijk van de frame grootte bepaald door de **NIC (Network Interface Card)**. DLL sluit ook de MAC adressen van afzender en ontvanger in de header.

De _MAC adres_ van de ontvanger is verkregen door een **ARP (Address Resolution Protocol)** verzoek te plaatsen die vraagt _"Van wie is dit IP adres?"_ en de bestemming host antwoordt met zijn _MAC adres_.

De functies van de Data Link Layer zijn:

- **Framing**: Framing geeft een afzender een manier om een set bits te verzenden die relevant zijn voor de ontvanger. Dit is door speciale bit patronen bij te voegen aan het begin en einde van de frame.
- **Physical Addressing**: Na het creëren van frames, de DLL voegt de MAC adressen van de afzender en/of ontvanger in de header van elke frame.
- **Error Control**: De DLL verstrekt  demechanisme van foutcontrole, waar het beschadigde/verloren frames opspoort en herstuurt.
- **Flow Control**: De datasnelheid moet stabiel aan beide kanten zijn, anders wordt de data corrupt - daarom coordineert Flow Control de hoeveelheid data die verzonden kan worden voordat een erkenning wordt ontvangen.
- **Access Control**: Als een enkele communicatie kanaal door meerdere apparaten gedeeld wordt, de MAC onderlaag van de DLL helpt te bepalen welke apparaat controle over het kanaal heeft op een gegeven moment.

Een pakket in de DLL wordt genoemd als een _Frame_
DLL wordt behandeld door de _NIC (Network Interface Card)_ en apparaat drivers van de host machines.
DLL apparaten: _Switch_ en _Bridge_.





**Layer 3- Network Layer**

De Network Layer zorgt voor de dataoverdracht van een host naar de andere in verschillende netwerken. Het zorgt ook voor _packet routing_ i.e. de kortste pad selecteren voor de dataoverdracht, van de aantal routes beschikbaar. De IP adressen van de afzender en ontvanger worden in de _header_ geplaatst door de Network Layer.

Functies van de Network Layer:


- **Routing**: De Network Layer protocollen bepalen welke route geschikt is vanaf de bron tot de bestemming. 
- **Logical Addressing**: Om ieder apparaat in de netwerk uniek te identificeren, de Network Layer bepaalt een adressering schema. De IP adressen van de afzender en ontvanger worden in de header geplaatst. Een adres in zo'n schema herkent elke apparaat op een unieke manier.

De Network Layer wordt geïmplememteerd door netwerk apparaten zoals _routers_.




De Physical Layer, Data Link Layer en Network Layer staan ook bekend als de **Hardware Layers** of **Lower Layers**.



**Layer 4 - Transport Layer**

De Transport Layer verstrekt diensten naar de Application Layer en neemt diensten van van de Network Layer. Het is verantwoordelijk voor de _End to End_ levering van de hele bericht. De Transport Layer zorgt ook voor het aanvarden van succesvolle data overdracht, en herstuurt de data als er een fout is. De data in de Transport Layer wordt genoemd als _Segments_. 

Aan de kant van de afzender, de TL ontvangt de geformateerde data van de bovenste lagen, voert segmentatie uit, en implementeert _Flow & Error control_ om voor goede data overdracht te zorgen. Ook worden bron en bestemming port nummers toegevoegd in de _header_, en wordt de gesegmenteerde data verstuurd naar de Network Layer. 
- De zender moet de port weten die bij de applicatie van de ontvanger hoort. Vele applicaties hebben standaard port nummers vastgesteld.

Aan de kant van de ontvanger, de TL leest de port nummer vanuit de header en stuurt de data die het ontvangen heeft door naar de behorende applicatie. Het voert ook sequencing en reassembling van de gesegmenteerde data.

Functies van de Transport Layer :

- **Segmentation en Reassembly**: Deze laag neemt het bericht over van de Session Layer en breekt het af in smallere segmenten. Elke segment heeft een header die er aan gekoppeld is. De TL op de bestemming zet het bericht weer in elkaar.

- **Service Point Addressing**: Om het bericht naar het goeie proces te kunnen overhandigen, voegt de TL een soort adres toe die heet _Service Point Address_ of _Port Address_. Dit adres specificeert naar welke proces het bericht verstuurd moet worden.


Diensten verstrekt door de Transport Layer:

- **Connection-Oriented Service**: Een drie-fase proces die omvat: _connection establishment_, _data transfer_, _termination/disconnection_. In dit soort transmissie, de ontvanger stuurt een aanvaarding terug naar de bron na een pakket of groep pakketten is ontvangen. Dit soort transmissie is betrouwbaar en veilig.

- **Connectionless Service**: Het is een proces met één fase, inclusief _data transfer_. In dit soort transmissie, de ontvanger voert geen bevestiging van pakketontvangst. Dit zorgt voor snellere communicatie tussen apparaten. Dit proces is minder betrouwbaar.


De Transport Layer wordt beheerd door het bestuursysteem. Het is een gedeelte ervan, en comuniceert met de Application Layer door _system calls_ te maken.

De Transport Layer wordt beschouwd als de **hart van het OSI model**.



(De volgende 3 lagen worden als één enkele laag beschouwd in de TCP/IP model als de "Application Layer". Deze 3 lagen worden door de netwerk applicatie zelf uitgevoerd. Ze staan ook bekend als _Upper Layers_ of _Software Layers_.)


**Layer 5 - Session Layer**

Deze laag is verantwoordig voor het tot stand brengen van verbindingen, sessie onderhoud, autenticatie, en zorgt ook voor beveiliging.

De functies van de Session Layer:

- **Session establishment, maintenance and termination**: de Session Layer laat twee processen een verbinding maken, gebruiken en vervolgens beëindigen.
- **Synchronization**: dit laag laat een proces checkpoints toevoegen die als synchronisatie punten worden beschouwd. Deze synchronisatie punten helpen een fout te identificeren zodat de data her-synchroniseerd kan worden, en een bericht niet voortijdig beëindigt, waardoor dataverlies wordt vermijd.
- **Dialog Controller**: de Session Layer laat twee systemen met elkaar communiceren in _half-duplex_ of _full-duplex_.



**Layer 6 - Presentation Layer**

Ook **Translation Layer** genoemd. De data van de Application Layer wordt geëxtraheerd en behandeld volgens het benodigde formaat om overdracht te worden over het netwerk.


Functies van de Presentation Layer:

- **Translation**: Vertaling, bijvorbeeld, van ASCII naar EBCDIC.
- **Encryption/Decription**: Data encryptie vertaalt de data naar een andere form of code. De versleutelde data wordt _ciphertext_ genoemd, en de gedecodeerde data wordt _plain text_ genoemd. Een _key value_ wordt gebruikt voor zowel het _versleutelen_ als het _decoderen_ van data.
- **Compression**: Compressie vermindert het aantal bits die op het netwerk overhandigd moeten worden.


**Layer 7- Application Layer**

De Aplication Layer, ook **Desktop Layer** genoemd, wordt geïmplementeerd door de _netwerk applicaties_. Die produceren de data, die overgedragen moet worden over de netwerk. Deze laag dient ook als toegangspunt voor de applicatie diensten om toegang tot de netwerk te krijgen, en de ontvangen informatie aan de gebuiker te verstrekken.


- Voorbeelden: _Internet Browsers, Skype Messenger_.



Functies van de Application Layer: 

 - **Network Virtual Terminal**
 - **FTAM- File transfer access and management**
 - **Mail Services**
 - **Directory Services**



### The TCP/IP model and its uses.

Het OSI model beschrijft ideale netwerk communicaties met een familie van protocols. TCP/IP komt hier niet direct overeen. TCP/IP voegt meerdere OSI lagen in één enkele laag, of gebruikt bepaalde lagen niet. 


De originele TCP/IP model bestond uit 4 lagen: _Link Layer, Internet Layer, Transport Layer, Application Layer_.
Tegenwoordig bestaat het uit 5 lagen: _Physical Network Layer, Data-Link Layer, Network Layer, Transport Layer_ en _Application Layer_.


**Physical Network Layer**: de Physical Network Layer specificeert de kenmerken van de hardware de op het netwerk gebruikt dient te worden. Bijvoorbeeld, de fysieke kenmerken van de communicatie media. De Physical Layer van TCP/IP beschrijft hardware standaarden zoals IEEE 802.3, de specificatie voo Ethernet netwerk media, en RS-232, de specificatie voor standaard pin connectors.


**Data-Link Layer**: de Data-Link Layer identificeert de netwerk protocol type van een pakket, bijv. TCP/IP. De Data-Link layer zorgt ook voor foutpreventie en framing. Voorbeelden van Data-Link Layer protocols zijn Ethernet IEEE 802.2 framing en Point-to-Point Protocol (PPP) framing.


**Internet Layer**: bepaalt de protocols die verantwoordig zijn voor de logishe overdracht van data over het hele netwerk; die zijn dus tussen de belangrijkste in het hele TCP/IP model. De hoofd protocollen hiervan zijn:

- **IP (Internet Protocol)**: zorgt voor pakket levering vanuit de bron host naar de bestemingshost door naar de IP adressen in de packet headers te kijken. 
- **ICMP (Internet Control Message Protocol)**: het voorziet hosts met informatie over netwerk problemen.
- **ARP (Address Resolution Protocol)**: vindt het hardware adres van een host door middel van een bekende IP adres.


**Transport Layer**: zorgt dat pakketten in volgorde en zonder fouten aankomen, door erkenningen van data ontvangst uit te wisselen, en verloren pakketten hersturen. Dit soort communicatie staat bekend als end-to-end. De hoofdprotocollen hiervan zijn:

- **TCP (Transport Layer Protocol)**: Applicaties kunnen hiermee op elkaar inwerken alsof ze fysiek met een circuit verbonden zouden zijn. TCP zendt data op een karakter-per-karakter systeem, in plaats van gescheiden pakketten. Een zending heeft een startpunt (die de verbinding maakt), de hele transmissie in byte orde, en een eindpunt (waarmee de verbingen wordt afgesloten).

- **SCTP (Stream Control Transmission Protocol)**: een betrouwbare, verbinding georiënteerde Transport Layer protocol die dezelfde diensten uitvoert als TCP. Daar bovenop kan SCTP verbindingen ondersteunen tussen systemen die meer dan één adres hebben, of "multihomed". Bepaalde applicaties, zoals die gebruikt door de telecommunicatie industrie, dienen gerund te worden in SCTP, en niet op TCP.

- **UDP (User Datagram Protocol)**: voert datagram levering. UDP checkt de verbindingen _niet_ op fouten. Wordt gebruikt door applicaties die kleine aantallen data gebruiken, en het proces van verbindingen vaststellen en valideren kunnen overslaan.


**Application Layer**: bepaalt standaard Internet diensten en netwerk applicaties dat iedereen kan gebruiken. Deze diensten werken met de Transport Layer om data te verzenden en ontvangen. Voorbeelden van protocollen hiervan zijn:

- FTP
- HTTP en HTTPS
- SSH
- Naam diensten, zoals NIS en DNS
- Directory diensten (LDAP)
- Bestand diensten, zoals NFS






### Verschillen tussen TCP/IP en OSI




| **TCP/IP** | **OSI** |
|------- | --- |
| 5 lagen | 7 lagen |
| Meer betrouwbaar | Minder betrouwbaar |
| Heeft geen stricte grenzen | Heeft stricte grenzen|
| Volgt een horizontale aanpak | Volgt een verticale aanpak|
| Session en Presentation layer zijn onderdeel van de Application Layer | OSI heeft aparte Session en Presentation layers |
| Eerst werden protocols ontwerpt, daarna model | Eerst werd model ontwerpt, daana protocols |
| Transport Layer geeft geen zekerheid van pakket levering | Transport Layer geeft zekerheid van pakket levering |
| Network Layer verstrekt alleen verbindingloze diensten | Network Layer verstrekt verbindingloos - en verbinding georiënteerde diensten |
| Protocollen kunnen niet makkelijk vervangen worden | Protocollen zijn goed gedekt, en makkelijk te vervangen in lijn met veranderingen in technologie |


