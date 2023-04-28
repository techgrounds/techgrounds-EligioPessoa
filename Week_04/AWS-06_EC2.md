# Elastic Compute Cloud (EC2)

De Elastic Compute Cloud-webservice van Amazon biedt aanpasbare rekencapaciteit in de cloud, zodat ontwikkelaars kunnen genieten van schaalbaarheid voor het bouwen van applicaties. Simpel gezegd, een EC2 is een virtuele machine die een als een fysieke server werkt, waarop je je applicaties kan implementeren. In plaats van je eigen hardware te kopen en deze op een netwerk aan te sluiten, geeft Amazon je bijna onbeperkte virtuele machines om je applicaties uit te voeren terwijl zij voor de hardware zorgen. _EC2 instances_ hebben een unieke functie die van fundamenteel belang is voor cloudcomputing, genaamd _Auto-Scaling Groups_. Hierdoor kunnen EC2 instances dynamisch extra rekenkracht toevoegen wanneer drempels zoals CPU-gebruik worden verbroken vanwege de grote vraag. AWS ondersteunt meerdere besturingssystemen, van Windows tot vele soorten Linux enz. Als klant kan je ook je eigen aangepaste besturingssysteem meenemen en op hun platform uitvoeren. Dit zorgt voor vrijwel onbeperkte mogelijkheden om je applicatie in de cloud uit te voeren.



## Key-terms

- **Instance**: Een _server resource_ die wordt geleverd door _third party cloudservices_. Hoewel je fysieke serverresources op locatie kunt beheren en onderhouden, is het duur en inefficiënt om dit te doen. Cloudproviders onderhouden hardware in hun datacenters en geven je virtuele toegang tot _compute resources_ in de vorm van een _instance_. Je kunt de cloud instance gebruiken voor het uitvoeren van rekenintensieve workloads zoals containers, databases, microservices en virtuele machines.

## Opdracht
### Gebruikte bronnen

https://www.techtarget.com/searchaws/definition/Amazon-EC2-instances

https://aws.amazon.com/what-is/cloud-instances/

https://www.clickittech.com/aws/connect-ec2-instance-using-ssh/#4

https://www.youtube.com/watch?v=0Gz-PUnEUF0

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

#### Exercise 1:
Navigate to the EC2 menu.

Launch an EC2 instance with the following requirements:

AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type

Instance type: t2.micro

Default network, no preference for subnet

Termination protection: enabled

User data:

![ec2prelaunch2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-06_ec2prelaunch2.png)


Root volume: general purpose SSD, Size: 8 GiB

New Security Group:

Name: Web server SG

Rules: Allow SSH, HTTP and HTTPS from anywhere

![prelaunch](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-06_ec2prelaunch.png)

#### Exercise 2:
Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.



![launch](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-06_ec2launch.png)

Log in to your EC2 instance using an ssh connection.

![ec2loggedin](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-06_ec2loggedin.png)


Terminate your instance.

![terminate](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-06_terminate.png)
![terminated](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-06_terminated.png)
