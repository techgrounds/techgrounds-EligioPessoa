# EFS
Amazon EFS is een cloudgebaseerde service voor bestandsopslag voor applicaties en workloads die worden uitgevoerd in de openbare cloud van Amazon Web Services.

Het is ontworpen om zeer beschikbaar, zeer duurzaam en zeer schaalbaar te zijn, waardoor het ideaal is voor use cases die gedeelde bestandsopslag vereisen, zoals contentmanagementsystemen, webservers en ontwikkelomgevingen. De service wordt automatisch geschaald om te voldoen aan de opslagbehoeften van applicaties, zonder handmatige tussenkomst.

Gegevens worden gerepliceerd over meerdere beschikbaarheidszones binnen een regio; een IT-professional heeft toegang tot elk bestandssysteem vanuit verschillende AZ's in de regio waar het zich bevindt. De service ondersteunt ook periodieke back-ups van on-premises opslagservices naar EFS voor noodherstel.

## Key-terms


## Opdracht
### Gebruikte bronnen

https://www.youtube.com/watch?v=Aux37Nwe5nc (AWS - Amazon EFS file system creation, mounting & settings)

https://www.youtube.com/watch?v=GG8PAAOUGBg (Neal Davis - Create an Amazon EFS Filesystem)

https://www.shellhacks.com/sudo-echo-to-file-permission-denied/


### Ervaren problemen
Geen problemen ervaren

### Resultaat

### Create a File System

#### Create security group

![createsec1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFScreatesec1.png)

#### Add NFS inbound rule for this security group
This Security Group will be attached to our instances but it will also be attached to the file system and this rule we've just added will allow inbound traffic on the NFS Port from the instances that have this Security Group attached

![createsec2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFScreateinstance2.png)

#### Launch instance(s)

![createinstance1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFScreateinstance1.png)
![createinstance2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFScreateinstance2.png)

#### Create EFS file system and copy DNS name

![filesyscreate1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFSfilesyscreate1.png)
![filesyscreate2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFSfilesyscreate2.png)

#### Connect to instances

![connect1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFSconnect1.png)


#### Commands

sudo yum -y update
mkdir ~/efs-mount-point
sudo yum install -y amazon-efs-utils


#### Change Security Group from default to EFS
 We've enabled the mount points only in the 1A and 1B availability zones and we have a security group attached and that Security Group will allow inbound access on the NFS Port from the instances because they are in the security group)

![changesg](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFSchangesg.png)

#### Mount EFS File System

sudo mount -t efs -o tls fs-070d39c6ec8f92f0f.efs.eu-central-1.amazonaws.com:/ ~/efs-mount-point

#### Create directory and file into first EC2 instance

![test1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFStest1.png)

#### View created directory and file in second EFS instance

![test2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/EFStest2.png)


We have launched two instances and attached them to an EFS file system and we can read and write data from multiple availability zones to the same EFS file system

