# Subnetting

Subnetting is een methode om een enkele fysieke netwerk te splitsen in _logische sub-netwerken_. Subnetting laat een bedrijf zijn netwerk uitbreiden zonder dat nieuwe netwerk nummers aangevraagd moeten worden.


## Key-terms

- **Subnet**: een kleiner netwerk dat onderdeel is van een groter netwerk. Subnets kunnen worden gebruikt om een deel van het netwerk logisch te isoleren. Een subnet heeft per definitie een grotere prefix dan het netwerk waar het subnet in zit.

- **NAT Gateway**: gebruikt om hosts in een privé subnet met het Internet te laten communiceren, zonder dat ongesoliciteerde verbindingen vanuit Internet ontvangen kunnen worden.

- **Internet Gateway**: Een verbinding russen een Virtual Private Cloud (VPC) en het Internet. Het laat internetverkeer binnen het netwerk.

## Opdracht
### Gebruikte bronnen

https://medium.com/awesome-cloud/aws-vpc-difference-between-internet-gateway-and-nat-gateway

https://stackoverflow.com/questions/57196792/does-a-nat-gateway-require-an-internet-gateway

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

https://www.linkedin.com/pulse/connecting-internet-from-ec2-instance-private-subnet-aws-thandra

https://www.youtube.com/watch?v=bQ8sdpGQu8c (Free CCNA | Subnetting (Part 1) | Day 13 | CCNA 200-301 Complete Course)

https://www.youtube.com/watch?v=IGhd-0di0Qo&t=866s (Free CCNA | Subnetting (Part 2) | Day 14 | CCNA 200-301 Complete Course)

### Ervaren problemen

Er was verwarring over het aantal subnets die gemaakt moesten worden, zowel als met hoe de private subnet zonder internet met de rest van het netwerk moest verbinden. Discussie met de groep heeft dit verhelderd.


### Resultaat

De Internet gateway maakt verbinding met het Internet. Aan de Internet Gateway zijn verbonden:

- De NAT Gateway, die via de Internet Gateway op Internet moet verbinden.
- De publieke subnet, met een publieke IP met subnet mask 255.255.255.248 , geschikt voor 6 hosts, dus 1 meer dan nodig.

Aan de NAT Gateway wordt de privé subnet die Internet via NAT Gateway moet hebben, waardoor de hosts in die subnet met het Internet kunnen verbinden, maar geen verbindingen vanuit het Internet ontvangen. Die subnet heeft een subnet mask 255.255.255.192, die geschikt is voor maximaal 62 hosts, dus meer dan de 30 benodigde hosts.


De publieke subnet maakt verbinding met een privé subnet met dezelfde subnet mask eigenschappen, om vervolges te kunnen verbinden met de rest van het netwerk. Voor beveiligingsredenen heb ik de verbinding tussen de publieke en de privé subnet via een reverse proxy gedaan.

Dan is er de privé subnet die alleen binnen de LAN toegankelijk is. Die heeft een subnet mask 255.255.255.224, die geschikt is voor 30 hosts, meer dan de 15 benodigde hosts.

Om de privé subnet 1 te kunnen verbinden met de andere privé subnetten, heb ik ze via een switch verbonden. Die is Layer 3, om zeker te maken dat alle soort verkeer tussen de subnets uitgewisseld kan worden.


![Diagram](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/NTW06.drawio(1).png)
