# Detection, response and analysis


## Key-terms

- **Intrusion Detection System (IDS)**: Een _passieve_ monitoringsoplossing voor het detecteren van cyberbeveiligingsbedreigingen voor een organisatie. Als een potentiële indringing is gedectecteerd, genereert de IDS een alert die beveiligingspersoneel notifieert om het incident te onderzoeken en corrigerende maatregelen te nemen.
- **Intrusion Prevention System (IPS)**: Een _actieve_ beschermingssyteem die, zoals de IDS, potentiële bedreigingen identificeert gebaseerd op de monitoringsfuncties van een beschermde host of netwerk, en _signature_, _anomaly_ of _hybrid detectie_ methodes kan gebruiken. In tegenstelling tot een IDS, een IPS neemt actie om een geïdentificeerde bedreiging te blokkeren of verhelpen. Een IPS kan aan de bel trekken, maar het helpt ook om indringingen te voorkomen.
- **Systems Hardening**: Een verzameling van tools, technieken en beste praktijken om de kwetsbaarheid te verminderen in technologische toepassingen, systemen, infrastructuur, firmware en andere gebieden. Het doel vanSystems Hardening is om beveiligingsrisicos te verminderen door potentiële aanvalsvectoren te elimineren en het aanvalsoppervlak van het systeem te verkleinen. 
- **Disaster Recovery (DR)**: DR is het vermogen van een organisatie te reageren op en te herstellen van een gebeurtenis die de bedrijfsvoering negatief beïnvloedt. Het doel van DR methoden is om de organisatie in staat te stellen om zo snel mogelijk na een calamiteit weer gebruik kunnen maken van kritieke systemen en IT-infrastructuur. Om zich hierop voor te bereiden voeren organisaties vaak een diepgaande analyse van hun systemen uit en stellen ze een formeel document op dat ze kunnen volgen in tijden van crisis. Dit document staat bekend als _disaster recovery plan_, of een noodherstelplan.
- **Recovery Time Objective (RTO)**:  De tijdsduur waarbinnen een bedrijfsproces hersteld moet worden na een calamiteit om onaanvaardbare gevolgen van een continuïteistsonderbreking te voorkomen. 
- **Recovery Point Objective (RPO)**:  Het tijdsinterval dat tijdens een storing kan verstrijken voordat de hoeveelheid verloren gegevens gedurende die periode de maximaal toegestane drempel van het bedrijfscontinuiteitsplan overschrijdt.

## Opdracht
### Gebruikte bronnen

https://www.checkpoint.com/cyber-hub/network-security/what-is-an-intrusion-detection-system-ids/ids-vs-ips/

https://www.grcilaw.com/blog/what-is-cyber-incident-response

https://www.beyondtrust.com/resources/glossary/systems-hardening

https://www.techtarget.com/searchdisasterrecovery/definition/disaster-recovery

https://cloudian.com/guides/disaster-recovery/disaster-recovery-solutions-top-5-types-and-how-to-choose/

https://www.druva.com/blog/understanding-rpo-and-rto



### Ervaren problemen
Het feite dat er geen vastgestelde aantal stappen is voor Hack Response Strategies, waardoor ik moest kiezen naar wat het meest geschikt leek.

### Resultaat

Study:

### Hack response strategies.

Er zijn verschillende aanpakken om te reageren op een hackaanval, maar de meest gewone zijn:


**1) Voorbereiding (Preparation)**: Een effectieve _incident response plan_ geeft richtlijnen voor de stappen die een organisatie moet nemen voordat een storend incident zich voordoet. Het plan begint met een schema van hoe een organisatie het risico op een datalek moet verkleinen. De voorbereiding moet organisatie richtlijnen over data beveiliging in lijn brengen metbeveiligingsdoelen en technologische verdedigingen. Medewerkers moeten minimaal getraind worden op _information security awareness_.

**2) Identificeren (Identification)**: De stappen dat een organisatie moet nemen om te identificeren als een systeem gecompromitteerd is. Hoe sneller het geïdentificeerd is, hoe beter men in staat is om een aanval tegen te werken. De volgende vragen horen beantwoord te worden:
  - Wie heeft de inbreuk ontdekt?
  - Wat is de omvang van de inbreuk?
  - Heeft het invloed op onze bedrijfsvoering?
  - Wat is de bron?

**3) Inperking (Containment)**: De stappen die genomen moeten worden om de shcade te beperken als je eenmaal bent geschonden. Dit kan betekenen actie ondernemen om de criminele hacker van het systeem te verwijderen of om de reeds gecompromitteerde data te isoleren. Tijdens deze fase, moet er overwogen worden of systemen offline moeten worden gehaald of verwijderd, en of onmiddelijke stappen ondergenomen kunnen worden om kwetsbaarheden te dichten.

**4) Uitbanning (Eradication)**: Het verhelpen van de kwetsbaarheden die het datalek mogelijk maakte. Het hangt af van het soort incident, maar er moet bepaald worden hoe informatie gecompromiteerd was, en hoe het risico verwijderd kan worden.

**5) Herstel (Recovery)**: Als de bedreiging verwijderd is, moet het systeem terug online komen. Zonder een goede herstel proces, het systeem kan kwetsbaar blijven voor dergelijke aanvallen, wat de schade zal vergroten.

**6) Leren ervan (Lessons Learned)**: Het incident moet beoordeeld worden en verbetermogelijkheden horen geïdentificeerd te worden. Iedereen in de _incident response team_ hoort samen te komen om te evalueren welke delen van het plan goed zijn gegaan en welke problemen zijn ze tegengekomen. Men hoort iedere stap uit het proces te beoordelen, discusseren wat er gebeurd is, waarom het is gebeurd, wat er gedaan werd om de situatie in te houden, en wat anders gedan had kunnen worden. Dit gesprek moet plaatsnemen tussen één en twee weken na de beveiligingsincident - lang genoeg om een overweging er over te maken, maar kort genoeg dat iedereen het nog kan onthouden.


### Soorten noodherstelopties (Disaster Recovery Options):

**1) Data Center Disaster Recovery / Data Center Rampenherstel**

Organisaties met eigen datacenters moeten een strategie voor noodherstel implementeren die alle componenten van de IT infrastructuur in het datacenter en de omliggende fysieke faciliteit aanpakt. Deze strategie draait meestal om _back-ups_ naar _failover sites_ die zijn ondergebracht in secundaire datacenters of co-locatie faciliteiten. IT en zakelijke leiders moeten de verschillende componenten van deze fysieke faciliteiten documenteren, waaronder verwarming, koeling, stroom, brandbestrijding en beveiligingscontroles.

**2) Network Disaster Recovery / Netwerk Noodherstel**

Netwerkconnectiviteit is essentieel voor externe en interne communicatie, toegang tot applicaties en het delen van gegevens in het geval van een ramp. De strategie voor netwerkherstel bij calamiteiten moet een plan bevatten om netwerkservices te herstellen en toegang tot backup gegevens en secundaire opslaglocaties te garanderen.

**3) Virtualized Disaster Recovery / Gevirtualiseerde Noodherstel**

Organisaties kunnen virtualisatie gebruiken om workloads naar een secundaire locatie of cloudomgeving te repliceren voor noodherstel. Gevirtualiseerde DR is flexibel, eenvoudig te implementeren, snel en efficiënt - gevirtualiseerde workloads hebben een kleine IT footprint, ondersteunen frequente replicatie en maken snelle failover-initiatie mogelijk. Verschillende leveranciers van databescherming bieden virtuele DR en backup producten.

**4) Disaster Recovery in the Cloud / Noodherstel in de Cloud**

Met veel beschikbare cloudservices kunnen organisaties DR systemen hosten in een cloudomgeving in plaats van op een fysieke locatie. DR in de cloud omvat meer dan backup in de cloud. IT teams moeten automatische failover van de werklast naar het DR cloudplatform configureren voor onmiddelijk herstel wanneer zich een storing voordoet.

**5) Disaster Recovery as a Service (DRaaS)**

Met DRaaS kan een organisatie haar virtuele en fysieke servers repliceren en hosten op de infrastructuur van een derde partij. De DR dienstverlener is verantwoordelijk voor de uitvoering van het calamiteitenplan tijdens een crisis op basis van de service level agreement.





### Exercise:
- A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?

De RPO is de maximale hoeveelheid tijd die kan verstrijken voordat de aantal verloren data onacceptabel is. Aangezien er geen informatie is over de bedrijfsdoelen, we kunnen alleen zeggen dat **de RPO van de database is 24 uur.**

- An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?


RTO is de lengte van tijd waarin bedrijfsprocessen hersteld moeten worden na een storing. Omdat er verder geen informatie is over bedrijfsdoelen, kan er alleen gezegd worden dat **de RTO van de website is 8 minuten.**
