Voor het project die ik uitgevoerd heb, de volgende eisen zijn aangegeven:










| **User story** | **Als klant wil ik weten hoe ik de applicatie kan gebruiken** |
| -------------- | -------------------------------| 
| **Epic** | v1.0 |
| **Beschrijving** | Zorg dat de klant kan begrijpen hoe deze de applicatie kan gebruiken. Zorg dat het duidelijk is wat de klant moet configureren voor de deployment kan starten en welke argumenten het programma nodig heeft. |
| **Deliverable** | Documentatie voor het gebruik van de applicatie |


| **User story** | **Als klant wil ik een MVP kunnen deployen om te testen** |
| -------------- | -------------------------------| 
| **Epic** | v1.0 |
| **Beschrijving** | De klant wil zelf intern je architectuur testen voordat ze de code gaan gebruiken in productie. Zorg ervoor dat er configuratie beschikbaar is waarmee de klant een MVP kan deployen. |
| **Deliverable** | Configuratie voor een MVP deployment |
















De volgende eisen zijn aangegeven als noodzakelijk:



De webserver moet op een geautomatiseerde manier geïnstalleerd worden.
De admin/management server moet bereikbaar zijn met een publiek IP.
De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis)
De volgende IP ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24
Alle subnets moeten beschermd worden door een firewall op subnet niveau.
SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server.



# Netwerk

| **User story** | **Als klant wil ik een werkende applicatie hebben waarmee ik een veilig netwerk kan deployen** | 
| -------------- | ------------------------------------------------------------------------------ | 
| **Epic** | v1.0 |
| **Beschrijving** | De applicatie moet een netwerk opbouwen dat aan alle eisen voldoet. Een voorbeeld van een genoemde eis is dat alleen verkeer van trusted sources de management server mag benaderen. |
| **Deliverable** | IaC-code voor het netwerk en alle onderdelen | 


2 VPC's moeten worden aangemaakt. Één voor productie omgeving, andere voor administratie/management omgeving. 
- De reden om 2 VPC's te maken is om te zorgen dat de omgevingen apart van elkaar zijn, waardoor ze veiliger zijn. 
- In de oorspronkelijke schema werd gevraagd om de VPC's in 2 aparte regio's te bouwen. Uit discussie is gebleken dat dat meer kostbaar is, en de veiligheid en stabiliteitsvoordelen dat het zou brengen niet te relevant zijn.
- Elke VPC dient 2 availability zones te hebben, met een subnet in elke AZ. In het geval van de management vpc, zal die als backup dienen in het geval van uitval van de hoofdmanagement server en availability zone. In het geval van de applicatie productie VPC, omdat er piekverkeer momenten kunnen zijn, zullen er extra availability zones zijn om te zorgen dat er extra EC2 instances gecreërd kunnen worden door middel van een auto-scaler, met natuurlijk een load balancer om de load te balanceren tussen die instances. Uitzoeken of er ook meerdere availability zones beschikbaar gesteld kunnen worden voor de webserver.<----------------------
- Om verbinding te maken tussen de twee VPC's wordt een VPC peering connection gebruikt. Uit kostoverwegingen lijkt het verstandig om te zorgen dat de services die altijd aan zullen zijn op dezelfde availability zone zitten, waardoor er geen kosten komen.

------------- Het is aangegeven dat IP ranges 10.10.10.0/24 & 10.20.20.0/24 worden gebruikt. Echter weet ik nog niet of ik ze per VPC of per subnet moet indelen. Moet hierover vragen, maar ik ben van plan om per VPC in te delen<--------------------------------------
- per subnet moet een NACL zijn, die dient als firewall op subnet niveau. De ip adressen die daarin toegelaten zullen worden zijn nu niet bekend. Er zullen misschien maatregelen genomen moeten worden om die IP adressen later aan te passen. (user input?)
- Moeten de availability zones van de management vpc publiek zijn????<------------------------
 - UPDATE: private subnets zullen toegepast worden voor de database

# Servers

| **User story** | **Als klant wil ik een werkende applicatie hebben waarmee ik een werkende webserver kan deployen** |
| -------------- | -------------------------------| 
| **Epic** | v1.0 |
| **Beschrijving** | De applicatie moet een webserver starten en deze beschikbaar maken voor algemeen publiek. |
| **Deliverable** | IaC-code voor en webserver en alle benodigdheden

| **User story** | **Als klant wil ik een werkende applicatie hebben waarmee ik een werkende management server kan deployen** |
| -------------- | -------------------------------| 
| **Epic** | v1.0 |
| **Beschrijving** | De applicatie moet een management server starten en deze beschikbaar maken voor een beperkt publiek. |
| **Deliverable** | IaC-code voor een management server met alle benodigdheden |


- De product owner heeft aangegeven dat er piektijden zijn. Daardoor wordt er er een auto-scaler samen met een load balancer toegepast. Die zal gekoppeld zijn aan de webserver. 
 - Omdat er geen buitengewoon verkeer wordt verwacht, zal er één EC2 instance altijd aan zijn. 
 - Versie 1.1: De auto-scaler zal maximaal 3 instances tegelijk aan hebben. Dit om te zorgen dat er genoeg instances zijn. Er is gecomuniceerd dat de piekverkeer niet buitengewoon hoog is.
- Er moet een URL gecreërd worden voor de webserver. Er werd overwogen of die door Route 53 gemaakt zou moeten worden. Overleg met de product owner heeft getoond dat de DNS van de load balancer voldoende is.
- Bij het creëren van de EC2 instance(s) moet er op de user data configuratie ingesteld worden voor een webserver. Uit overleg met PO is het gebleken dat gebruikers zich moeten kunnen inschrijven op een nieuwsbrief, die dan bewaard wordt in de database. Er moet dus gezorgd worden dat de webserver kan communiceren met de database.
 - Versie 1.1: Omdat de webserver nu geen publiek ip mag hebben, moet het uit een voorbereide AMI gebouwd worden.





- Betreffende de management server, moet ik nog uitzoeken wat voor een oplossing toegepast moet worden. EC2 vs RDS of EC2 + RDS????<---------------------
- Wat komt precies in die webserver te zitten
 - UPDATE: Omdat er een RDP verbinding gemaakt moet worden, moet de management server een windows server zijn.
- Er moet een database zijn met gebruikersinformatie voor de nieuwsbrief. Een SQL database zal gebruikt moeten worden.
- Toegang moet beperkt zijn tot degenen die geauthorizeerd zijn om daar in te loggen. Er zal dus een IAM oplossing toegepast moeten worden. Ik moet uitzoeken hoe dat moet gebeuren<--------------
- Moet er ook een patch management oplossing toegepast worden?
  - In overleg besloten dat het niet noodzakelijk is.

UPDATE: Ik zie nu dat als ik een RDS met Multi-AZ wil opzetten, kan ik de primaire availability zone niet kiezen. Daardoor overweeg ik of RDS Read Replicas of Aurora te gebruiken.
	UPDATE: Omdat ik met Multi AZ de keuze niet krijg om de availability zone te kiezen, heb ik gekozen om de RDS database te plaatsen in de private netwerk van de productie VPC. omdat er dan minder kosten komen te zitten betreffende de comunicatie tussen de web server en de RDS database.


# Beveiliging

| **User story** | **Als klant wil ik dat al mijn data in de infrastructuur is versleuteld** |
| -------------- | -------------------------------| 
| **Epic** | v1.0 |
| **Beschrijving** | Er wordt veel gehecht aan de veiligheid van de data at rest en in motion. Alle data moet versleuteld zijn. |
| **Deliverable** | IaC-code voor versleuteling voorzieningen |



- Om de versleuteling uit te voeren, wordt de service AWS KMS toegepast.
- De data die versleuteld wordt is:
 - De webserver
 - De management server
 - De S3 bucket
 - De RDS database instance


- Er moeten security groups aan beide servers toegepast worden. 
- SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server. 

# Opslag


| **User story** | **Als klant wil ik een opslagoplossing hebben waarin bootstrap/post-deployment script opgeslagen kunnen worden** |
| -------------- | -------------------------------| 
| **Epic** | v1.0 |
| **Beschrijving** | Er moet een locatie beschikbaar zijn waar bootstrap scripts beschikbaar worden. Deze script moeten niet publiekelijk toegankelijk zijn. |
| **Deliverable** | IaC-code voor een opslagoplossing voor scripts |

- Overleg met de klant heeft getoond dat de voorkeur ligt op een S3 bucket waar SQL scripts worden bewaard.
- Er is verder bekend gemaakt dat die bucket niet publiek toegankelijk moet zijn. Daardoor is er gezorgd dat de script vanuit de stack geüpload wordt.
- Om die script later naar de RDS database te laten exporteren, is er gezorgd voor een Lambda functie die die operatie uitvoert.


# Backups

| **User story** | **Als klant wil ik iedere dag een backup hebben dat 7 dagen behouden wordt** |
| -------------- | -------------------------------| 
| **Epic** | v1.0 |
| **Beschrijving** | De klant wil graag dat er een backup beschikbaar is, mocht het nodig zijn om de servers terug te brengen naar een eerdere staat. (Zorg ervoor dat de Backup ook daadwerkelijk werkt) |
| **Deliverable** | IaC-code voor backup voorzieningen |


- Om de backups uit te voeren wordt gebruik gemaakt van de service AWS Backup.
- Overleg met de product owner heeft getoond dat de web server geen behoefte heeft aan een backup oplossing, omdat de klant zelf het makkelijk kan herstellen, ook als er aanpassingen komen. 
- Omdat de RDS database service zelf backup voorzieningen bevat, is er besloten die te gebruiken in plaats van AWS Backup.
- Er worden dus backups uitgevoerd van de management server en de S3 bucket.



![diagram](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Copy%20of%20cdk-project-01.drawio.png)
