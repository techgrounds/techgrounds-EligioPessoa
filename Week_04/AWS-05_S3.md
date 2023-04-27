# Simple Storage Service (S3)

Amazon Simple Storage Service (Amazon S3) is een schaalbare, snelle, webgebaseerde cloudopslagservice. De service is ontworpen voor online back-up en archivering van gegevens en applicaties op Amazon Web Services (AWS). Amazon S3 is ontworpen met een minimale functieset en gemaakt om web-scale computing eenvoudiger te maken voor developers.

## Key-terms

- **S3**: Amazon S3 is een objectopslagservice die verschilt van andere soorten cloud computing-opslagtypen, zoals blok- en bestandsopslag. Elk object wordt opgeslagen als een bestand met de bijbehorende metadata. Het object krijgt ook een ID-nummer. Applicaties gebruiken dit ID-nummer om toegang te krijgen tot objecten.
De S3-cloudservice voor objectopslag geeft een abonnee toegang tot dezelfde systemen die Amazon gebruikt om zijn eigen websites te beheren. Met S3 kunnen klanten vrijwel elk bestand of object met een grootte tot 5 terabyte (TB) uploaden, opslaan en downloaden - met een maximum van 5 gigabyte (GB) voor de grootste enkele upload.


- **Bucket**: Een Amazon S3 bucket is een _public cloud_ opslag _resource_ die beschikbaar is op het AWS S3 platform. Het biedt objectgebaseerde opslag, waarbij gegevens worden opgeslagen in S3-buckets in afzonderlijke eenheden die _objecten_ worden genoemd in plaats van bestanden.
Amazon S3-buckets zijn vergelijkbaar met bestandsmappen en kunnen worden gebruikt voor het opslaan, ophalen, back-uppen en openen van objecten. Elk object heeft drie hoofdcomponenten: de inhoud of gegevens van het object, een unieke identificatie voor het object en de beschrijvende metagegevens, waaronder de naam, URL en grootte van het object.
Een object moet binnen een bucket bestaan, omdat het niet alleen kan bestaan. Elk Amazon-account kan honderden buckets hebben, die elk een groot aantal objecten bevatten.

## Opdracht
### Gebruikte bronnen

https://www.techtarget.com/searchaws/definition/AWS-bucket

https://www.techtarget.com/searchaws/definition/Amazon-Simple-Storage-Service-Amazon-S3

https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html#step2-create-bucket-config-as-website

https://www.youtube.com/watch?v=mDRoyPFJvlU (Amazon/AWS S3 (Simple Storage Service) Basics | S3 Tutorial, Creating a Bucket | AWS for Beginners)

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

#### Exercise 1:
#### Create new S3 bucket with the following requirements:
Region: Frankfurt (eu-central-1)

![createbucket](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05create.png)

#### Upload a cat picture to your bucket.

![s3object](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05s3object.png)


#### Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.

![share](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05share.png)
![presigned](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05presigned.png)
![shared](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05shared.png)


#### Exercise 2:
#### Create new bucket with the following requirements:
Region: Frankfurt (eu-central-1)
Upload the four files that make up AWS’ demo website.
Enable static website hosting.

![enablestatic](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05enablestatic.png)
![info](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05infowebsite.png)
#### Share the bucket website endpoint with a peer. Make sure they are able to see the website.

![website](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/AWS-05staticwebsite.png)
