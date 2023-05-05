# Aurora
AWS RDS Aurora is een relationele database-engine die de snelheid en betrouwbaarheid van hoogwaardige commerciële databases combineert met de eenvoud en kosteneffectiviteit van open-source databases.

Het heeft hogere capaciteiten dan AWS RDS, en ook exclusieve services, zoals:

- **Aurora Global Database**: Aurora biedt de mogelijkheid om een enkele database te creëren die meerdere regio's omvat. Met deze functie kan je gegevens met een lage latentie repliceren naar verschillende regio's, waardoor noodherstel mogelijk wordt en de leeslatentie voor wereldwijd gedistribueerde applicaties wordt verminderd.
- **Parallel Query**: Aurora gebruikt een gedistribueerde architectuur waarmee het parallel query's kan uitvoeren over meerdere knooppunten. Deze functie verbetert de queryprestaties aanzienlijk voor grote tabellen met miljarden rijen.
- **Fault-tolerant storage**: Aurora maakt gebruik van een gedistribueerd opslagsysteem dat gegevens repliceert over meerdere knooppunten in meerdere _availability zones_, waardoor zeer duurzame en beschikbare opslag voor je database wordt geboden. 
- **Aurora Backtrack**: Aurora biedt een functie genaamd "Aurora Backtrack" waarmee je een database kunt terugdraaien naar een specifiek tijdstip zonder dat je een back-up hoeft te herstellen. Deze functie kan handig zijn om onbedoelde wijzigingen in je database snel ongedaan te maken.
- **Aurora Serverless**: Hiermee kan je een Aurora-database maken en beheren zonder dat je database-instances of -clusters hoeft in te richten of te beheren. In plaats daarvan schaalt Aurora Serverless automatisch de rekencapaciteit op basis van de databaseworkload.


## Key-terms


## Opdracht
### Gebruikte bronnen

(How to create an Amazon Aurora Global Database) https://www.youtube.com/watch?v=Q7jU1QpP9oQ

https://dev.to/aws-builders/create-and-connect-to-rds-aurora-serverless-mysql-database-thru-cloud9-2djo

https://www.percona.com/blog/when-should-i-use-amazon-aurora-and-when-should-i-use-rds-mysql/


### Ervaren problemen

Geen problemen ervaren

### Resultaat

#### Create Security Group for accessing Aurora

![aurorasgedit](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Aurorasgedit.png)

#### Connect Cloud9 to Aurora instance

![auroraendpoint](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/auroraendpoint.png)
![auroraconnected](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/auroraconnected.png)

#### Create Aurora Database in different Region

![auroracreatesecond](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Auroracreate%20second.png)
![auroracreatesecond2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Auroracreatesecond2.png)

#### Remove cluster from first Global Database , and promote it to another Global Database

![Auroraremovepromote](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Auroraremovepromote.png)
![aurora2ndglobal](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Aurora2ndglobal.png)
