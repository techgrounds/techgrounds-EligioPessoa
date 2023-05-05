# Elastic Load Balancing (ELB) & Auto Scaling
Een van de belangrijkste voordelen van de cloud is dat je niet hoeft te raden hoeveel capaciteit je nodig hebt. Je kunt altijd op- en afschalen met on-demand services. Een van de services die dit mogelijk maakt, heet Auto Scaling.

Wanneer je een applicatie uitvoert met een piekerige werklast, kan je de applicatie hosten op een _fleet_ van EC2-instances in plaats van op een enkele server. Wanneer de vraag naar de applicatie groot is, kan Auto Scaling automatisch instanties aan de fleet toevoegen. Wanneer de vraag lager is, kan het op dezelfde manier instanties verwijderen.

Om ervoor te zorgen dat alle servers hetzelfde zijn, maakt Auto Scaling gebruik van een (custom) AMI. Auto Scaling maakt gebruik van CloudWatch-statistieken om te bepalen of instanties moeten worden toegevoegd of verwijderd.

## Key-terms

- **Endpoint**: Fysieke apparaten die verbinding maken met en informatie uitwisselen met een computernetwerk. Enkele voorbeelden van eindpunten zijn mobiele apparaten, desktopcomputers, virtuele machines, ingebedde apparaten en servers.
- **AMI**: Een Amazon Machine Image (AMI) is een _masterimage_ voor het maken van virtuele servers - bekend als EC2-instances - in de Amazon Web Services (AWS)-omgeving.
De machine-images zijn als _templates_ die zijn geconfigureerd met een besturingssysteem en andere software die de besturingsomgeving van de gebruiker bepalen. AMI-typen zijn gecategoriseerd op basis van regio, besturingssysteem, systeemarchitectuur - 32- of 64-bits - startmachtigingen en of ze worden ondersteund door Amazon Elastic Block Store (EBS) of ondersteund door de instance store.
Elke AMI bevat een _template_ voor het rootvolume dat nodig is voor een bepaald type instantie. Een typisch voorbeeld kan een besturingssysteem, een applicatieserver en applicaties bevatten. Machtigingen worden ook gecontroleerd om ervoor te zorgen dat AMI-lanceringen worden beperkt tot de juiste AWS-accounts. Block device mapping zorgt ervoor dat de juiste volumes aan de gestarte instantie worden gekoppeld.
- **Load Balancer**: Load Balancer verdeelt het applicatieverkeer over meerdere doelen zoals EC2-instances, IP-adressen en containers. Als ik twee actieve instances heb en een N-aantal leden om toegang tot hun gegevens vraagt. Vervolgens verdeelt de load balancer die N-aanvragen gelijkmatig over twee actieve instances. Load balancer vermindert de belasting van de individuele instance en verhoogt de algehele prestaties van de applicatie. Er zijn ee paar load balancer-keuzes op AWS:

  - **Application Load Balancer**: werkt op laag 7. Richt zich op IP-instances, Lambda, containers. Ondersteunde protocollen zijn HTTP, HTTPS, gRPC
  - **Network Load balancer**: Werkt op laag 4. Richt zich op IP, instances, ALB, containers. Ondersteunde protocollen zijn TCP, UDP, TLS
  - **Gateway Load Balancer**: Pass through load balancer die werkt als laag 3 gateway en laag 4 load balancer. Richt zich op IP, instances. Ondersteunde protocollen zijn IP.
  - **Classic Load Balancer**: werkt op laag 4/7. Richt zich op EC2-Classic. Ondersteunde protocollen zijn TCP, SSL/TLS, HTTP, HTTPS. Klassieke load balancer wordt niet actief ontwikkeld.
  - **AWS Global Accelerator**: werkt als een load balancer. Werkt op TCP/UDP. Richt zich op IP, ALB, NLB. Ondersteunde protocollen zijn TCP, UDP

- **Auto Scaling**: Automatisch schalen wordt gebruikt om het aantal exemplaren automatisch te verhogen of te verlagen op basis van wat de applicatie vereist. Het zorgt ervoor dat je over het juiste aantal instances beschikt om de belasting van je applicatie te verwerken. Het schaalbeleid dat je definieert, past het aantal exemplaren aan, binnen je minimum- en maximumaantal exemplaren, op basis van de criteria die je opgeeft. Het doel van een Auto Scaling Group is om:

- **Scale Out** (EC2-instances toevoegen) om te voldoen aan een verhoogde belasting
- **Scale In** (verwijder EC2-instances) om overeen te komen met een verminderde belasting
- Zorg ervoor dat we een minimum en een maximum aantal draaiende machines hebben
- Registreer nieuwe instances automatisch bij een load balancer

## Opdracht
### Gebruikte bronnen

https://www.techtarget.com/searchaws/definition/Amazon-Machine-Image-AMI
https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment
https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html
https://repost.aws/questions/QUBf2Pm87iSsWkcpA3tF0EyQ/what-is-the-main-differences-between-an-load-balancer-and-a-autoscaling-group

### Ervaren problemen

Het uitshcalen van instances gebeurde niet goed, eerst omdat scaling policy niet aan was, en daarna omdat de CloudWatch alarms nniet aan waren.

### Resultaat

#### Exercise 1:
Launch an EC2 instance with the following requirements:

Region: Frankfurt (eu-central-1)

AMI: Amazon Linux 2

Type: t3.micro

Security Group: Allow HTTP

![instance](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11.png)
![sg](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11instance%26SG1.png)


#### Exercise 2:
Create an application load balancer with the following requirements:

Name: LabELB

Listener: HTTP on port 80

AZs: eu-central-1a and eu-central-1b

Subnets: must be public

Security Group: 

Name: ELB SG

Rules: allow HTTP access

Target Group:

Name: LabTargetGroup

![lb1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11createloadbalancer1.png)
![lb2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11elb1.png)

#### Exercise 3:
Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.

Create an auto scaling group with the following requirements:

Name: Lab ASG

Launch Configuration: Web server launch configuration

Subnets: must be in eu-central-1a and eu-central-1b 

Load Balancer: LabELB

![asg1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11createautoscaling1.png)
![asg2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11createautoscaling2.png)


Group Size:

Desired Capacity: 2

Minimum Capacity: 2

Maximum Capacity: 4

Scaling policy: Target tracking with a target of 60% average CPU utilisation


![asg3](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11createautoscaling3.png)
![tracking](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11trackingpolicy.png)

Group metrics collection in CloudWatch must be enabled
![alerts](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11alerts.png)


#### Exercise 4:
Verify that the EC2 instances are online and that they are part of the target group for the load balancer.

![](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11running1.png)
![](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11running2.png)

Access the server via the ELB by using the DNS name of the ELB.

![dns](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11DNS1.png)


Perform a load test on your server(s) using the website on your server to activate auto scaling. 

![success](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS11success!.png)
