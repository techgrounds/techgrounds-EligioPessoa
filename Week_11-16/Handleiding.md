## Download en installeer benodigde programma's

- Visual Studio Code
- Python

## Zorg dat je een AWS account hebt, met administrator rechten

## Download en instaleer node.js vanuit https://nodejs.org/

### Download de AWS extensie voor Visual Studio Code
- configureer het om VSCode te koppelen aan je account
 


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


