# RDS

Amazon Relational Database Service (RDS) is een beheerde SQL-databaseservice die wordt aangeboden door Amazon Web Services (AWS). Amazon RDS ondersteunt een reeks database-engines om gegevens op te slaan en te organiseren. Het helpt ook bij relationele databasebeheertaken, zoals gegevensmigratie, back-up, herstel en patching.

Amazon RDS vergemakkelijkt de implementatie en het onderhoud van relationele databases in de cloud. Een cloudbeheerder gebruikt Amazon RDS om een relationele instantie van een clouddatabase in te stellen, te bedienen, te beheren en te schalen. Amazon RDS is zelf geen database; het is een service die wordt gebruikt om relationele databases te beheren.

## Key-terms


## Opdracht
### Gebruikte bronnen

https://www.youtube.com/watch?v=Viy1tBoinl0 (Intro to RDS in AWS for MySQL)

https://vigneshn.in/install-mysql-8-client-on-amazon-linux-2-arm-and-x86_64/

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html#CHAP_GettingStarted.Connecting.MySQL

https://www.techtarget.com/searchaws/definition/Amazon-Relational-Database-Service-RDS

### Ervaren problemen

Na het creëren en verbinden van een rds database met een ec2 instance, wou ik een .sql bestand importeren om te demonstreren dat het werkt. Het is me uiteindelijk niet gelukt, en omdat het toch niet bij de verantwoordigheden van cloud engineering hoorde, heb ik gewoon wat commands uigevoerd binnen mysql.

### Resultaat


#### Create Security Group for database (public access)

![sgrds1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/RDSsgrds1.png)

#### Create DB subnet groups (for redundancy, at least 2)

![subnetgrprds1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/RDSsubnetgrprds1.png)

#### Create Database (public access)

![created](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/RDSdbrdscreated1.png)


#### Connect to Database and execute a command

![](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/RDSrdsconnected.png)
