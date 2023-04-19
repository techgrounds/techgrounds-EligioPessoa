# Firewalls
Een _firewall_ beschermt je computer of netwerk van externe cyberaanvallers door gevaarlijke of overbodige netwerkverkeer uit te filteren. Firewalls kunnen ook voorkomen dat schadelijke malware toegang krijgt tot een computer of netwerk via het Internet.

## Key-terms


- **Firewall**: Een netwerk beveiligingsapparaat of software die _inkomende _en _uitgaande netwerkverkeer_ monitort, en bepaalt of specifieke verkeer toegelaten of geblokkeerd moetworden volgens een gedefinieerde set van beveiligingsregels. Voor de doelen van dit opdracht zijn er deze soorten firewalls te bespreken:
  - **Stateful Firewall**: Een firewall die een status onderhoudt, of informatie bewaart over actieve netwerk verbindingen. Als er een verbinding wordt gemaakt, begint de firewall het na te sporen, en vernieuwt zijn interne status als nieuwe pakketten geïnspecteerd en verwerkt worden door de firewall.
  - **Stateless Firewall**: het verschilt van een _stateful firewall_ omdat het geen interne status onderhoudt tussen een pakket en de andere. In plaats daarvan, is elk pakket geevalueerd op basis van de data die in zijn header staat.
  - **Hardware Firewall**: Een fysieke apparaat die netwerkverkeer naar een computer filtert. Terwijl normaal gesproken een netwerkkabel direct aan een computer of server verbbonden zou zijn, is die in dit geval eerst gekoppeld aan de firewall. De firewall zit tussen de externe netwerk en de server, waarmee een antivirus oplossing en een barriére wordt verstrekt tegen


Er zijn meerdere soorten firewalls zoals:

- **Proxy Firewall**: Een proxy firewall dient als de gateway tussen een netwerk naar een andere voor een specifieke doel. Proxy servers kunnen aanvullende functionaliteit leveren, zoals _content caching_ en beveiligin door directe verbindingen van buiten het netwerk te blokkeren.
- **Unified Threat Management (UTM) Firewall**: Een UTM combineert de functies van een _stateful firewall_ met _intrusion prevention_ en _antivirus_. Het kan ook andere diensten omvatten.
- **Next Generation Firewall**: Een NGFW is meer geavanceerd en omvat diensten zoals: _Integrated Intrusion Prevention System_; _application awareness_ om risicovolle apps te blokkeren; URL filtering gebaseerd op geolocatie en reputatie; _Intelligence-based_ toegangscontrole met _stateful inpection_.
- **Threat Focused NGFW**: Alle capaciteiten van een traditionele NGFW en ook geavanceerde _threat detection adn remediation_.
- **Cloud Native Firewall**: Met geautomatiseerde scaling functies, Cloud Native Firewalls laten netwerk operaties en beveiligingsoperaties snel runnen.


## Opdracht
### Gebruikte bronnen

https://www.checkpoint.com/cyber-hub/network-security/what-is-firewall/what-is-a-stateful-firewall/stateful_vs_stateless_firewall/

https://www.cisco.com/c/en/us/products/security/firewalls/what-is-a-firewall.html



https://askubuntu.com/questions/857609/apache2-now-pointing-to-new-default-page

https://www.linode.com/community/questions/17215/cant-reach-default-apache-page-trough-ip

http://didgeridoo.une.edu.au/

https://stackoverflow.com/questions/28558145/how-to-open-default-page-in-browser-from-apache-web-server

https://www.inmotionhosting.com/support/security/open-a-port-in-ufw/

https://linuxize.com/post/how-to-list-and-delete-ufw-firewall-rules/


### Ervaren problemen

- Ik wist niet hoe ik mijn Apache startpagina moest visualiseren in de browser, omdat ik niet door had dat ik de server IP samen met mijn poort nummer moest gebruiken ipv de IP van mijn VM.
- Er was verwarring over het feite dat de startpagina werd nog steeds getoond nadat ik port 80 had geblokkeerd. Ik heb later uitgevonden dat nog in mijn cache stond; zodra ik mijn Apache startpagina open deed in _private browsing_, kon ik de resultaten zien die ik verwachtte.

### Resultaat


![UFW](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/statusufw.png)
![Apache](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/apache.png)
