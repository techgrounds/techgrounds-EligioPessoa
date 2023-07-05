# Log 05/06/2023

## Dagverslag 
Projecteisen bestudeerd en een plan ontworpen.

## Obstakels

Gebrek aan kennis, onduidelijkheid over doelen, gebrek aan informatie

## Oplossingen

Gestructureerde analyse uitgevoerd van de projecteisen om uitvoerbare acties te kunnen isoleren

## Learnings

Introductie aan cdk, user stories and epics

---

# Log 06/06/2023

## Dagverslag 
Ik heb VSCode aan mijn AWS account gekoppeld, en de benodigde programma's geïnstalleerd om de CDK tools te kunnen gebruiken.

## Obstakels
- Iedere keer dat ik wou beginnen met experimenteren met de cdk tool, kwam ik telkens achter dat er bepaalde programma's nog bij geïnstalleerd moesten worden.
- Resource templates voor cdk zijn niet helemaal duidelijk, waardoor ik ze niet zomaar kan kopiëren en plakken
## Oplossingen
Bronnen goed uitgezocht en stappen teruggelopen als er iets foutging.

## Learnings

- Het aanmaken, deployen en verwijderen van een cdk applicatie en de bijbetrokken resources
- Dat we naast de tijdlogs ook de ontwerp en beslissingdocumentatie bij moeten houden

---

# Log 07/06/2023


## Dagverslag 
Ik heb vandaag een preliminaire diagram gemaakt van de VPC, mijn beslissingsdocument geredacteerd en mijn uitvoeringsplan verder uitgebreid.

## Obstakels
Onduidelijkheid over de uitvoeringen van de management server

## Oplossingen
Na overleg met de team, zag ik dat ik het te ingewikkeld maakte.

## Learnings
VPC Peering kosten en voorwaarden, verdiept in benodigheden van management server, beveiliging en versleutelingservices.

---

# Log 08/06/2023


## Dagverslag
Ik heb mijn diagram verbeterd en vervolgens aan mijn team getoond, en cdk code gebouwd voor 2 VPC's met 2 subnets

## Obstakels
Code die op internet te vinden is voor AWS CDK Python is niet direct toepasbaar, ik kon geen werkende code invoeren.

## Oplossingen
Diverse bronnen nagecheckt, samen met ChatGPT, tot ik aan werkende code kon komen.

## Learnings
De basis syntax om VPCs en subnets met ingestelde ip-range in te stellen; ideën met de team uitgewisseld voor het bouwen van de diagram.

---

# Log 09/06/2023


## Dagverslag 
Vandaag had ik een sollicitatiegesprek bij inQdo, waardoor ik maar 2 uur bezig was met studie, en wat verder onderzoek heb gedaan op het veld van VPC, subnets en route tables.

## Obstakels
n.v.t.

## Oplossingen
n.v.t.

## Learnings
Hoe een configuratie bestand in kunt stellen en refereren; route table syntax en het associeren daarvan met subnets.

---

# Log 12/06/2023


## Dagverslag 
Ik heb de grootste gedeelte van de dag pogingen gemaakt tot het creëren van 2 VPC's met 2 subnets en routetables. Daarna wat onderzoek gedaan over VPC Peering.

## Obstakels
Het lukt nog steeds niet om de subnets op één routetable per VPC te distribuëren.

## Oplossingen
Wat kleine stapjes gemaakt, aangepast waar het kon, foutmeldingen waren steeds anders, dus er is progressie. Geschakeld naar VPC Peering.

## Learnings
Werken met variabels in AWS CDK Python.

---

# Log 13/06/2023


## Dagverslag
Vandaag heb ik beide vpcs met vpc peering gedeployed, een ec2 instance op elke vpc gedeployed, en een rds instance op de tweede netwerk. Ik ben ook achtergekomen hoe ik minder route tables kan maken.

## Obstakels
- Ik kon geen RDS creëren omdat het ook een subnet group moest hebben.
- Ik kon nog steeds geen twee VPC's met een enkele route table per vpc, en ik had problemen met het creëren van meerdere internet gateways

## Oplossingen
- Onderzoek heeft getoond dat het een bekende issue van cdk dat er een route table per subnet werd gecreërd. Uiteindelijk heb ik een aparte configuratie sdk kunnen maken voor het aanmaken van elke individuele subnet, route table, en twee internet gateways.
- Na het creëren van een subnetgroup lukte het mij om een rds instance aan te maken.

## Learnings

- Ik heb verdere inzicht gekregen op de verschillende soorten varianten in python, en hoe ze verschillen per use case.

---

# Log 14/06/2023


## Dagverslag
Ik heb de ideën van verschillende pogingen tot deployen geïntegreerd in één ontwerp, dat is, ec2's gedeployed in de code waar ik route tables goed ingericht had.

## Obstakels
- Achtergekomen dat RDS niet gedeployed kan worden in de vorm die ik oorspronkelijk had gepland.
- Een api waar ik gebruik van maakte was deprecated, en ik wist niet hoe ik het moest vervangen.

## Oplossingen
- Ik heb besloten te schakelen naar het gebruik van Aurora, die volgens AWS Cost Explorer zelfs voordeliger wordt.
- Na wat googlen, experimenteren en code observeren, heb ik kunnen vinden hoe ik precies de code moest aanpassen.
## Learnings
Beperkingen van RDS, beter werken met aws api's.

---
# Log 15/06/2023


## Dagverslag
Vandaag heb ik een s3 bucket toegevoegd aan mijn ontwerp, en een security group ingesteld volgens best security practices 

## Obstakels
- Ik kwam achter dat het niet volgens best practices om ingress/egress rules toe te voegen aan een security group met cdk.
- Ik kon een bucket aanmaken, maar wist de naam niet goed aan te passen
## Oplossingen
- Curt heeft ons laten zien hoe de S3 bucket aangepast kan worden
- Ik heb de .connections object gebruikt om de security group in te stellen.

## Learnings
- Best practices Security Groups, naaminstellingen cdk.

---
# Log 16/06/2023


## Dagverslag (1 zin)
Ik heb mijn stack aangepast - wat comments toegevoegd, en security groups aangepast.

## Obstakels
Ik kon geen verbinding maken met mijn instance

## Oplossingen
Troubleshooting toonde dat het probleem lag aan een misgeconfigureerde security group. Ik zocht uit hoe ik die moest coderen, en daarna lukte het.

## Learnings

Mijn collega's en ik hebben wat ideën uitgewisseld over het maken van verschillende stacks en het toepassing daarvan.

---
# Log 19/06/2023


## Dagverslag 
Na het presenteren van mijn huidige vooruitgang, heb ik mijn security groups aangepast en onderzoek gedaan tot het toevoegen van private subnets en een NAT gateway.

## Obstakels
Het toevoegen van private subnets en NAT gateway schijnt niet compatibel te zijn met mijn huidige ontwerp.

## Oplossingen
Ik ben eenvoudigere vormen aan het uitzoeken voor dezelfde doeleinden die ik zover had.

## Learnings
Het configureren van uitzonderingen in security groups zonder ip's, cdk code voor NAT gateway.

---
# Log 20/06/2023


## Dagverslag 
Ik heb een elastic load balancer en auto scaling group toegepast aan mijn netwerk.

## Obstakels
De configuratie van de ELB shijnt niet compatibel te zijn met de ontwerp van mijn netwerk

## Oplossingen
Ik heb geschakel naar een simpelere versie van de netwerk ontwerp.

## Learnings
CDK opmaak van Elastic Load Balancer en Auto Scaling Group

---

# Log 21/06/2023


## Dagverslag (1 zin)
Ik heb aanpassingen gemaakt aan de Elastic Load Balancer en Auto-Scaling Group, en verder onderzoek gedaan naar AWS Backup en KMS

## Obstakels
Auto-Scaling Group schijnt alleen maar out te scalen, en niet in

## Oplossingen
Even geschakeld naar de laatste gedeelten van de CDK die nog gemaakt moeten worden.

## Learnings
CDK benodigheden van KMS en AWS Backup

---
# Log 22/06/2023


## Dagverslag 
Ik heb de basiscode van AWS Backup geïmplementeerd en de Auto-Scaling Group getest

## Obstakels


## Oplossingen


## Learnings
CDK toepassing van AWS Backup.

---
# Log 23/06/2023


## Dagverslag 
Ik ben vandaag begonnen met KMS toepassen in mijn ontwerp, en AWS Backup taken toegevoegd

## Obstakels
Toen ik encryptie toepastte op de ec2 instanties, werden ze niet gedeployed.

## Oplossingen
Ik zag dat het aan mijn zelf gecreërde KMS sleutel lag. Nadat ik het verwijderde, konden de instanties gecreërd worden met de sleutel van AWS zelf.

## Learnings

CDK toepassing van AWS KMS.

---
# Log 26/06/2023


## Dagverslag 
Ik heb permissies toegepast om de AWS Backup jobs uit te kunnen voeren.

## Obstakels
De backup jobs bleven falen door gebrek aan juiste permissies

## Oplossingen
Ik heb de AWS documentatie gekeken om de permissies toe te kunnen passen.

## Learnings
Toepassing van permissies in CDK

---
# Log 27/06/2023


## Dagverslag
Testen uitgevoerd, troubleshooting en aanpassingen op de backup opties.

## Obstakels
Ik wist niet hoe ik alleen 2 ec2 instances aan kon hebben samen met de load balancer/auto-scaling group.

## Oplossingen
Na wat tips gekregen van mijn collega's, heb ik de load balancer als web server ingesteld. Toch blijkt het dat ik dat los moet laten, omdat het het backup proces ingewikkelder maakt.

## Learnings
Auto-Scaling group, KMS en Backup opties

---
# Log 28/06/2023


## Dagverslag
Fine-tuning uitgevoerd aan mijn huidige code.

## Obstakels
- Ik kon mijn RDS instance niet deployen als ik geen NAT Gateway had
- Mijn S3 bucket kon niet gebackupt worden, al had ik alle permissions staan
## Oplossingen
- Het vervangen van low-level constructs naar high-level constructs op RDS lostte mijn probleem op
- Uiteindelijk bleek het dat één van de permissions voor S3 niet op het goede veld was. Nadat ik dat ontdekte, kon ik de S3 backuppen.

## Learnings
Onderzoek gedaan naar het verschil tussen RDS automated backups en AWS Backup.

---

# Log 29/06/2023


## Dagverslag 
Ik heb wat problemen opgelost, testen uitgevoerd en onderzoek naar de NACL gedaan.

## Obstakels
- Ik kon de geëncrypteerde auto scaling group niet deployen.
- Ik kon geen verbinding maken tussen de management server en web server

## Oplossingen
- Ik heb de kms permissions aangepast, om de autoscaling group te laten deployen
- Ik heb de publieke ip van de management server gekoppeld aan de security group van de web server; daarna lukte het om verbinding te maken

## Learnings

- Het belang van permissions; effecten van NACL.


# Log [30/06/2023]


## Dagverslag
Ik heb testen uitgevoerd, problemen troublegeshoot

## Obstakels
- Mijn autoscaling group schaal alleen uit, niet in.
- Ik kan de NACL nog niet configureren om de netwerk te kunnen gebruiken (health checks voor ASG falen; kan niet toegang krijgen tot ec2 instances, al zet ik mijn eigen ip nummer in de toegestane ip nummers)

## Oplossingen
- Ik heb in verschillende condities mijn code gedeployed, om te testen of een bepaalde conditie het inschalen tegenhoudt, maar zonder succes.
- Ik heb geprobeerd om ephemeral port nummers toe te laten in de NACL, maar geen succes.
## Learnings

- Hoe ephemeral port nummers toegelaten moeten worden om bepaalde services te laten werken.
---


# Log [03/07/2023]


## Dagverslag
Ik heb de versie 1.1 van het project doorgelezen, plannen gemaakt voor de nieuwe en aangepaste eisen, en wat code aangepast.

## Obstakels
- Ik kon mijn autoscaling group nog steeds niet goed laten in en uitschalen
- Toen ik `assign_public_ip=False` probeerde in te stellen, kreeg ik een foutmelding omdat het niet toe te passen was met de launchtemplate die ik had ingesteld
## Oplossingen
- Ik heb expliciete scale policies ingesteld voor het in en uitschalen volgens custom metrics i.p.v. automatische scale policies, en nu schalen de instances in en uit zoals verwacht.
- Mijn groep heeft mij laten zien dat het encrypteren (de reden waarom ik templates gebruiktte) ook kan in de gewone autoscaling construct.

## Learnings

Het gebruik van een load balancer als proxy en het herrouten van net verkeer naar https ermee.

---

# Log 04/07/2023


## Dagverslag 

Ik heb testen en troubleshooting uitgevoerd voor de aanpassingen voor v1.1

## Obstakels
- Als ik geen publieke ip zet voor de instances in de auto-scaling group, falen de healthchecks
- Zover kan ik mijn zelf getekende ssl certificaten niet importeren

## Oplossingen
- Testen uitgevoerd met userdata in de autoscaling instances. Nog geen oplossing gevonden

## Learnings

Bewust geworden van aanpassende voorwaarden tijdens het gebrek aan een publieke ip

---
