# Security Groups

Een van de fundamentele uitdagingen waarmee men te maken krijgt bij een cloudcomputingservice zoals AWS, is dat niet alle beveiligingscontroles geïmplementeerd kunnen worden die ter plaatse beschikbaar zouden zijn, omdat men geen toegang heeft tot de fysieke infrastructuur die de cloud-omgeving aandrijft. Je kan bijvoorbeeld niet dezelfde typen netwerkfirewalls instellen, omdat je geen controle hebt over de netwerkinfrastructuur van je cloudprovider. Wat je wel kan doen is profiteren van oplossingen zoals AWS Security Groups, een _framework_ om te bepalen welk netwerkverkeer van en naar cloudgebaseerde virtuele machines kan stromen.

## Key-terms

- **Security Group**: _AWS Security Groups_ zijn software gedefinieerde firewalls die het verkeer naar EC2-instanties regelen. Met andere woorden, een Security Group is een reeks beleidsregels die bepalen met welke andere _resources_ op het netwerk je op EC2 gebaseerde virtuele machines kunnen communiceren. Security Groups kunnen ook specificeren welke netwerkprotocollen gebruikt mogen worden door EC2-instanties.
- **Access Control List**: In AWS is ACL een beveiligingsfunctie die helpt bij het beheren van de toegang tot objecten die zijn opgeslagen in Amazon S3-buckets. ACL's zijn in wezen een set regels die bepalen welke AWS-accounts of groepen toestemming krijgen voor toegang tot specifieke S3-objecten of -buckets.

## Opdracht
### Gebruikte bronnen

https://jayendrapatil.com/aws-vpc-security-group-vs-nacls/

https://www.wiz.io/academy/understanding-aws-security-groups



https://www.tutorialspoint.com/what-are-the-differences-between-security-group-and-network-acl-in-aws

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison

https://medium.com/awesome-cloud/aws-difference-between-security-groups-and-network-acls-adc632ea29ae

https://docs.aws.amazon.com/vpc/latest/userguide/security-groups.html

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html

https://docs.aws.amazon.com/managedservices/latest/userguide/restrict-nacl.html

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

Study:
- Security Groups in AWS




- Network Access Control Lists in AWS

In vergelijking met _Security Groups_ is een ACL moeilijker in te stellen omdat er meer velden geconfigureerd moeten worden dan Security Groups vereisen. ACL's zijn ook ontworpen om verkeer op subnetniveau te beheren in plaats van op het niveau van individuele VM-instanties, dus ze bieden niet zo veel granulaire controle.


| Security Groups | Network Access Control Lists - NACLs |
| --------------- | ------------------------------------ |
| Werkt op _instance_ niveau | Werkt op _subnet_ niveau |
| Is alleen van toepassing op een _instance_ als deze aan de _instance_ is gekoppeld | Is van toepassing op alle _instances_ die geïmplementeerd zijn in het bijbehorende subnet (zorgt voor een extra verdedigingslaag als de regels van de _Security Group_ te tolerant zijn) |
| Ondersteunt alleen _allow_ regels toe | Ondersteunt _allow_ regels  en _deny_ regels |
| Alle regels worden geëvalueerd voordat er besloten wordt of verkeer wordt toegestaan | Regels worden op volgorde geëvalueerd, beginnend met de laagst genummerde regel, bij de beslissing om verkeer toe te staan |
| Stateful: Retourverkeer is toegestaan, ongeacht de regels | Stateless: Retourverkeer moet expliciet worden toegestaan door regels |
| Meerdere _Security Groups_ kunnen gekoppeld worden aan _resources_ en één _Security Group_ kan aan meerdere _resources_ gekoppeld worden | Meerdere _subnetten_ kunnen worden gekoppeld aan een enkele NACL, maar alleen **één** _subnet_ kan tegelijkertijd gekoppeld zijn aan een enkele NACL |
