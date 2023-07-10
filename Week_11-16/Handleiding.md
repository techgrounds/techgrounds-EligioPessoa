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


- In de terminal, voer uit de command "cdk deploy" in de folder "~/pro-01-cdk"


(Versie 1.1: Doe hetzelfde voor de folder van versie 1.1)


# Provisionele toepassingen om de stack te kunnen deployen

## SSL certificaat creërenen en uploaden

De volgende commands horen uitgevoerd te worden in de (VSCode) CLI

- Volg de aanwijzingen om je eigen SSL certificaat te creëren: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html

- Vervolgens upload je certificaat naar ACM: 
`aws acm import-certificate --certificate fileb://path_to/certificate.pem --private-key fileb://path_to/privatekey.pem`

- Copieër de ARN nummer van de certificaat, en plaats het in plaats van degene die nu op `# Import an existing SSL certificate` staat.

## Web Server AMI creëren

- Copiëer uit de repository het bestand "my_script.txt"
- Maak een default VPC aan, als je nog geen hebt: `aws ec2 create-default-vpc``
- Creër een instance: `aws ec2 run-instances --image-id ami-0aea56f3589631913 --instance-type t2.micro --user-data file://my_script.txt`
- Wacht een minuut of twee, dan voer deze command uit: `aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].InstanceId"`
- Copiëer de instance ID, en plaats het in deze command: `aws ec2 create-image --instance-id i-xxxxxxxxxxxxxxxxx --name "My server" --description "An image for my server" --no-reboot`
- Copiëer de Image Id die verschjint, en plaats het in de cdk bij: `# Get the ID of the existing AMI`

## Creër een key pair:

- `aws ec2 create-key-pair --key-name exp3 --query 'KeyMaterial' --output text > exp3.pem`
- Copiëer de private key die vertoond wordt
- Bij ec2 instance connect voer de volgende commands uit:
```
nano ~/.ssh/exp3.pem

chmod 400 ~/.ssh/exp3.pem

ssh -i ~/.ssh/exp3.pem ec2-user@(ip van de instance waarmee je wilt verbinden)
```

