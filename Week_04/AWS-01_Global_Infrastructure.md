# AWS Global Infrastructure

**Amazon Web Services (AWS)** heeft een wereldwijde infrastructuur gebouwd die is ontworpen om klanten veilige, betrouwbare en krachtige _cloud computing_ diensten te bieden. De infrastructuur bestaat uit meerdere geografisch verspreide _Regions_, die elk meerdere _Availability Zones_ bevatten. Bovendien heeft AWS een netwerk van _edge locations_ die strategisch over de hele wereld zijn gelegen om de prestaties en beschikbaarheid van haar diensten te verbeteren. Door gebruik te maken van deze wereldwijde infrastructuur kunnen klanten hun applicaties en _services_ eenvoudig in meerdere regio's implementeren, terwijl ze profiteren van de hoge niveaus van schaalbaarheid, beschikbaarheid en fouttolerantie die AWS biedt.


## Key-terms

- **Redundancy**: Een systeemontwerp waarin een component wordt gedupliceerd, zodat er een back-up is als deze faalt.
- **Latency**: Hoe lang het duurt voordat gegevens reizen tussen de zender en de ontvanger - of tussen een specifieke gebruikersactie en het antwoord.

## Opdracht
### Gebruikte bronnen

ChatGPT

https://www.w3schools.com/aws/aws_cloudessentials_awsavailabilityzones.php

https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/RegionsAndAZs.html

https://www.rackspace.com/blog/aws-101-regions-availability-zones

https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/

https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/

### Ervaren problemen
Geen problemen ervaren.

### Resultaat

#### What is an AWS Availability Zone?

Een _Availability Zone_ is een logische datacenter in een region dat beschikbaar is voor gebruik door elke AWS-klant. Elke zone in een regio heeft redundante en gescheiden voeding, netwerken en connectiviteit om de kans te verkleinen dat twee zones tegelijkertijd uitvallen. In een _availability zone_ liggen de datacenters vele kilometers uit elkaar. Door ze uit elkaar te houden, verklein je het risico dat ze allemaal ten onder gaan als er zich een ramp voordoet in de regio. 

Een veel voorkomende misvatting is dat een enkele zone gelijk is aan een enkel datacenter. In feite wordt elke zone ondersteund door één of meer fysieke datacenters, waarbij de grootste wordt ondersteund door vijf. Hoewel een enkele beschikbaarheidszone meerdere datacenters kan omvatten, delen geen twee zones een datacenter.


#### What is a Region?

Een _AWS Region_ is een geografische locatie met een verzametling van _availability zones_ die toegewezen zijn aan fysieke datacenters in die regio. Elke regio is fyziek geïsoleerd en onafhankelijk van elke andere regio wat betreft locatie, stroomvoorziening, watervoorziening, enz. Dit isolatieniveau is van cruciaal belang voor _workloads_ met nalevings- en gegevenssoeveriniteitsvereisten waar er gegarandeerd moet worden dat gebruikersgegevens een bepaalde geografische regio niet verlaten. De aanwezigheid van _AWS regions_ wereldwijd is ook belangrijk voor woorkloads die latentiegevoelig zijn en zich in de buurt van gebruikers in een bepaal geografisch gebied moeten bevinden.


#### What is an Edge Location?

_Edge Locations_ zijn AWS datacenters die ontworpten zijn om _services_ te leveren met de laagst mogelijke latentie. Amazon heeft tientallen van deze datacenters verspreid over de hele wereld. Ze staan dichter bij gebruikers dan _Regions_ of _Availability Zones_, vaak in grote steden, dus reacties kunnen snel en krachtig zijn. 

Hoewel het primaire doel van _AWS Edge Locations_ is om _content_ met een _lage latentie_ te leveren, ze kunnen ook andere _resources_ en mogelijkheden bevatten die gebruikt worden om andere AWS services en functies te ondersteunen. Een subset van _services_ waarvoor latentie er echt toe doet maakt gebruik van _Edge Locations_,  waaronder:
  - CloudFront, die _edge locations_ gebruikt om kopieën van de _content_ die het uitdeelt op te slaan in de cache, zodat het dichter bij de gebruikers staat en sneller aan hen kan worden geleverd.
  - Route 53, die _DNS responses_ van _edge locations_ uitdeelt, zodat _DNS queries_ die in de buurt ontstaan sneller kunnen worden opgelost; en ook de belangrijkste database van Amazon is.
  - Web Application Firewall en AWS Shield, die verkeer op _edge locations_ filteren om ongewenst verkeer zo snel mogelijk te stoppen.



#### Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).

Er zijn vier belangrijke factoren die een role spelen bij het evalueren van elke _AWS Region_ voor een workloadimplementatie:

1. **Naleving**: Als een _workload_ gegevens bevat die gebonden zijn aan lokale regelgeving, heeft het selecteren van de regio die voldoet aan de regelgeving voorrang boven andere evaluatiefactoren. Dit is van toepassing op workloads die gebonden zijn aan wetgeving inzake _data residency_, waarbij het kiezen van een AWS Region in dat land verplicht is.

2. **Latentie**: Een belangrijke factor om rekening mee te houden voor de gebruikerservaring is _latentie_. Verminderde netwerklatentie kan substantiële invloed hebben op het verbetering van de gebruikerservaring. Het kiezen van een AWS Region dicht bij de locatie van een bepaalde gebruikersbestand kan een lagere netwerklatentie opleveren. Het kan ook de communicatiekwaliteit verbeteren, aangezien netwerkpakketten minder uitwisselingspunten hebben om doorheen te reizen.

3. **Kosten**: AWS services zijn per _Region_ anders geprijsd. Sommige regio's hebben lagere kosten dan andere, wat uit kan komen in een kostenverlaging voor dezelfde implementatie.

4. **Diensten en functies**: Nieuwe _services_ en _features_ worden geleidelijk in regio's geïmplementeerd. Hoewel alle AWS Regions dezelfde _Service Level Agreement_ (SLA) hebben, zijn sommige grotere regio's meestal de eersten die nieuwere diensten, functies en _software releases_ aanbieden. Kleinere regio's krijgen deze diensten of functies misschien niet snel genoeg zodat iemand ze kan gebruiken om hun werklast te ondersteunen.


Dus er moet overgewogen worden tussen deze vier factoren, waar _wetgeving_ het belangrijkste zal zijn, daarna _afstand_ voor latentie, en vervolgens _prijs/mogelijkheden_.
