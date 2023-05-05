# CloudFront
AWS CloudFront is een service van Amazon Web Services (AWS) die websites en webapplicaties helpt om content sneller en veiliger aan gebruikers te leveren. CloudFront slaat kopieën van website-inhoud op locaties over de hele wereld op, zodat gebruikers toegang hebben tot de inhoud vanaf een server die fysiek dichter bij hen staat. Dit helpt de tijd te verminderen die nodig is om een website of applicatie te laden en verbetert de algehele prestaties en gebruikerservaring. Bovendien biedt CloudFront een beveiligingslaag door de inhoud te versleutelen wanneer deze aan de gebruiker wordt geleverd. AWS CloudFront helpt website-eigenaren om snellere, betrouwbaardere en veiligere toegang tot hun inhoud te bieden aan gebruikers over de hele wereld.

## Key-terms

- **Content Delivery Network (CDN)**: Een geografisch gedistribueerde groep servers die content dicht bij eindgebruikers in de cache opslaat. Een CDN zorgt voor een snelle overdracht van activa die nodig zijn voor het laden van internetinhoud, waaronder HTML-pagina's, JavaScript-bestanden, stylesheets, afbeeldingen en video's. Hoewel een CDN geen inhoud host en de behoefte aan goede webhosting niet kan vervangen, helpt het wel bij het cachen van inhoud aan de rand van het netwerk, wat de prestaties van de website verbetert. Veel websites hebben moeite om aan hun prestatiebehoeften te voldoen door traditionele hostingdiensten, daarom kiezen ze voor CDN's. In de kern is een CDN een netwerk van aan elkaar gekoppelde servers met als doel content zo snel, goedkoop, betrouwbaar en veilig mogelijk te leveren. Om de snelheid en connectiviteit te verbeteren, plaatst een CDN servers op de uitwisselingspunten tussen verschillende netwerken.

- **Edge Locations**:  _Edge Locations_ zijn AWS datacenters die ontworpen zijn om _services_ te leveren met de laagst mogelijke latentie. Amazon heeft tientallen van deze datacenters verspreid over de hele wereld. Ze staan dichter bij gebruikers dan _Regions_ of _Availability Zones_, vaak in grote steden, dus reacties kunnen snel en krachtig zijn. Hoewel het primaire doel van _AWS Edge Locations_ is om _content_ met een _lage latentie_ te leveren, ze kunnen ook andere _resources_ en mogelijkheden bevatten die gebruikt worden om andere AWS services en functies te ondersteunen. Een subset van _services_ waarvoor latentie er echt toe doet maakt gebruik van _Edge Locations_,  waaronder:
  - **CloudFront**, die _edge locations_ gebruikt om kopieën van de _content_ die het uitdeelt op te slaan in de cache, zodat het dichter bij de gebruikers staat en sneller aan hen kan worden geleverd.
  - **Route 53**, die _DNS responses_ van _edge locations_ uitdeelt, zodat _DNS queries_ die in de buurt ontstaan sneller kunnen worden opgelost; en ook de belangrijkste database van Amazon is.
  - **Web Application Firewall en AWS Shield**, die verkeer op _edge locations_ filteren om ongewenst verkeer zo snel mogelijk te stoppen.

## Opdracht
### Gebruikte bronnen

https://medium.com/mindful-engineering/today-we-will-learn-about-cloudfront-690bf3a8819a

https://www.cloudflare.com/learning/cdn/what-is-a-cdn/

https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/

### Ervaren problemen
Geen problemen ervaren

### Resultaat

Amazon CloudFront is een _fast content delivery network_ (CDN) service die veilig data, video's, applicaties en API's levert aan klanten wereldwijd met lage latentie, hoge overdrachtssnelheden, allemaal binnen een ontwikkelaarsvriendelijke omgeving. Het versnelt de distributie van statische en dynamische webinhoud, zoals .html, .css, .js en afbeeldingsbestanden, naar gebruikers. CloudFront levert content via een wereldwijd netwerk van datacenters die edge-locaties worden genoemd.

Wanneer een gebruiker content opvraagt die je aanbiedt met CloudFront, wordt het verzoek doorgestuurd naar de edge-locatie die de laagste latentie (tijdsvertraging) biedt, zodat content wordt geleverd met de best mogelijke prestaties.

- Als de content zich al op de edge-locatie met de laagste latentie bevindt, levert CloudFront deze direct.
- Als de inhoud zich niet op die edge-locatie bevindt, haalt CloudFront deze op van een oorsprong die je hebt gedefinieerd, zoals een Amazon S3-bucket, een MediaPackage-kanaal of een HTTP-server (bijvoorbeeld een webserver) die je hebt geïdentificeerd als bron voor de definitieve versie van je inhoud.

Stel dat je een afbeelding aanbiedt vanaf een traditionele webserver, niet vanaf CloudFront. Je kunt bijvoorbeeld een afbeelding weergeven, sunsetphoto.png, met de URL http://example.com/sunsetphoto.png.

Je gebruikers kunnen eenvoudig naar deze URL navigeren en de afbeelding zien. Maar ze weten waarschijnlijk niet dat hun verzoek van het ene netwerk naar het andere wordt geleid - door de complexe verzameling onderling verbonden netwerken die het internet vormen - totdat de afbeelding is gevonden.


Je krijgt ook meer betrouwbaarheid en beschikbaarheid omdat kopieën van je bestanden (ook wel objecten genoemd) nu worden bewaard (of in de cache worden opgeslagen) op meerdere edge-locaties over de hele wereld.

Amazon CloudFront brengt automatisch de netwerkcondities in kaart en leidt het verkeer van gebruikers op intelligente wijze naar de meest performante AWS edge-locatie om gecachte of dynamische inhoud te serveren. CloudFront wordt standaard geleverd met een meerlaagse caching-architectuur die een verbeterde cachebreedte en herkomstbescherming biedt.



### Voordelen van het gebruik van een CDN


1) **Verbetering van de laadtijden van websites** - Door inhoud dichter bij de bezoekers van de website te verspreiden door gebruik te maken van een nabijgelegen CDN-server (naast andere optimalisaties), ervaren bezoekers snellere laadtijden van pagina's. Aangezien bezoekers meer geneigd zijn weg te klikken van een langzaam ladende site, kan een CDN de bouncepercentages verlagen en de hoeveelheid tijd die mensen op de site doorbrengen verhogen. Met andere woorden, een snellere website betekent dat meer bezoekers langer blijven en blijven.
2) **Verlaging van bandbreedtekosten** - Bandbreedteverbruikskosten voor websitehosting zijn een primaire kostenpost voor websites. Door caching en andere optimalisaties kunnen CDN's de hoeveelheid gegevens die een origin-server moet leveren verminderen, waardoor de hostingkosten voor website-eigenaren worden verlaagd.
3) **Verhogen van de beschikbaarheid en redundantie van inhoud** - Grote hoeveelheden verkeer of hardwarestoringen kunnen de normale websitefunctie onderbreken. Dankzij hun gedistribueerde aard kan een CDN meer verkeer aan en is het beter bestand tegen hardwarestoringen dan veel oorspronkelijke servers.
4) **Verbetering van de websitebeveiliging** - Een CDN kan de beveiliging verbeteren door DDoS-mitigatie, verbeteringen aan beveiligingscertificaten en andere optimalisaties te bieden.


#### 1) Latency

Hoe verbetert een CDN de laadtijden van websites?



- Het wereldwijd gedistribueerde karakter van een CDN betekent dat de afstand tussen gebruikers en websitebronnen wordt verkleind. In plaats van verbinding te moeten maken met waar de oorspronkelijke server van een website zich bevindt, kunnen gebruikers met een CDN verbinding maken met een geografisch dichterbij gelegen datacenter. Minder reistijd betekent snellere service.
- Hardware- en software-optimalisaties, zoals efficiënte taakverdeling en solid-state harde schijven, kunnen ervoor zorgen dat gegevens de gebruiker sneller bereiken.
- CDN's kunnen de hoeveelheid gegevens die wordt overgedragen verminderen door de bestandsgrootte te verkleinen met behulp van tactieken zoals verkleining en bestandscompressie. Kleinere bestandsgroottes betekenen snellere laadtijden.
- CDN's kunnen ook sites versnellen die TLS/SSL-certificaten gebruiken door hergebruik van verbindingen te optimaliseren en valse start van TLS mogelijk te maken.

#### 2) Cost

Hoe kan het gebruik van een CDN de bandbreedtekosten verlagen?

- Een content delivery network (CDN) verlaagt de kosten van gegevensoverdracht omdat het zich tussen gebruikers en de hostingservers van de website bevindt, of oorsprongservers, waardoor het verkeer tussen de hostingservers en de rest van internet afneemt. Een CDN is een netwerk van servers verspreid over de hele wereld die inhoud dichter bij eindgebruikers opslaan, waardoor latentie wordt verminderd. CDN's bieden inhoud in de cache aan, zodat de oorspronkelijke servers niet steeds dezelfde inhoud hoeven te leveren.
- Webhostingservices brengen kosten in rekening voor de gegevens die van of naar de oorspronkelijke server worden verzonden (dit wordt vaak "bandbreedte" genoemd). Maar als de meeste inhoud van een website in de cache is opgeslagen in een CDN, hoeven er veel minder gegevens van en naar de hostserver van de website te worden overgebracht, wat resulteert in lagere bandbreedtekosten.

#### 3) Reliability and redundancy

Hoe houdt een CDN een website altijd online?

Uptime is een cruciaal onderdeel voor iedereen met een interneteigendom. Hardwarestoringen en pieken in het verkeer, als gevolg van kwaadwillende aanvallen of gewoon een toename in populariteit, hebben de potentie om een webserver neer te halen en te voorkomen dat gebruikers toegang krijgen tot een site of service. Een goed afgerond CDN heeft verschillende functies die downtime minimaliseren:

- **Loadbalancing** verdeelt het netwerkverkeer gelijkmatig over verschillende servers, waardoor het gemakkelijker wordt om snelle toenames in het verkeer op te schalen.
- **Intelligent failover** zorgt voor een ononderbroken service, zelfs als een of meer van de CDN-servers offline gaan als gevolg van hardwarestoringen; de failover kan het verkeer herverdelen naar de andere operationele servers.
- In het geval dat een heel datacenter technische problemen heeft, stuurt _Anycast_ routering het verkeer naar een ander beschikbaar datacenter, zodat geen enkele gebruiker de toegang tot de website verliest.

#### 4) Data security
Hoe beschermt een CDN gegevens?

Informatiebeveiliging is een integraal onderdeel van een CDN. Een CDN kan een site beveiligd houden met nieuwe TLS/SSL-certificaten die een hoge standaard van authenticatie, codering en integriteit garanderen. Een correct geconfigureerd CDN kan ook helpen websites te beschermen tegen enkele veelvoorkomende kwaadaardige aanvallen, zoals Distributed Denial of Service (DDOS)-aanvallen.
