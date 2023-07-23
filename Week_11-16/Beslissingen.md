Voor het project die ik uitgevoerd heb, de volgende eisen zijn aangegeven:


User story:

| **Als klant wil ik een werkende applicatie hebben waarmee ik een veilig netwerk kan deployen** | 

| **Epic** | v1.0 |

| **Beschrijving** | De applicatie moet een netwerk opbouwen dat aan alle eisen voldoet. Een voorbeeld van een genoemde eis is dat alleen verkeer van trusted sources de management server mag benaderen. |

| **Deliverable** | IaC-code voor het netwerk en alle onderdelen | 



Alle VM disks moeten encrypted zijn.
De webserver moet dagelijks gebackupt worden. De backups moeten 7 dagen behouden worden.
De webserver moet op een geautomatiseerde manier geïnstalleerd worden.
De admin/management server moet bereikbaar zijn met een publiek IP.
De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis)
De volgende IP ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24
Alle subnets moeten beschermd worden door een firewall op subnet niveau.
SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server.



# Netwerk


2 VPC's moeten worden aangemaakt. Één voor productie omgeving, andere voor administratie/management omgeving. 
- De reden om 2 VPC's te maken is om te zorgen dat de omgevingen apart van elkaar zijn, waardoor ze veiliger zijn. 
- In de oorspronkelijke schema werd gevraagd om de VPC's in 2 aparte regio's te bouwen. Uit discussie is gebleken dat dat meer kostbaar is, en de veiligheid en stabiliteitsvoordelen dat het zou brengen niet te relevant zijn.
- Elke VPC dient 2 availability zones te hebben, met een subnet in elke AZ. In het geval van de management vpc, zal die als backup dienen in het geval van uitval van de hoofdmanagement server en availability zone. In het geval van de applicatie productie VPC, omdat er piekverkeer momenten kunnen zijn, zullen er extra availability zones zijn om te zorgen dat er extra EC2 instances gecreërd kunnen worden door middel van een auto-scaler, met natuurlijk een load balancer om de load te balanceren tussen die instances. Uitzoeken of er ook meerdere availability zones beschikbaar gesteld kunnen worden voor de webserver.<----------------------
- Om verbinding te maken tussen de twee VPC's wordt een VPC peering connection gebruikt. Uit kostoverwegingen lijkt het verstandig om te zorgen dat de services die altijd aan zullen zijn op dezelfde availability zone zitten, waardoor er geen kosten komen.

------------- Het is aangegeven dat IP ranges 10.10.10.0/24 & 10.20.20.0/24 worden gebruikt. Echter weet ik nog niet of ik ze per VPC of per subnet moet indelen. Moet hierover vragen, maar ik ben van plan om per VPC in te delen<--------------------------------------
- per subnet moet een NACL zijn, die dient als firewall op subnet niveau. De ip adressen die daarin toegelaten zullen worden zijn nu niet bekend. Er zullen misschien maatregelen genomen moeten worden om die IP adressen later aan te passen. (user input?)
- Moeten de availability zones van de management vpc publiek zijn????<------------------------
 - UPDATE: private subnets zullen toegepast worden voor de database

# Services

- Omdat er piektijden zijn, moet er een auto-scaler samen met een load balancer geconfigureerd worden. Die zal gekoppeld zijn aan de webserver. 
- Omdat er geen buitengewoon verkeer wordt verwacht, zal er één EC2 instance altijd aan zijn. Er moet nog bepaald worden of het een Reserved instance is of On-Demand. Ik neig naar Reserved, omdat het altijd aan moet zijn. Aan de andere kant, ik weet niet of het te doen is met IaC.<---------------------
  - Overleg met de groep heeft getoond dat projektmatig het niet verstandig zou zijn om Reserved Instances te gebruiken, omdat het ook getest moet worden.
  - De auto-scaler zal maximaal 4 instances tegelijk aan hebben. Dit om te zorgen dat er genoeg instances zijn. Er is gecomuniceerd dat de piekverkeer niet buitengewoon hoog is, dus lijkt het meer dan 6 instances overbodig.
- Er moet een URL gecreërd worden voor de webserver. Die zou door Route 53 gemaakt moeten worden.
- Bij het creëren van de EC2 instance(s) moet er op de user data configuratie ingesteld worden voor een webserver. Uit overleg met PO is het gebleken dat gebruikers zich moeten kunnen inschrijven op een nieuwsbrief, dus er zal een veld moeten zijn waar een e-mail adres ingevoerd kan worden, die dan bewaard wordt in de database van de management server.

UPDATE: Onderzoek heeft getoond dat het gebruik van het object .connections best practice is, in plaats van Direct manipulation of the Security Group through addIngressRule and addEgressRule.
 - Verder zie ik dat de security group van de web server regels moet hebben waar er toegang wordt gekregen via de management server met SSH en RDP. UPDATE: er moet geen elastic ip zijn in de management server, omdat het niet noodzakelijk is.



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

- Volgens de aangegeven instellingen, hoort er een KMS toegepast te worden. Echter hoort alle data at rest en in transit versleuteld te worden. Ik moet nog onderzoeken hoe KMS toegepast moet worden.<------------------------------
- Er moeten security groups aan beide servers toegepast worden. 
- SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server. Dit betekent dat Security Groups uitgaande verbindingen vanuit die protocollen op de webserver geblokeerd moeten worden.

# Opslag

Het is bekend dat de klant een opslagoplossing wilt hebben waarin bootstrap/post-deployment script opgeslagen kunnen worden. Er moet dus een S3 zijn, die niet toegankelijk is voor het pupliek, waar ze bewaard worden. Ik weet niet of die scripts er al in staan, of er een script gemaakt moet worden om ze daarin te plaatsen.<--------------


# Backups

Het is bekend dat de klant iedere dag een backup wilt hebben dat 7 dagen behouden wordt. De service AWS Backup wordt aangewezen, maar ik moet kijken hoe dat toegepast kan worden, en op welke servers (allebei?)
	UPDATE: Overleg met de product owner heeft getoond dat de web server geen behoefte heeft aan een backup oplossing, omdat de klant zelf het makkelijk kan herstellen, ook als er aanpassingen komen.



![diagram](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Copy%20of%20cdk-project-01.drawio.png)
