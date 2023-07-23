## Download en installeer benodigde programma's

- Visual Studio Code
- Python

## Zorg dat je een AWS account hebt, met administrator rechten
- Download en installeer AWS CLI.

### Download en instaleer node.js vanuit https://nodejs.org/

### Download de AWS extensie voor Visual Studio Code
- Configureer het om VSCode te koppelen aan je account
 


## In de CLI van Visual Studio Code, voer uit de volgende commando's:



- Instaleer pip voor python:

```
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```


## Maak een nieuwe project folder aan:

```
mkdir pro-01-cdk
cd pro-01-cdk
cdk init app --language python
python -m pip install -r requirements.txt

```

- Copieer het bestand 'pro-01-cdk.py' naar de folder "~/pro-01-cdk/pro_01_cdk"


- In de terminal, voer uit de command "cdk synth" in de folder "~/pro-01-cdk"


(Versie 1.1: Doe hetzelfde voor de folder van versie 1.1)


# Provisionele toepassingen om de stack te kunnen deployen

## SSL certificaat creëren en uploaden

De volgende commands horen uitgevoerd te worden in de (VSCode) CLI

- Volg de aanwijzingen om je eigen SSL certificaat te creëren: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html

- Vervolgens upload je certificaat naar ACM: 
`aws acm import-certificate --certificate fileb://path_to/certificate.pem --private-key fileb://path_to/privatekey.pem`

- Copieër de ARN nummer van de certificaat, en plaats het in plaats van degene die nu op `# Import an existing SSL certificate` staat.

## Creër een key pair:

- Creër een key-pair en bewaar de private key in een locale bestand: `aws ec2 create-key-pair --key-name your_key --query 'KeyMaterial' --output text > your_key.pem`
- Als je vanuit Windows werkt, zorg dat de key in de goede formaat is: save file as UTF-8
- In het bestand Pro-1_1_cdk_stack.py, vervang bij `def setup_ec2` en `def setup_ec2` de `key_name` met je eigen key.




## Web Server AMI creëren

- Copiëer uit de repository het bestand "linux_script.txt"
- Maak een default VPC aan, als je nog geen hebt: `aws ec2 create-default-vpc`
- Zorg dat je default security group HTTP (Port 80) toestaat:
 - - Security group ID: `aws ec2 describe-security-groups --filter Name=group-name,Values=default --query 'SecurityGroups[*].[GroupId,GroupName]' --output text`
 - Allow HTTP: `aws ec2 authorize-security-group-ingress --group-id sg-0123456789abcdef0 --protocol tcp --port 80 --cidr 0.0.0.0/0`
- Creër een instance: `aws ec2 run-instances --image-id ami-0aea56f3589631913 --instance-type t2.micro --user-data file://linux_script.txt`
- Wacht een minuut of twee, dan voer deze command uit: `aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].InstanceId"`
- Copiëer de instance ID, en plaats het in deze command: `aws ec2 create-image --instance-id i-xxxxxxxxxxxxxxxxx --name "My server" --description "An image for my server" --no-reboot`
- Copiëer de Image Id die verschjint, en plaats het in de cdk bij: `# Get the ID of the existing AMI`
- Verwijder de instance: `aws ec2 terminate-instances --instance-ids i-xxxxxxxxxxxxxxxx`
- Verwijder je security group regel: `aws ec2 revoke-security-group-ingress --group-id sg-0123456789abcdef0 --protocol tcp --port 80 --cidr 0.0.0.0/0`

## Management Server AMI creëren

- Copiëer uit de repository het bestand "windows_script.txt"
- Maak een default VPC aan, als je nog geen hebt: `aws ec2 create-default-vpc``
- Zorg dat je default security group alle verkeer toestaat:
  - Security group ID: `aws ec2 describe-security-groups --filter Name=group-name,Values=default --query 'SecurityGroups[*].[GroupId,GroupName]' --output text`
  - Allow All Traffic: `aws ec2 authorize-security-group-ingress --group-id sg-0123456789abcdef0 --protocol -1 --cidr 0.0.0.0/0`
- Creër een instance: aws ec2 run-instances --image-id ami-0df2883917b75bae7 --instance-type t2.micro --user-data file://windows_script.txt --key-name your_key
- Wacht een minuut of twee, dan voer deze command uit:  `aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].InstanceId"`
- Copiëer de instance ID, en plaats het in deze command: `aws ec2 create-image --instance-id i-xxxxxxxxxxxxxxxxx --name "Management Server" --description "Windows Server Image" --no-reboot`
- Zorg dat je het wachtwoord kopieërt: `aws ec2 get-password-data --instance-id i-071c319d280a861d5 --priv-launch-key pexp3.pem --query 'PasswordData' --output text | Set-Content password.txt`
- Verwijder de instance: `aws ec2 terminate-instances --instance-ids i-xxxxxxxxxxxxxxxx`
- Verwijder je security group regel: `aws ec2 revoke-security-group-ingress --group-id sg-0123456789abcdef0 --protocol -1 --cidr 0.0.0.0/0`

# Als alles klaar is:

- Deploy je stack de CLI, in de folder waar het project staat:

`cdk deploy --context ip_address=your_ip/32`

