# Processes

Processen in Linux kunnen verdeeld worden in drie categorieën: Daemons, Services en Programma's.

Een daemon werkt in de achtergrond en is non-interactief. Een Service verwerkt verzoeken van programma's, en kan interactief zijn. Een programma wordt toegepast en gebruikt door gebruikers.




## Key-terms

telnet - Een netwerk protocool gebruikt om virtuele toegang naar een computer te krijgen en om een wederzijdse, collaboratieve, tekst gebaseerde communicatie kanaal te maken tussen twee machines.

process - Een programma die gerund wordt. Een werkende instantie van een programma. Iedere uitgevoerde command begint een process.

systemctl command - Beheert configuraties van systeem en services, en stelt administrators in staat de OS te beheren en de status van services te controleren.


## Opdracht
### Gebruikte bronnen

[How to install Telnet](https://adamtheautomator.com/linux-to-install-telnet/)

[Phoenixnap](https://phoenixnap.com/kb/telnet-linux)

[How to start, stop, and restart services in Linux](https://www.techrepublic.com/article/how-to-start-stop-and-restart-services-in-linux/)

[telnetd vs inetd](https://sites.ualberta.ca/dept/chemeng/AIX-43/share/man/info/C/a_doc_lib/cmds/aixcmds5/telnetd.htm)



### Ervaren problemen


Er was wat verwarring over het feite dat de telnetd daemon niet getoond wordt. Verder onderzoek liet weten dat de inetd daemon is degene die de telnetd daemon opstart, en daardoor daadwerkelijk degene was die ik moest hebben.

### Resultaat

![Start Telnetd en Status check](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/startstatus.png)

![Kill Process](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/stop.png)
