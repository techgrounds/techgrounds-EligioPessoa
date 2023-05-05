# Well Architected Framework
Het AWS Well-Architected Framework helpt men de voor- en nadelen te begrijpen van beslissingen die genomen worden bij het bouwen van systemen op AWS. Door het Framework te gebruiken, leert men _best practices_ op het gebied van architectuur voor het ontwerpen en gebruiken van veilige, betrouwbare, efficiënte, kosteneffectieve en duurzame workloads in de AWS Cloud. Het biedt een manier om architecturen consistent te meten aan de hand van best practices en verbeterpunten te identificeren. Het proces voor het beoordelen van een architectuur is een constructief gesprek over architectuurbeslissingen en is geen auditmechanisme.

Het AWS Well-Architected Framework documenteert een reeks fundamentele vragen die mensen helpen te begrijpen of een specifieke architectuur goed aansluit bij best practices voor de cloud. Het _framework_ biedt een consistente benadering voor het evalueren van systemen aan de hand van de kwaliteiten die verwacht worden van moderne cloudgebaseerde systemen, en het herstel dat nodig zou zijn om die kwaliteiten te bereiken.

Dit _framework_ is bedoeld voor mensen in technologierollen, zoals chief technology officers (CTO's), architecten, ontwikkelaars en leden van het operationele team. Het beschrijft best practices en strategieën voor AWS die kunnen worden gebruikt bij het ontwerpen en gebruiken van een cloudworkload, en biedt koppelingen naar verdere implementatiedetails en architecturale patronen.

Naarmate AWS zich blijft ontwikkelen en steeds meer leert van de samenwerking met hun klanten, zullen ze de definitie van _Well Architected_ blijven verfijnen.


## Key-terms

- **AWS Well-Architected Tool (AWS WA Tool)**: is een service in de cloud die een consistent proces biedt voor het meten van architectuur met behulp van AWS best practices. AWS WA Tool helpt men gedurende de levenscyclus van het product door:

  - Assisteren bij het documenteren van genomen beslissingen.

  - Aanbevelingen doen om werklast te verbeteren op basis van best practices

  - AWS begeleidt hun klanten bij het betrouwbaarder, veiliger, efficiënter en kosteneffectiever maken van hun workloads



## Opdracht
### Gebruikte bronnen

https://molecularsciences.org/content/aws-well-architected-framework-in-a-nutshell/

https://aws.amazon.com/architecture/well-architected/

https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html

https://medium.com/@avinash90006/summary-on-aws-well-architected-framework-60adf14b76b5


### Ervaren problemen
Geen problemen ervaren

### Resultaat

Amazon definieert AWS Well-Architected Framework als een _framework_ dat "_key concepts_, _design principles_ en _architectural best practices_ beschrijft voor het ontwerpen en uitvoeren van workload in de cloud". Het framework schetst eenvoudig hoe men infrastructuur moet ontwerpen en beheren. Het framework is gebaseerd op vijf _pillars_:

- **Operational Excellence**:
  - Verbeter continu processen, procedures, monitoring en ontwikkelingsondersteuning om een efficiënte uitvoering van workloads te garanderen.
- **Security**:
  - Cloudmogelijkheden gebruiken om gegevens en systemen beter te beschermen.
- **Reliability**:
  - De werklast wordt correct en consistent uitgevoerd.
  - Mensen zijn in staat om de workload gedurende de hele levenscyclus te bedienen en te testen.
- **Performance Efficiency**:
  - Gebruik computerbronnen efficiënt.
- **Cost Optimization**:
  - Voer systemen uit tegen de laagste prijs.
- **Sustainability**:
  - Minimaliseer de milieu-impact van het uitvoeren van cloudworkloads

Het _framework_ beveelt best practices aan voor elke pijler:


### Operational Excellence

Verbeter continu processen, procedures, monitoring en ontwikkelingsondersteuning om een efficiënte uitvoering van workloads te garanderen.

**Design Principles**


- Codeer handelingen in plaats van ze handmatig uit te voeren
- Breng in plaats van een paar grote veranderingen aan, regelmatig kleine en omkeerbare veranderingen aan
- Verfijn procedures voor operaties regelmatig
- Plan voor falen
- Leer van operationele mislukkingen


**Best Practice Areas**

- **Organization**: Teams moeten hun werklast en hun belang van het begrijpen van hun rollen verdelen om hun zakelijke doelen te bereiken.
- **Prepare**: ontwerp workloads zodanig dat ze de informatie bieden die nodig is voor alle componenten, zodat men de interne status ervan kunt begrijpen. Dit stelt men in staat om waar nodig effectieve antwoorden te geven.
- **Operate**: de focus ligt hier op het begrijpen van de gezondheid van workloads en operaties. Definieer, leg vast en analyseer werklast-/operationele statistieken om zichtbaarheid te krijgen. Hierdoor kan men de juiste actie ondernemen.
- **Evolve**: de belangrijkste focus ligt op het besteden van tijd en middelen voor continue verbeteringen om operaties te ontwikkelen.




### Security:
Cloudmogelijkheden gebruiken om gegevens, bedrijfsmiddelen en systemen beter te beschermen.

**Design Principles**


- Implementeer sterke identiteit en authenticatie
- Schakel traceerbaarheid in
- Beveiliging toepassen op elke laag van de architectuur
- Automatiseer best practices voor beveiliging
- Bescherm data in rust en onderweg
- Houd mensen uit de buurt van gegevens
- Wees voorbereid op beveiligingsincidenten


**Best Practice Areas**


- Security: Voer de _workload_ veilig uit door best practices toe te passen op elk beveiligingsgebied. Neem vereisten en processen die je hebt gedefinieerd in _Operational Exceleence_ op organisatie- en workload niveau en pas ze toe op alle gebieden
- Identity and Access Management: Om AWS-workloads veilig uit te voeren, zijn er twee soorten identiteiten die beheerd moeten worden. Het begrijpen van het type identiteit dat nodig is om te beheren en toegang te verlenen zorgt ervoor dat de juiste identiteiten onder de juiste voorwaarden toegang hebben tot de juiste _resources_.
- Detection: In AWS kunnen detectivecontroles geïmplementeerd worden met behulp van CloudTrail-logboeken, AWS API-aanroepen, CloudWatch. Ze bieden monitoringstatistieken met alarmen en logboeken die ons helpen bij het monitoren van kwaadaardig of ongeoorloofd gedrag. Logboekbeheer is om vele redenen belangrijk voor een goed ontworpen _workload_, variërend van beveiliging of forensisch onderzoek tot wettelijke of wettelijke vereisten.
- Infrastructure Protection: Meerdere verdedigingslagen helpen te beschermen tegen externe en interne netwerkbedreigingen. Mensen kunnen bijvoorbeeld AWS VPC gebruiken om een besloten, beveiligde en schaalbare omgeving te creëren waarin de topologie gedefinieerd kan worden, inclusief gateways, routeringstabellen en _public_ en _private_ subnetten.
- Data Protection: Voordat iemand een systeem ontwerpt, moeten ze een solide plan hebben om gegevens te beschermen. AWS biedt veel faciliteiten om gegevens te beschermen terwijl ze _at rest_ en _in transit_ zijn. Ze hebben bijvoorbeeld server-side encryptie voor AWS S3 om het voor makkelijker te maken om gegevens in een gecodeerde vorm op te slaan. Men kan er ook voor zorgen dat het volledige HTTPS-coderings- en decoderingsproces door ELB wordt afgehandeld. (AKA. Implementatie van meerdere controles om het risico van ongeautoriseerde toegang, verlies of verkeerd gebruik te verminderen.)
- Incident Response: De architectuur van een workload heeft een sterke invloed op het vermogen van een team om effectief te opereren tijdens een incident, om systemen te isoleren of in te dammen en om operaties te herstellen naar een bekende goede staat. Door voorafgaand aan een beveiligingsincident toegang en tools in te voeren en vervolgens tijdens _game days_ routinematig incidentrespons te oefenen, kan ervoor gezorgd worden dat de architectuur geschikt is voor tijdig onderzoek en herstel.




### Reliability:
De _workload_ wordt correct en consistent uitgevoerd. Men is in staat om de workload gedurende de hele levenscyclus te bedienen en te testen.

**Design Principles**
- Automatisch herstellen van een storing
- Herstelprocedures testen
- Horizontaal schalen om de totale beschikbaarheid van workloads te vergroten
- Stop met raden naar capaciteit
- Veranderingen in de automatisering beheren

**Best Practices**

- Foundations: Fundamentele vereisten zijn vereisten waarvan de reikwijdte verder reikt dan een enkele workload of project. Voordat er systemen worden ontworpen, moeten er fundamentele vereisten zijn die van invloed zijn op de betrouwbaarheid. Er moet bijvoorbeeld voldoende netwerkbandbreedte zijn naar een datacenter.
- Workload Architecture: Een betrouwbare workload begint met een vooraf ontworpen ontwerp voor zowel software als infrastructuur. De architectuurkeuze heeft invloed op he workload gedrag voor alle zes _Well Architected Pillars_.
- Change Management: Veranderingen in de workload of de omgeving ervan moeten worden geanticipeerd en aangepast om een betrouwbare werking van de werklast te bereiken. Men kan het gedrag van een werklast monitoren en de reactie op KPI's automatiseren. De workload kan bijvoorbeeld extra servers toevoegen naarmate een workload meer gebruikers krijgt. Er kan bepaald worden wie toestemming heeft om wijzigingen in de werkbelasting aan te brengen en de geschiedenis van deze wijzigingen controleren.
- Failure Management: Workloads must be able to both withstand failures and automatically repair issues. With AWS, you can take advantage to react to monitoring data. For example, when a particular metric crosses a threshold, you can trigger an automated action to remedy the problem.
Workloads moeten bestand zijn tegen storingen en automatisch problemen kunnen oplossen. Met AWS kan men reageren op monitoringgegevens. Wanneer een bepaalde statistiek bijvoorbeeld een drempel overschrijdt, kan een geautomatiseerde actie geactivereerd worden om het probleem op te lossen.

### Performance Efficiency:
Gebruik computerresources efficiënt om aan systeemvereisten te voldoen en om die efficiëntie te behouden naarmate de vraag verandert en technologieën evolueren.

**Design Principles**

- Democratiseer geavanceerde technologieën
- Ga binnen enkele minuten wereldwijd
- Gebruik serverloze architectuur
- Experimenteer vaker
- Overweeg mechanische sympathie

**Best Practices**

- Selection: Vaak zijn meerdere benaderingen vereist voor optimale prestaties binnen een werkbelasting. Goed ontworpen systemen gebruiken meerdere oplossingen en functies om de prestaties te verbeteren. Een beheerde service zoals AWS DynamoDB biedt bijvoorbeeld een volledig beheerde NoSQL-database met latentie van enkele milliseconden op elke schaal.
- Compute: De optimale rekenoplossing voor een workload varieert op basis van applicatieontwerp, gebruikspatronen en configuratie-instellingen. Compute in AWS is beschikbaar in 3 vormen, zoals _instances_, _containers_ en _functies_.
- Storage: De optimale opslagoplossing voor een systeem varieert op basis van het type toegangsmethode (blok, bestand of object), toegangspatronen (willekeurig, sequentieel), vereiste doorvoer, toegangsfrequentie (offline, online) en meer factoren. Opslag in AWS is beschikbaar in 3 vormen zoals objecten, blokken, bestanden.
- Database: De optimale databaseoplossing voor een systeem varieert op basis van vereisten voor beschikbaarheid, consistentie, partitietolerantie, latentie, duurzaamheid, schaalbaarheid en querymogelijkheden. Het selecteren van de verkeerde databaseoplossing en -functies voor een systeem kan leiden tot lagere prestatie-efficiëntie.
- Network: De optimale netwerkoplossing voor een workload varieert op basis van latentie, doorvoervereisten, jitter en bandbreedte. Fysieke beperkingen, zoals gebruikers- of on-premises resources, bepalen de locatie-opties. Deze beperkingen kunnen worden gecompenseerd met edge-locaties of plaatsing van resources.
- Review: Cloudtechnologieën evolueren snel en er moet ervoor gezorgd worden dat workloadcomponenten de nieuwste technologieën en benaderingen gebruiken om de prestaties voortdurend te verbeteren. Men moet voortdurend wijzigingen in workloadcomponenten evalueren en overwegen om ervoor te zorgen dat er aan de prestatie- en kostendoelstellingen volgedaan wordt.
- Monitoring: De systeemprestaties kunnen na verloop van tijd afnemen. Bewaak de systeemprestaties om degradatie te identificeren en interne of externe factoren te verhelpen, zoals de belasting van het besturingssysteem of de applicatie.
- Tradeoffs: Bij het ontwerpen van oplossingen stelt het bepalen van afwegingen men in staat om een optimale benadering te kiezen. Vaak kunnen de prestaties verbeterd worden door consistentie, duurzaamheid en ruimte in te ruilen voor tijd en latentie.

### Cost Optimization:
Run systemen om bedrijfswaarde te leveren tegen de laagste prijs.

**Design Principles**

- Implementeer cloud financieel beheer
- Pas een consumptiemodel toe
- Meet de algehele efficiëntie
- Stop met geld uitgeven aan ongedifferentieerd _heavy lifting_
- Uitgaven analyseren en toeschrijven

**Best Practices**

- Practice Cloud Financial Management: Door Cloud Financial Management te implementeren, kunnen organisaties bedrijfswaarde en financieel succes realiseren door hun kosten en gebruik te optimaliseren en te schalen op AWS.
- Expenditure and usage awareness: Veel bedrijven bestaan uit meerdere systemen die door verschillende teams worden beheerd. De mogelijkheid om resourcekosten toe te schrijven aan de individuele organisatie of producteigenaren stimuleert efficiënt gebruiksgedrag en helpt verspilling tegen te gaan. Nauwkeurige kostentoerekening stelt men in staat om te weten welke producten echt winstgevend zijn en om beter geïnformeerde beslissingen te nemen over waar het budget aan wordt toegewezen. In AWS creër je een accountstructuur met AWS Organizations of AWS Control Tower, die zorgt voor scheiding en helpt bij de toewijzing van kosten en gebruik.
- Cost-effective resources: Een goed ontworpen workload maakt gebruik van de meest kosteneffectieve resources, wat een aanzienlijke en positieve economische impact kan hebben. Het gebruik van de juiste instances en resources voor de workload is _key_ tot kostenbesparingen. Een rapportageproces kan bijvoorbeeld vijf uur duren om te draaien op een kleinere server, maar een uur om te draaien op een grotere server die twee keer zo duur is. Beide servers geven hetzelfde resultaat, maar de kleinere server brengt na verloop van tijd meer kosten met zich mee
- Manage demand and supply resources: Wanneer je naar de cloud overstapt, betaal je alleen voor wat je nodig hebt. Je kunt resources leveren die passen bij de vraag naar workload op het moment dat ze nodig zijn, waardoor kostbare en verspillende overprovisioning overbodig wordt. Voor een werklast met evenwichtige uitgaven en prestaties, moet u ervoor zorgen dat alles waarvoor u betaalt, wordt gebruikt en vermijdt u aanzienlijk onderbenutte instanties.
- Optimize over time: Het implementeren van nieuwe functies of resourcetypen kan de workload stapsgewijs optimaliseren, terwijl de inspanning die nodig is om de wijziging door te voeren, wordt geminimaliseerd. Dit zorgt voor voortdurende verbeteringen in efficiëntie in de loop van de tijd en zorgt ervoor dat men op de meest recente technologie blijft om de bedrijfskosten te verlagen.

### Sustainability:
Minimaliseer de milieu-impact van het uitvoeren van cloudworkloads

**Design Principles**

- Begrijp je impact
- Vaststellen van duurzaamheidsdoelen
- Maximaliseer het gebruik
- Anticiperen op en adopteren van nieuwe, efficiëntere hardware- en softwareaanbiedingen
- Gebruik beheerde services
- Verminder de downstream-impact van cloudworkloads

**Best Practices**

- Region selection: De keuze van de regio voor de workload heeft een aanzienlijke invloed op de KPI's, waaronder prestaties, kosten en CO2-voetafdruk. Om deze KPI's effectief te verbeteren, moet men Regio's kiezen voor de workloads op basis van zowel zakelijke vereisten als duurzaamheidsdoelen.
- Alignment to demand: De manier waarop gebruikers en applicaties workloads en andere bronnen gebruiken, kan helpen verbeteringen te identificeren om duurzaamheidsdoelen te bereiken. Schaal de infrastructuur om voortdurend aan de vraag te voldoen en verifieer dat er alleen de minimale middelen gebruikt worden die nodig zijn om gebruikers te ondersteunen. Stem serviceniveaus af op de behoeften van de klant. Positioneer bronnen om het netwerk te beperken dat nodig is voor gebruikers en applicaties om ze te gebruiken. Verwijder ongebruikte activa. Voorzie teamleden van apparaten die hun behoeften ondersteunen en hun impact op de duurzaamheid minimaliseren.
- Software and architecture: Implementeer patronen voor het afvlakken van de belasting en het handhaven van een consistent hoog gebruik van geïmplementeerde bronnen om de verbruikte bronnen te minimaliseren. Componenten kunnen inactief worden door gebrek aan gebruik vanwege veranderingen in gebruikersgedrag in de loop van de tijd. Herzie patronen en architectuur om onderbenutte componenten te consolideren om het algehele gebruik te vergroten. Verwijder componenten die niet langer nodig zijn. Krijg inzicht in de prestaties van workloadcomponenten en optimaliseer de componenten die de meeste resources verbruiken. Wees bewust van de apparaten die klanten gebruiken om toegang te krijgen tot services en implementeer patronen om de noodzaak van apparaatupgrades te minimaliseren.
- Data: Implementeer praktijken voor gegevensbeheer om de ingerichte opslag die nodig is om de workload te ondersteunen, en de middelen die nodig zijn om deze te gebruiken, te verminderen. Krijg inzicht in je gegevens en gebruik opslagtechnologieën en -configuraties die de zakelijke waarde van de gegevens en de manier waarop deze worden gebruikt, het beste ondersteunen. Bepaal het Levenscyclus van gegevens naar efficiëntere, minder performante opslag wanneer de vereisten afnemen, en verwijder gegevens die niet langer nodig zijn.
- Hardware and services: Zoek naar mogelijkheden om de impact van de duurzaamheid van de workload te verminderen door wijzigingen aan te brengen in je hardwarebeheerpraktijken. Minimaliseer de hoeveelheid hardware die nodig is om in te richten en te implementeren, en selecteer de meest efficiënte hardware en services voor je individuele workload.
- Process and culture: Zoek naar mogelijkheden om impact op duurzaamheid te verminderen door wijzigingen aan te brengen in ontwikkelings-, test- en implementatiepraktijken.

