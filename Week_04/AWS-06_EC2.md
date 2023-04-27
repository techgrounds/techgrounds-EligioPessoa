# Elastic Compute Cloud (EC2)
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen

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
