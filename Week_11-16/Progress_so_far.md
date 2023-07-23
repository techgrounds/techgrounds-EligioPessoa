# Voldane en ontbrekende eisen


- Voor versie 1.0 in dit project is het zover gelukt om twee VPC's aan te maken, met verbinding aan elkaar via VPC Peering
	- Zover is het nog niet gelukt om de NACL's te configureren om alleen de toegestane ip's in te laten.


- In de Management VPC is een EC2 die verbinding kan maken via SSH of RDP met de EC2 instance van de Productie VPC.

- De RDP instance is geplaatst in de private subnets van de Productie VPC. Het is geconfigureerd op Multi AZ om te zorgen voor availability, en met automatische Backups, die iedere dag uitgevoerd worden en 7 dagen bewaard worden.

- In de Productie VPC, zit de Web Server in een Load Balancer met een Auto-Scaling group, die zorgt voor schaalbaarheid. 
	- Het is op dit moment niet gelukt om de ASG volledig te configureren zodat het automatisch in kan schalen. Zover schaalt het alleen uit.

- Er is een S3 aangemaakt waar er later post-deployment scripts zullen komen te staan
	- Toestemmingen moeten nog worden aangepast ervoor

- Er is een AWS Backup actie gescheduled om dagelijks backups uit te voeren van de S3 en de Management Server, en ze 7 dagen bewaard te houden.

- Er is ervoor gezorgd dat de EC2 en RDS instances en de S3 allemaal worden geëncrypteerd me een KMS sleutel, aangemaakt tijdens het deployen.





De redenen waarom het project nog niet volledig af is zijn:
	- Tijdens ontwerp van de netwerk zijn er problemen ontstaan, waardoor er adres conflicten waren in de subnets, en de netwerk opnieuw ontworpen moest worden.
	- Omdat er met CDkv2 gewerkt wordt, is er weinig documentatie beschikbaar om valkuilen op te lossen.

Door deze redenen, heeft het ontwerpen van het project langer geduurd dan gepland.
