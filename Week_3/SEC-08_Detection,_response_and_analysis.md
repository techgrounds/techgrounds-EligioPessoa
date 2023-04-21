# Detection, response and analysis


## Key-terms

- **Intrusion Detection System (IDS)**:Een _passieve_ monitoring oplossing voor het detecteren van cyberbeveiligingsbedreigingen voor een organisatie. Als een potentiële indringing is gedectecteerd, genereert de IDS een alert die beveiligingspersoneel notifieert om het incident te onderzoeken en corrigerende maatregelen te nemen.
- **Intrusion Prevention System (IPS)**: Een _actieve_ beschermingssyteem die, zoals de IDS, potentiële bedreigingen identificeert gebaseerd op de monitoringsfuncties van een beschermde host of netwerk, en _signature_, _anomaly_ of _hybrid detectie_ methodes kan gebruiken. In tegenstelling tot een IDS, een IPS neemt actie om een geïdentificeerde bedreiging te blokkeren of verhelpen. Een IPS kan aan de bel trekken, maar het helpt ook om indringingen te voorkomen.
- **Systems Hardening**: Een verzameling van tools, technieken en beste praktijken om de kwetsbaarheid te verminderen in technologische toepassingen, systemen, infrastructuur, firmware en andere gebieden. Het doel vanSystems Hardening is om beveiligingsrisicos te verminderen door potentiële aanvalsvectoren te elimineren en het aanvalsoppervlak van het systeem te verkleinen. 

## Opdracht
### Gebruikte bronnen

https://www.checkpoint.com/cyber-hub/network-security/what-is-an-intrusion-detection-system-ids/ids-vs-ips/

https://www.grcilaw.com/blog/what-is-cyber-incident-response

https://www.beyondtrust.com/resources/glossary/systems-hardening

### Ervaren problemen
Het feite dat er geen vastgestelde aantal stappen is voor Hack Response Strategies, waardoor ik moest kiezen naar wat het meest geschikt leek.

### Resultaat


### Hack response strategies.

Er zijn verschillende aanpakken om te reageren op een hackaanval, maar de meest gewone zijn:


- 1) Voorbereiding (Preparation): Een effectieve _incident response plan_ geeft richtlijnen voor de stappen die een organisatie moet nemen voordat een storend incident zich voordoet. Het plan begint met een schema van hoe een organisatie het risico op een datalek moet verkleinen. De voorbereiding moet organisatie richtlijnen over data beveiliging in lijn brengen metbeveiligingsdoelen en technologische verdedigingen. Medewerkers moeten minimaal getraind worden op _information security awareness_.
- 2) Identificeren (Identification): De stappen dat een organisatie moet nemen om te identificeren als een systeem gecompromitteerd is. Hoe sneller het geïdentificeerd is, hoe beter men in staat is om een aanval tegen te werken. De volgende vragen horen beantwoord te worden:
  - Wie heeft de inbreuk ontdekt?
  - Wat is de omvang van de inbreuk?
  - Heeft het invloed op onze bedrijfsvoering?
  - Wat is de bron?
- 3) Inperking (Containment): De stappen die genomen moeten worden om de shcade te beperken als je eenmaal bent geschonden. Dit kan betekenen actie ondernemen om de criminele hacker van het systeem te verwijderen of om de reeds gecompromitteerde data te isoleren. Tijdens deze fase, moet er overwogen worden of systemen offline moeten worden gehaald of verwijderd, en of onmiddelijke stappen ondergenomen kunnen worden om kwetsbaarheden te dichten.
- 4) Uitbanning (Eradication): Het verhelpen van de kwetsbaarheden die het datalek mogelijk maakte. Het hangt af van het soort incident, maar er moet bepaald worden hoe informatie gecompromiteerd was, en hoe het risico verwijderd kan worden.
- 5) Herstel (Recovery): Als de bedreiging verwijderd is, moet het systeem terug online komen. Zonder een goede herstel proces, het systeem kan kwetsbaar blijven voor dergelijke aanvallen, wat de schade zal vergroten.
- 6) Leren ervan (Lessons Learned): Het incident moet beoordeeld worden en verbetermogelijkheden horen geïdentificeerd te worden. Iedereen in de _incident response team_ hoort samen te komen om te evalueren welke delen van het plan goed zijn gegaan en welke problemen zijn ze tegengekomen. Men hoort iedere stap uit het proces te beoordelen, discusseren wat er gebeurd is, waarom het is gebeurd, wat er gedaan werd om de situatie in te houden, en wat anders gedan had kunne worden. Dit gesprek moet plaatsnemen tussen één en twee weken na de beveiligingsincident - lang genoeg om een overweging er over te maken, maar kort genoeg dat iedereen het nog kan onthouden.



## Exercise:
### A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?



### An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?
