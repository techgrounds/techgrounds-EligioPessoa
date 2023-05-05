# Elastic Beanstalk
Amazon Elastic Beanstalk is een beheerservice voor webinfrastructuur. Het zorgt voor de implementatie en schaalbaarheid van webapplicaties en -services. In eenvoudige bewoordingen neemt dit platform als een service (PaaS) applicatiecode en implementeert deze terwijl het de ondersteunende architectuur en computerresources levert die nodig zijn om code uit te voeren. Elastic Beanstalk beheert ook volledig de patching en beveiligingsupdates voor die ingerichte _resources_.

De naam "Elastic Beanstalk" is een verwijzing naar de bonenstaak die tot in de wolken groeide in het sprookje Jaap en de bonenstaak. De metafoor van "bonenstaak" in AWS Elastic Beanstalk, een platform voor het implementeren en beheren van webapplicaties, verwijst naar het gemak en de snelheid van het opzetten en laten groeien van een applicatie in de cloud. Net zoals een bonenstaak snel groot en sterk kan worden, stelt Elastic Beanstalk ontwikkelaars in staat om snel en eenvoudig webapplicaties in de cloud te implementeren, beheren en schalen zonder zich zorgen te hoeven maken over de onderliggende infrastructuur.

## Key-terms


## Opdracht
### Gebruikte bronnen

https://www.hava.io/blog/what-is-aws-elastic-beanstalk

https://www.geeksforgeeks.org/introduction-to-aws-elastic-beanstalk/

https://aws.amazon.com/elasticbeanstalk/details/


### Ervaren problemen
Geen problemen ervaren

### Resultaat



Het gebruik van het Elastic Beanstalk-platform biedt de mogelijkheid om meer tijd te besteden aan het ontwikkelen en minder aan het beheer van het netwerk, de opslag, o/s en rekenruntimes, aangezien dit allemaal wordt afgehandeld door Elastic Beanstalk. Dit leidt tot een snellere implementatie, aangezien het enige dat nodig is, is om de code te bereiden, naar Elastic Beanstalk te voeren en het platform neemt het vanaf daar over.

Je hoeft geen tijd te besteden aan het selecteren van rekeninstances, database- en opslagvereisten, beveiliging, bewakingsservices, loadbalancing-resources, enzovoort, wat leidt tot een veel snellere implementatie. Jij zorgt voor de code en elastische bonenstaak doet de rest.

Na implementatie is de werking van de door Elastic Beanstalk gehoste applicaties ook eenvoudiger. Je hoeft niet langer de rol op je te nemen van het bewaken van servers, het bewaken van opslag, het beheren van netwerkbelastingen, het up-to-date houden van besturingssystemen, aangezien dit allemaal door het platform wordt geregeld.

Elastic beanstalk zorgt voor de automatische schaling van resources die nodig zijn om een geïmplementeerde applicatie te ondersteunen wanneer de vraag groeit of krimpt.

Wanneer Elastic Beanstalk een toepassing analyseert en de bronnen selecteert die nodig zijn, kan je ook ingrijpen en alternatieve bronnen selecteren die mogelijk beter geschikt zijn voor verwachte use-cases waarvan het misschien niet op de hoogte is.


### Elastic Beanstalk Components

#### Environment Tiers:

Er zijn twee tiers die worden geïnstantieerd wanneer je een applicatie implementeert via elastic beanstalk.

De **Web Server environment tier** is het naar voren gerichte segment dat reageert op http-verzoeken van gebruikers die toegang hebben tot de applicatie URL.

Een **Worker environment tier** is een achtergrondservice die verzoeken verwerkt die zijn gedelegeerd door de webserverlaag en die ook workloads kan uitvoeren die achtergrondtaken verwerken. Je kan code schrijven en die code implementeren in een _worker environment_ in plaats van in de hoofd werbserver applicatie.

#### Elastic Beanstalk Web Server Architecture:
Wanneer je een toepassing implementeert met behulp van _Elastic Beanstalk_ in een _webserver environment_, zal de _environment_ doorgaans de volgende architectuurstructuur creëren.

- **Elastic Beanstalk Environment**: Elastic Beanstalk environment is de container voor deze unieke versie van de applicatie en biedt een naam en URL-toegangspunt voor gebruikers om toegang te krijgen tot de applicatie.
- **Elastic Load Balancer**: Elastic Load Balancer verdeelt http-verzoeken naar de EC2-instances die binnen de _environment_ zijn ingericht.
- **Auto Scaling Group**: De Auto Scaling Group zal het aantal EC2-instances binnen de -environment_ in- en uitschalen op basis van verkeersbelasting. Je kunt specificeren met hoeveel EC2-instances je wilt beginnen en met hoeveel je de automatische scaler wilt laten instantiëren binnen de instellingen van de _elastic beanstalk environment_.
- **EC2 Instances**: De EC2-instances zijn de compute images die workloads uitvoeren. Elastic beanstalk stelt de grootte en het type EC2-instance voor, maar je kunt deze instancetypen handmatig wijzigen om de CPU-capaciteit en het gereserveerde geheugen te vergroten of te verkleinen, mocht je verwachten dat er meer of minder rekenkracht nodig is om acceptabele applicatieprestaties voor gebruikers te bieden.
- **Host Manager**: De hostmanager is aanwezig op elk van je EC2-instances en is verantwoordelijk voor het monitoren van en rapporteren over de prestaties van je applicatie, het rapporteren van gebeurtenissen op resource instanceniveau en het verzenden van logs naar je cloudwatch-dashboard.
- **Security Groups**: Er wordt een nieuwe _security group_ ingericht voor een _elastic beanstalk application environment_ die HTTP-toegang tot je applicatie mogelijk maakt via poort 80. Met behulp van het elastic beanstalk dashboard voor het wijzigen van instellingen kan je extra _security groups_ of een bestaande VPC aan je _web server environment_ toewijzen.

#### Elastic Beanstalk Worker Environment


Een _worker environment_ wordt gemaakt om specifieke achtergrondtaken te verwerken, maar wordt ook gemaakt om je webserver applicatie te helpen wanneer deze wordt belast.

Wanneer een webapplicatie een tijdrovende taak verwerkt als reactie op een gebruikersverzoek, als een tweede gebruiker een verzoek indient moet hij dan wachten, en bestaat de mogelijkheid dat er een time-out optreedt voor het verzoek.

Om dit probleem op te lossen, zal elastic beanstalk de gebruikersverzoeken doorgeven aan de _background worker environment_ die de verzoeken op een ordelijke manier in de wachtrij plaatst en verwerkt wanneer taken te veel tijd in beslag nemen op de webserver. Dit maakt de webserver vrij om meerdere verzoeken te accepteren zonder een time-out wanneer deze de verzoeken doorgeeft aan de "werker" voor verwerking.

#### How does the elastic beanstalk and web application and worker communicate?

Wanneer de webserver detecteert dat een verzoek te lang duurt, worden volgende verzoeken via een SQS-bericht doorgegeven aan een SQS-wachtrij. In de _worker environment_ wordt een daemon uitgevoerd die de SQS-wachtrij peilt en de SQS-berichten achtereenvolgens ophaalt voor verwerking. De _worker environment_ retourneert vervolgens http-antwoorden terug naar de client die het verzoek heeft gedaan.

#### Application:

Wanneer je een applicatie maakt, plaats je doorgaans alle gerelateerde activa, zoals code, resourceconfiguratiesjablonen, codeversies en vereiste bestanden in een map.

Een Elastic Beanstalk applicatie is een soortgelijk concept - het is de entiteit die alle gerelateerde bestanden, platformresources en configuratie-informatie bevat om de applicatie te ondersteunen wanneer je je applicatie implementeert via Elastic Beanstalk.

Als je een nieuwe applicatie of versie maakt en implementeert, wordt de applicatienaam weergegeven in de _elastic beanstalk console_.

#### Application Version:

Wanneer je wijzigingen aanbrengt in je applicatie, kan je de bijgewerkte applicatie implementeren via Elastic Beanstalk. De applicatieversie heeft betrekking op een specifiek gelabelde iteratie van implementeerbare code voor je webapplicatie.

Binnen elastic beanstalk is de applicatieversie een link naar een S3-object dat je inzetbare Zip- of Java WAR-bestand bevat.

De benoemde versie verschijnt als een nieuwe applicatie als je ervoor kiest om deze in een andere omgeving te implementeren in plaats van vanuit een bestaande applicatie.

#### Environments:


Wanneer je je applicatie implementeert met elastic beanstalk, wordt er een _environment_ gemaakt waarin de versie van de applicatie die je implementeert is ondergebracht. De _environment_ host de vereiste EC2-instances, opslag, load balancer, autoscaling-groepen of iets anders dat vereist is voor deze versie van de applicatie.

Een enkele _environment_ kan slechts één versie van je applicatie uitvoeren. Je kunt je nieuwe versie over een bestaande _application environment_ implementeren, zoals bijvoorbeeld productie, maar je hebt ook de flexibiliteit om te installeren in alternatieve _environments_ zoals ontwikkel-, staging- of testenvironments.

Elke environment heeft een unieke URL voor toegang tot de actieve applicatie.


#### Environment Health:


Elastic beanstalk bewaakt je webserver applicatie en _worker environments_ en voert _health checks_ uit op de werking van de applicatie.

De gezondheid van een _environment_ wordt gerapporteerd met behulp van kleurcodes voor onmiddellijke visuele herkenning dat alles in orde is of niet.


Grijs - laat je weten dat je environment wordt bijgewerkt of nog wordt ingericht.

Groen - Je environment is gezond en heeft de laatste _health check_ doorstaan.

Geel - Je omgeving heeft een of twee recente controles niet doorstaan

Rood - Je omgeving heeft drie of meer recente _health checks_ niet doorstaan.



