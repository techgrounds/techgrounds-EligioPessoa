# Elastic Block Store (EBS)

**AWS Elastic Block Store (EBS)** is de opslagoplossing op blokniveau van Amazon die wordt gebruikt met de EC2-cloudservice om persistente gegevens op te slaan. Dit betekent dat de gegevens op de AWS EBS-servers worden bewaard, zelfs wanneer de EC2-instanties worden afgesloten. EBS biedt dezelfde prestaties met hoge beschikbaarheid en lage latentie binnen de geselecteerde beschikbaarheidszone, waardoor gebruikers opslagcapaciteit kunnen schalen tegen een laag abonnementsgebaseerd prijsmodel. De datavolumes kunnen dynamisch worden gekoppeld, losgekoppeld en geschaald met elke EC2-instantie, net als een fysieke blokopslagschijf.

## Key-terms


- **Block Storage**: Technologie die gegevensopslag en opslagapparaten bestuurt. Het neemt alle gegevens, zoals een bestand of database-item, en verdeelt deze in blokken van gelijke grootte. Het _block storage_ systeem slaat vervolgens het gegevensblok op de onderliggende fysieke opslag op een manier op die is geoptimaliseerd voor snelle toegang en ophalen. Ontwikkelaars geven de voorkeur aan blokopslag voor toepassingen die efficiënte, snelle en betrouwbare gegevenstoegang vereisen. Beschouw blokopslag als een directere pijplijn naar de gegevens. Bestandsopslag heeft daarentegen een extra laag die bestaat uit een bestandssysteem (NFS, SMB) dat moet worden verwerkt voordat toegang tot de gegevens wordt verkregen.
- **Snapshot**: Een EBS-snapshot is een point-in-time back-up van een EBS-volume. Het is een kopie van de gegevens op je EBS-volume. Als je een backup van een EC2-instantie wilt maken, moet je EBS-snapshots maken van de EBS-volumes die aan de _instance_ zijn gekoppeld. Dit is een goede noodhersteloplossing voor een EBS-volume.

De Snapshot mogelijkheid is cruciaal tot bedrijfscontinuïteitsplannen voor bedrijfskritische apps en services. Gebruikers kunnen Recovery Time Objectives (RTO) en Recovery Point Objectives (RPO) definiëren en de snapshots beheren om aan die doelstellingen te voldoen. Naast de doelstellingen voor gegevensback-up en noodherstel, gebruiken klanten EBS Snapshots ook om productiegegevens vast te leggen voor testen en ontwikkeling. EBS-snapshots en -volumes ondersteunen ook codering, waardoor gebruikers indien nodig aangepaste CMK kunnen maken vanuit de AWS IAM-beheerconsole.

## Opdracht
### Gebruikte bronnen


https://aws.amazon.com/what-is/block-storage/

https://www.bmc.com/blogs/aws-ebs-elastic-block-store/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

https://blog.skeddly.com/2017/03/ebs-snapshots-explained.html


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

https://stackoverflow.com/questions/25838962/permission-denied-when-accessing-new-ebs-volume



### Ervaren problemen

- Ik kon geen tekstbestand creëren in de folder waar het moest staan. Het aanpassen van eigenaarschapsrechten loste dit op.
- Het Internet viel uit tijdens de opdracht, waardoor ik mijn stappen moest herhalen
- Op de laatste fase, lukte het mij niet om de tweede volume te mounten. Na herstarten lukte het wel

### Resultaat

AWS EBS verschilt van de standaard EC2 Instance Store, die slechts tijdelijke opslag biedt die beschikbaar is op de fysieke EC2-hostservers. De EC2 Instance Store is handig voor tijdelijke gegevensinhoud zoals caches, buffers of bestanden die over de gehoste servers worden gerepliceerd. Voor gegevens die permanent beschikbaar moeten zijn, ongeacht de levensduur van een EC2-instantie, biedt AWS EBS de volgende opties voor opslagvolumes:

- **General Purpose SSD (gp2)**: Een optimale balans tussen kosten en prestaties voor uiteenlopende IT-workloads. Toepassingen zijn onder andere virtuele desktops, apps, ontwikkel- en testomgevingen.
- **Provisioned IOPS SSD (io1)**: De krachtige functionaliteit is met name geschikt voor bedrijfskritische IT-workloads. Geschikte toepassingen zijn onder meer grote databases en zakelijke apps die 16.000 IOPS of 250 MiB/s throughput per volume vereisen.


- **Throughput Optimized HDD (st1)**: Een goedkoop alternatief voor werklasten met grote opslagvolumes en hoge throughput vereisten. Voorbeelden zijn het streamen van workloads, big data-applicaties, logverwerking en data warehousing.
- **Cold HDD (sc1)**: Een goedkoop alternatief voor gebruiksscenario's met een vereiste om minimale kosten te behouden voor gegevensopslag van grote volumes. Voorbeelden hiervan zijn workloads die minder vaak worden gebruikt.


#### Exercise 1:
Navigate to the EC2 menu.
Create a t2.micro Amazon Linux 2 machine with all the default settings.
Create a new EBS volume with the following requirements:
Volume type: General Purpose SSD (gp3)
Size: 1 GiB
Availability Zone: same as your EC2
Wait for its state to be available.

![AWS07](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_.png)
![ebs2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_ebs2.png)

#### Exercise 2:
#### Attach your new EBS volume to your EC2 instance.

![attach1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_attach1.png)
![attached1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_attached1.png)

#### Connect to your EC2 instance using SSH. Mount the EBS volume on your instance.

![filesystem](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_createfilesystem.png)
![mount1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_mount1.png)


#### Create a text file and write it to the mounted EBS volume.

![issue1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_issues1.png)
![issuesolved](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_issusolved1.png)


#### Exercise 3:
#### Create a snapshot of your EBS volume.

![snapshot](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_snapshot005.png)

#### Remove the text file from your original EBS volume. Create a new volume using your snapshot.

![snapshot2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_snapshot2.png)

#### Detach your original EBS volume.

![snapshot](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_detach1.png)


#### Attach the new volume to your EC2 and mount it.

![attach2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_attach2.png)

#### Find your text file on the new EBS volume.

![success](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-07_success.png)
