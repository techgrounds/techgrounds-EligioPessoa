# Virtual Private Cloud (VPC)

**Amazon Virtual Private Cloud (VPC)** is een commerciële cloud computing-service die een virtuele privécloud biedt door een logisch geïsoleerd deel van _Amazon Web Services (AWS) Cloud_ in te richten. Klanten hebben toegang tot de _Amazon Elastic Compute Cloud (EC2)_ via een op IPsec gebaseerd virtueel particulier netwerk. In tegenstelling tot traditionele EC2-instanties die door Amazon interne en externe IP-nummers krijgen toegewezen, kan de klant IP-nummers naar keuze toewijzen uit een of meer subnetten. Door de gebruiker de mogelijkheid te geven om te selecteren welke AWS resources openbaar zijn en welke niet, biedt VPC veel gedetailleerdere controle over beveiliging. Voor Amazon is het "een bevestiging van de hybride aanpak, maar het is ook bedoeld om de groeiende belangstelling voor private clouds tegen te gaan"

## Key-terms

- **Elastic IP**: In principe worden elastische IP-adressen door AWS gebruikt om zijn dynamische cloud computing-services te beheren. Binnen de AWS-infrastructuur hebben klanten virtual private clouds (VPC), binnen de VPC's hebben gebruikers instances. Dus als iemand een EC2-instantie start, ontvangen ze een openbaar IP-adres waarmee die instance bereikbaar is via internet. Zodra ze die instance stoppen en opnieuw starten, krijgen ze een nieuw openbaar IP-adres voor dezelfde instance. Het is dus eigenlijk een probleem om je instance vanaf internet te verbinden omdat je geen statisch IP-adres hebt. Om dit probleem op te lossen, koppelen we een Elastic IP aan een instance die niet verandert nadat de instance gestopt/gestart is. Kort gezegd is Elastic IP een permanent IP-adres voor je instantie.

## Opdracht
### Gebruikte bronnen

https://en.wikipedia.org/wiki/Amazon_Virtual_Private_Cloud

https://stackoverflow.com/questions/50306324/what-is-elastic-ip-in-aws-and-why-it-is-useful

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html

https://www.edureka.co/community/9792/what-is-difference-between-elastic-ip-and-public-ip

https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html

https://stackoverflow.com/questions/64413110/aws-ec2-what-can-i-accomplish-with-the-public-dns-hostname-that-i-cant-with-t

### Ervaren problemen

- Ik had geen DNS adres omdat het bleek dat ik nog geen Elastic IP had toegewezen.
- Ik kon de website niet openen, tot ik achterkwam dat ik het in HTTP i.p.v. HTTPS moest visualiseren.

### Resultaat

#### Exercise 1

![vpc](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex1vpc.png)
![pubtab](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex1pubtab1.png)
![privtab](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex1pritab1.png)

#### Exercise 2

![vpcpub](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex2vpcpub.png)
![vpcpriv](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex2vpcpri.png)
![pubtab](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex2pubtab2.png)
![pritab](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex2pritab2.png)

#### Exercise 3

![secgrp](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex3secgrp.png)

#### Exercise 4

![inst1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex4launchinstance.png)
![inst2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex4launchinstance2.png)
![inst3](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex4launchinstance3.png)
![website](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-10_ex4vpclastwebsite.png)
