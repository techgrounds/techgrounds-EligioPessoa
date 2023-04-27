# Elastic Block Store (EBS)
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen


https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

https://stackoverflow.com/questions/25838962/permission-denied-when-accessing-new-ebs-volume



### Ervaren problemen

- Ik kon geen tekstbestand creëren in de folder waar het moest staan. Het aanpassen van eigenaarschapsrechten loste dit op.
- Het Internet viel uit tijdens de opdracht, waardoor ik mijn stappen moest herhalen
- Op de laatste fase, lukte het mij niet om de tweede volume te mounten. Na herstarten lukte het wel

### Resultaat

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
