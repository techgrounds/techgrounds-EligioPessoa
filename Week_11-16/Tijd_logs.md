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
