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

