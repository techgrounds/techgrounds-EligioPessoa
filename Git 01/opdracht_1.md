# [Git en Github]
Git is een DevOps tool voor het beheren van broncode. Het staat teams toe om samen te werken aan dezelfde code zonder elkaar in de weg te zitten, en om terug te keren naar een werkende versie van de code wanneer er iets mis gaat. In zijn basisvorm wordt het met een Command Line Interface gebruikt.

GitHub is een Git hosting service. GitHub laat je repositories hosten en managen

## Key-terms

- Repository: Waar de bestanden van een project worden bewaard
- Main/Master: Het hoofd branch van een repository
- Branch: Een tak van de repository, die aangepast kan worden zonder dat de bestanden in de hoofdbranch geaffecteerd worden
- Commit: Actie die de huidige status van een repository vaststelt.
- Push: Het uploaden van repository inhoud van een locale bron naar een remote repository
- Clone: Het downloaden van remote repository inhoud naar een locale bron.


## Opdracht 1
### Gebruikte bronnen

Google Search

[GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

[A Cloud Guru tutorial](https://learn.acloud.guru/course/ec8e7da9-ecce-4215-ae1b-756396f23a2b/learn/f6695d49-bfb0-4414-84c9-4fd08527d166/5d900c69-b3f7-4ed1-a708-73306f11b1ac/lab/ee48386b-ce12-4804-9b20-27af29b12dab)

[FreeCodeCamp tutorial](https://www.freecodecamp.org/news/error-src-refspec-master-does-not-match-any-how-to-fix-in-git/)

[Mergify Blog](https://blog.mergify.com/how-to-merge-branches-in-github/)

### Ervaren problemen
In het begin kon ik niet achterkomen hoe ik de cloned repositories moest pushen naar mijn eigen repository. Na heel veel zoeken zag ik dat ik de repository van andere gebruikers moest clonen in de folder die al eerder uit mijn eigen account als eerste cloned moest worden. Daarna heb ik nog gecheckt hoe ik de naam van de bestemmings branch moest veranderen, om de repositories succesvol te kunnen pushen.

Daarna heb ik een pull request gecreërd, om de side branch te mergen met de main branch, en die request aangevaard.

### Resultaat
Aan de side branch pagina other-repositories kan ik nu de bestanden van de repositories van mijn collega's


![main branch](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/mainbranch.png)

![side branch](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/sidebranch.png)

![Younes repo](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Younesrepo.png)

![Danny repo](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Dannyrepo.png)

![Roan repo](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Roanrepo.png)

![Pull & Commit](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/Commit.png)

![Main branch - updated](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/mainupdated.png)
