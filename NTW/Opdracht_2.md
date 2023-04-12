# Network Devices

Netwerkapparatuur zijn fysieke apparaten die hardware in een computer netwerk verbinden om ze met elkaar te laten communiceren. Sommige apparaten hebben beperkte capaciteiten, en zijn geschikt alleen voor kleine netwerken, waarbij andere apparaten uitgebreide capaciteiten hebben en meer geschikt zijn voor grote netwerken.

## Key-terms

**Dynamic Host Configuration Protocol (DHCP)**: een client/server protocol die automatisch een IP host verstrekt, met een IP adres en andere gerelateerde configuratie, zoals subnet mask en default gateway. Zonder DHCP, de IP adressen van computers moeten handmatig geconfigureerd worden, en IP adressen van computers die uit de netwerk zijn verwijderd moeten handmatig teruggevorderd worden.

**Customer Premises Equipment (CPE)**: telecommunicatie en informatie technologie die op de fyzieke locatie van de klant gehouden wordt, ipv op het locatie van de dienstverlener.

## Opdracht

### Gebruikte bronnen

https://www.geeksforgeeks.org/network-devices-hub-repeater-bridge-switch-router-gateways/

https://github.com/MicrosoftDocs/windowsserverdocs/blob/main/WindowsServerDocs/networking/technologies/dhcp/dhcp-top.md

https://www.techtarget.com/searchnetworking/definition/customer-premises-equipment

### Ervaren problemen

Ik heb geen admin toegang tot de router van mijn eigen netwerk, en kan dus de DHCP configuraties niet instellen. Ik mocht naar de scherm van Roan kijken, om te zien hoe die configuraties eruitzien.

### Resultaat

### Benoem en beschrijf de functies van veel voorkomend netwerkapparatuur

**Repeater** - Een repeater opereert in de _Physical Layer_. Zijn taak is om een signaal te regenereren over hetzelfde netwerk voordat die te zwak of corrupt wordt, om de afstand te verlengen waar die signaal overgedragen wordt. Het is belangrijk op te merken dat het signaal wordt niet vergroot. Als het zwak wordt, kopieërt de repeater het bit voor bit en regenereert het op de netwerk topologie connectors in zijn oorspronkelijke sterkte. Het is een 2 port apparaat.


**Hub** - Een hub is net als een multi-port reapeater. Een hub verbindt meerdere draden van verschillende systemen. Een hub kan geen data filteren, dus data pakketen worden naar alle verbonden apparaten verstuurd. Het kan ook geen paden uitkiezen voor data pakketten, waardoor het inefficiënt en verkwistend is.

Soorten hubs:

- **Active hub**: Deze hub heeft zijn eigen stroomvoorziening en kan het signaal verhelderen, vergroten en doorsturen in de netwerk. 
- **Passive hub**: Deze hubs verzamelen draden vanuit nodes en stroom vanuit de active hub. Deze hubs sturen signalen door in de netwerk zonder ze te verhelderen of versterken, en kunnen de afstand tussen nodes niet verlengen.
- **Intelligent Hub**: Werkt als een active hub, met beheer op afstand capaciteit. Ook laat het een administrator de traffic die door het hub gaat te monitoren, en elke port in de hub te configureren.


**Bridge** - Een bridge opereert in de _Data Link layer_. Een bridge is een repeater, met de toegevoegde functie om inhoud te filteren door de MAC adressen van bron en bestemming te lezen. Het wordt ook gebruikt om twee LANs die op hetzelfde protocol werken, te verbinden. Het heeft een enkele input en een enkele output port.

Soorten bridges:

- **Transparent Bridge**: Bij deze zijn de verbonden punten onbewust van de aanwezigheid van de bridge, waardoor er geen herconfiguratie nodig is. Deze bridges gebruiken twee processen: bridge forwarding en bridge learning.
- **Source Routing Bridges**: Bij deze, wordt de routing uitgevoerd door de source station, en de frame specificeert welke route gevolgd moet worden. De host kan de frame ontdekken door een speciale frame te sturen, de "discovery frame", die spreidt door het hele netwerk via alle mogelijke routes naar zijn bestemming.


**Switch** - Een switch is een multiport bridge met een buffer en een ontwerp die het zijn prestatie vergroten en meer efficiënt maken. Een switch is een _Data-Link Layer_ apparaat.  De switch kan checken voor fouten voordat de data doorgestuurd wordt, waardoor het efficiënt is, omdat geen foutieve pakketten doorgestuurd worden, en goede pakketten worden alleen naar de juiste ports doorgestuurd.

Soorten Switches:

- **Unmanaged switches**: Deze switches hebben een eenvoudige plug-and-play ontwerp, en bieden geen geavanceerde configuraties aan. Ze zijn gepast voor kleine netwerken, of als verlenging voor een grotere netwerk.
- **Managed switches**: Deze switches biede geavanceerde configuraties aan zoals VLANS, QoS en link aggregation. Ze zijn gepast voor grote, complexe netwerken en maken gecentraliseerde beheer mogelijk.
- **Smart switches**: Deze switches hebben functies die vergelijkbaar zijn met managed switches, maar zijn makkelijker om op te zetten en te beheren. Ze zijn gepast voor klein tot medium grootte netwerken.
- **Layer 2 switches**: Deze switches opereren op de _Data-Link Layer_ van het OSI model en zijn verantwoordig voor het doorsturen van data tussen apparaten op hetzelfde netwerk segment.
- **Layer 3 switches**: Deze switches opereren op de _Network Layer_ van het OSI model en kunnen data routen tussen verschillende netwerk segmenten. Ze zijn geavanceerder da Layer 2 switches en worden vaak gebruikt in grotere, meer complexe netwerken.
- **PoE switches**: Deze switches hebben Power over Ethernet capaciteiten, waardoor ze stroom kunnen leveren naar netwerk apparaten over hetzelfde kabel die de data draagt.
- **Gigabit switches**: Deze switches ondersteunen _Gigabit Ethernet_ snelheden, die sneller zijn dan traditionele Ethernet.
- **Rack-mounted switches**: Deze switches zijn ontworpen om op een _server rek_ gemonteerd te worden, en zijn geschikt voor gebruik in data centers of andere grote netwerken.
- **Desktop switches**: Deze switches zijn ontworpen voor gebruik op een desktop of op een kleine kantoor omgeving, en zijn typisch kleiner in maat dan rack-mounted switches.
- **Modular switches**: Deze switches hebben _modulair ontwerp_, waardoor het makkelijk is om uit te breiden of aan te passen. Ze zijn geschikt voor grote netwerken en data centers.

**Routers** - Een router is een apparaat zoals een switch, die data pakketten routeert gebaseerd op hun IP adressen, en het is vooral een _Network Layer_ apparaat. Routers verbinden meestal LANs en WANs en hebben een routeringstabel die dynamisch bijgewerkt wordt, waarop ze beslissingen nemen over het routeren van data pakketten. De router onderscheidt de broadcast domeinen van de hosts die ermee verbonden zijn.


**Gateway** - Een gateway is een doorgangspunt waar twee netwerken verbonden worden die op _verschillende netwerk modellen_ kunnen werken. Ze werken als boodschap agenten die data vanuit een systeem nemen, interpreteren, en overdragen aan andere systeem. Gateways worden ook _protocol converters_ genoemd, en opereren op elke netwerk laag. Gateways zijn vaak complexer dan _switches_ of _routers_. 
  

**Brouter** - Ook bekend als bridging router, het is een apparaat dat eigenschappen combineert van _bridges_ en _routers_. Het kan werken op de _Data-Link layer_ of de _Network layer_. Als router, het kan pakketten routeren over netwerken; en als bridge, het kan locale netwerkverkeer filteren.

**Network Interface Card (NIC)** - Een netwerk adapter die gebruikt wordt om een computer op een netwerk te verbinden. Het is op de computer geïnstalleerd om een LAN op te zetten. Het heeft een unieke id die op de chip geschreven is, en een connector om aan een kabel te verbinden. De kabel dient als interface tussen de computer en de router of modem. NIC is een _Layer 2_ apparaat, wat betekent dat het op allebei de Physical en Data-Link layers werkt.


### De meeste routers hebben een overzicht van alle verbonden apparaten, vind deze lijst. Welke andere informatie heeft de router over aangesloten apparatuur?

- De informatie die te zien valt over verbonden apparaten is: Naam, MAC adres, private IP, soort verbinding (Wireless 5G/2.4G) 

![Netwerk](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW-02%20eigen%20netwerk.png)


### Waar staat je DHCP server op jouw netwerk? Wat zijn de configuraties hiervan?

Hier kunnen we zien dat de local address, subnet mask, lease time en nummer CPEs geconfigureerd kunnen worden.

![DHCP](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW-02%20DHCP.png)

