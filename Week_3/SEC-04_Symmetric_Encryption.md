# Symmetric encryption

Het idee van encryptie is om data over te zetten naar een form waar de originele betekenis _vermomd_ is, en alleen degenen die toestemming hebben het kunnen ontcijferen. Dit wordt gedaan door de informatie te door elkaar te halen met wiskundige functies gebaseerd op een nummer, die we een _key_ noemen. Een omgekeerde  proces wordt gebruikt om de informatie weer "samen te zetten", of decoderen.

In het geval dat dezelfde sleutel gebruikt wordt om te versleutelen en decoderen, heet het proces _Symmetric Encryption_.

## Key-terms


- **Cipher**: Een cipher is een _algoritme_ om _encryptie_ of _decryptie_ uit te voeren, oftewel een serie van gedefinieerde stappen die als een procedure gevolgd kan worden.
- **Caesar cipher**: een van de eenvoudigste en meest bekende versleuteltechnieken. Het is een _substitutie cipher_ waarin iedere letter inhet bericht vervangen wordt door een letter op een bepaald nummer van posities verder in het alfabet.



## Opdracht
### Gebruikte bronnen



https://thesecmaster.com/a-mathematical-explanation-of-the-diffie-hellman-key-exchange-protocol/

https://cryptotools.net/aes

https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

https://www.geeksforgeeks.org/vigenere-cipher/

https://www.geeksforgeeks.org/hill-cipher/

https://www.jscape.com/blog/cipher-suites

https://sites.google.com/site/danzcosmos/home

https://www.precisely.com/blog/data-security/aes-vs-rsa-encryption-differences

### Ervaren problemen
Ik had de Diffie Helman Key Exchange protocol willen uitvoeren, maar merkte dat iedereen andere route nam en een embedded bericht met de key zette op een afbeelding, en uiteindelijk moest ik dat ook doen, omdat niemand in staat bleek te zijn om de key exchange met mij uit te voeren. Hier was het voor mij moeilijk schakelen naar wat de rest van de groep aan het doen was.

### Resultaat

### Find one more historic cipher besides the Caesar cipher.

- **Vigenère Cipher**: een methode om alfabetische text te encrypteren met een simpele for van _polyalfabetische substitutie_. De encryptie van de originele tekst is gedaan met de _Vigenère tafel_. Die bestaat uit het alfabet die 26 keer herhaald wordt in verschillende rijen, en op elke rij verschuift het alfabet éénmaal naar links, waardoor het overeenkomt met de 26 mogelijke _Caesar ciphers_. De mogelijke combinaties worden bepaald door een _sleutelwoord_.

![Vigenère table](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-04_Vigen%C3%A8re_square_shading.png)


### Find two digital ciphers that are being used today.

- **Advanced Encryption Standard (AES)**: AES is een symmetrische algoritme die dezelfde sleutel van 128, 192 of 256 bits gebruikt voor allebei versleuteling en decodering. Hoe langer de sleutel is, hoe veiliger. Bijvoorbeeld, een sleutel die 128 bit lang is heeft 2^128 mogelijke waarden, en de snelste supercomputers van tegenwoordig zouden meer dan 100000000000000 jaar nodig hebben om het te ontkraken.

- **RSA Encryption**: RSA is genoemd naar de MIT wetenschappers (Rivest, Shamir, en Adleman) die het uitgevonden hebben in 1977. Het is een asymmetrische algoritme die een publiek bekend sleutel gebruikt voor encryptie, maar een andere sleutel gebruikt om te decoderen, die alleen bekend is door de ontvanger.



### Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. You are not allowed to use any private messages or other communication channels besides the public Slack channel. Analyse the shortcomings of symmetric encryption for sending messages.


In het gebruikte methode, is het bericht vrij makkelijk te ontcijferen, omdat alles openbaar te zien is. Met de Diffie-Helman methode zou het al niet meer zo simpel zijn, omdat het ontworpen is om in het openbaar een sleutel te creëren die toch veilig is.


![Elígio](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-04_Eligio.png)
![Elígio bericht](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-04_Eligio2.png)
![Curt cipher](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-04_Curt3.png)
![Curt bericht 1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-04_Curt.png)
![Curt bericht 2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/SEC-04_Curt2.png)
