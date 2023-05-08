# Route 53
De wereldwijde infrastructuur die het Domain Name System (DNS) wordt genoemd, vertaalt door mensen leesbare hostnamen in numerieke IP-adressen. IP-adressen in de cloud kunnen regelmatig veranderen, omdat services tussen datacenters en fysieke machines worden verplaatst. Dit betekent dat het vertaal- en communicatieproces complex is.

Organisaties die machines in de cloud laten draaien met Amazon Web Services (AWS) hebben een AWS DNS-oplossing nodig: een manier om gebruikersverzoeken correct te vertalen naar Amazon IP-adressen, zich aan te passen aan cloudveranderingen en deze snel door te geven aan DNS-clients.

AWS Route 53 is de officiële DNS-oplossing van Amazon. Het volgende proces vindt plaats wanneer een gebruiker toegang krijgt tot een webserver via Route 53 DNS:

1. Een gebruiker opent een adres dat wordt beheerd door Route 53, www.website.com, dat naar een door AWS gehoste machine leidt.
2. Meestal beheerd door het lokale netwerk of ISP, ontvangt de DNS-resolver van de gebruiker het verzoek voor www.website.com gerouteerd door AWS Route 53 en stuurt het door naar een DNS-rootserver.
3. De DNS-resolver stuurt de TLD-naamservers door voor ".com"-domeinen die de gebruiker aanvraagt.
4. De resolver verwerft de vier gezaghebbende Amazon Route 53-naamservers die de DNS-zone van het domein hosten.
5. De DNS-resolver selecteert een van de vier AWS Route 53-servers en vraagt details op voor www.website.com.
6. De Route 53-nameserver zoekt in de DNS-zone naar het www.website.com IP-adres en andere relevante informatie en stuurt deze terug naar de DNS-resolver.
7. Zoals gespecificeerd door de Time to Live (TTL) parameter, slaat de DNS-resolver het IP-adres lokaal op in de cache en stuurt het natuurlijk terug naar de webbrowser van de gebruiker.
8. De browser gebruikt het IP-adres dat de resolver verstrekt om contact op te nemen met door Amazon gehoste services, zoals de webserver.
9. De webbrowser van de gebruiker geeft de website weer.

## Key-terms

- **Domain Name System (DNS)**: Een naamgevingsdatabase waarin internetdomeinnamen worden opgespoord en vertaald naar Internet Protocol (IP)-adressen. Het domeinnaamsysteem koppelt de naam die mensen gebruiken om een website te vinden aan het IP-adres dat een computer gebruikt om die website te vinden.

## Opdracht
### Gebruikte bronnen

https://intellipaat.com/blog/what-is-aws-route53/

https://avinetworks.com/glossary/aws-route-53/

https://blog.runcloud.io/cloudflare-vs-route-53/

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html

### Ervaren problemen
Geen problemen ervaren

### Resultaat

AWS Route 53 is bedoeld voor het beheer van DNS voor services en machines die zijn geïmplementeerd in de openbare cloud van Amazon. De AWS Route 53 DNS-service verbindt gebruikersverzoeken met ELB-loadbalancers, Amazon EC2-instanties, Amazon S3-buckets en andere infrastructuur die op AWS draait.

Route 53 biedt de gebruiker verschillende voordelen:

- **Highly Available and Reliable**: AWS Route 53 is gebouwd met behulp van de zeer beschikbare en betrouwbare infrastructuur van AWS. DNS-servers zijn verdeeld over veel beschikbaarheidszones, wat helpt bij het consistent routeren van eindgebruikers naar uw website. Amazon Route 53 Traffic Flow-service helpt de betrouwbaarheid te verbeteren met eenvoudige herrouteringsconfiguratie wanneer het systeem uitvalt.
- **Flexible**: Route 53 Traffic Flow biedt gebruikers flexibiliteit bij het kiezen van verkeersbeleid op basis van meerdere criteria, zoals eindpuntgezondheid, geografische locatie en latentie.
- **Simple**: DNS queries worden binnen enkele minuten na installatie beantwoord door Route 53 in AWS, en het is een selfservice-aanmelding. Je kunt ook de eenvoudige AWS Route 53 API gebruiken en deze ook in je webtoepassing insluiten.
- **Fast**: Gedistribueerde Route 53 DNS-servers over de hele wereld vormen een service met lage latentie. Omdat ze gebruikers naar de dichtstbijzijnde beschikbare DNS-server leiden.
- **Cost-effective**: Je betaalt alleen voor wat je gebruikt, bijvoorbeeld de gehoste zones die je domeinen beheren, het aantal vragen dat per domein wordt beantwoord, enz. Ook optionele functies zoals verkeersbeleid en gezondheidscontroles zijn beschikbaar tegen zeer lage kosten.
- **Designed to Integrate with Other AWS Services**: Route 53 werkt heel goed met andere services zoals Amazon EC2 en Amazon S3. Je kunt Route 53 bijvoorbeeld gebruiken om domeinnamen of IP-adressen toe te wijzen aan EC2-instances en Amazon S3-buckets.
- **Secure**: U kunt met uw AWS-account unieke inloggegevens en machtigingen maken en toekennen aan elke gebruiker, terwijl u moet vermelden wie toegang heeft tot welke onderdelen van de service.
- **Scalable**: Amazon Route 53 is ontworpen om automatisch omhoog of omlaag te schalen wanneer de grootte van het queryvolume varieert.

 

### Belangrijkste voordelen en functies van Amazon Route 53

- **AWS service integration**: Het is duidelijk dat de nauwe integratie van AWS Route 53 met CloudFront, S3 en ELB betekent dat het eenvoudig is om verkeer naar een statische website te leiden die wordt gehost op S3 of een ELB CNAME-record, of om aangepaste domeinen te genereren voor CloudFront-URL's.
- **Simple routing policy**: Het eenvoudigste en meest voorkomende routeringstype, dit beleid gebruikt alleen AWS Route 53 om je sitenaam aan je IP toe te wijzen. Alle toekomstige browserverzoeken voor die sitenaam zouden dan naar het juiste IP-adres worden geleid.
- **Alias records**: Een _alias resource record_ kan rechtstreeks verwijzen naar andere _resource records_ in plaats van naar een IP-adres, zoals een ELB-loadbalancer, een CloudFront-distributie of een Amazon S3-bucket. Dit zorgt ervoor dat verkeer naar het juiste eindpunt wordt gestuurd, zelfs als de IP-adressen van de onderliggende bronnen veranderen.
- **Amazon Route 53 failover**: In het geval van een storing, zoals bepaald door gezondheidscontroles, leidt een Amazon Route 53-failoverbeleid gebruikers automatisch om naar een aangewezen back-up resource of alternatieve service.
- **Domain registration**: AWS fungeert als domeinregistreerder, waardoor gebruikers domeinnamen van alle topniveaudomeinen (.com, .net, .org, enz.) kunnen selecteren en registreren met de AWS-beheerconsole. Dit voorkomt de noodzaak om te migreren en stelt de Route 53-registrar in staat om gratis privacybescherming te bieden voor het WHOIS-record.
- **Geo DNS**: Afhankelijk van de gedetecteerde geografische locatie van de gebruiker, leidt dit beleid gebruikers naar eindpunten op basis van toegewezen resourcedoelen. Om latentie te beperken, wil je bijvoorbeeld dat alle query's van één regio worden doorgestuurd naar een server die zich in dezelfde fysieke regio bevindt.
- **Health checks**: AWS Route 53 voert gezondheidscontroles uit en bewaakt de gezondheid en prestaties van applicaties. Wanneer het een storing detecteert, leidt Amazon Route 53 gebruikers om naar een gezonde resource.
- **Latency-based routing**: Een op latentie gebaseerd beleid leidt gebruikers en verkeer naar de AWS-regio met de laagste latentie.
- **Private DNS**: Definieert _custom_ domeinnamen terwijl DNS-informatie privé blijft voor Amazon VPC-gebruikers. Met privé-DNS-records kun je eenvoudig verkeer routeren met behulp van domeinnamen die binnen je VPC's worden beheerd en privé gehoste zones creëren. Hierdoor kan je bijvoorbeeld snel schakelen tussen op IP gebaseerde resources  zonder meerdere ingesloten links bij te werken.
- **Traffic flow**: Routeert endpointverkeer op basis van de beste gebruikerservaring.
- **Weighted round-robin load balancing**: Gebruikt een round-robin-algoritme om verkeer over meerdere services te spreiden. Door de meerdere servers waaruit een webservice bestaat verschillende numerieke prioriteiten of gewichten toe te wijzen, kan je een lager of hoger percentage van inkomend verkeer naar een bepaalde server leiden. Dit soort routering kan handig zijn voor het testen van nieuwe versies van een softwarepakket en loadbalancing.
