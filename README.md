



# Tietoliikenteen sovellusprojekti
Tietoliikenteen sovellusprojekti on osa tieto- ja viestintätekniikan insinööriopintojen 2. vuoden kurssia. Tämä projekti yhdistää laitteisto-ohjelmoinnin, tietoliikenteen ja palvelinsovellukset. Projektin tavoitteena oli kehittää järjestelmä, joka pystyy keräämään, siirtämään ja tallentamaan reaaliaikaisia kiihtyvyysarvoja tietokantaan.
## Architecture
![Blank document (1)](https://github.com/user-attachments/assets/f0e6158f-fa61-4aba-8872-5d509d09ca10)
## Saimme käytännön kokemusta seuraavista aihealueista:
- Kiihtyvyysantureiden ja kehitysalustojen käyttö.
- Bluetooth-tiedonsiirto ja väliasemien ohjelmointi.
- Palvelin- ja tietokantasovellusten kehittäminen Pythonilla ja MySQL:llä.
- Koodin kirjoitusta koneoppimistarkoitukseen
- Monivaiheisen järjestelmän testaus ja virheenkorjaus.
## Projektin tavoitteet ja toteutus
Projektin päätavoitteena oli rakentaa toimiva tiedonsiirtojärjestelmä, joka:
1. Lukee kiihtyvyysanturin reaaliaikaisia arvoja (x-, y-, ja z-akselit).
2. Lähettää nämä arvot Bluetooth-yhteydellä Raspberry Pi:lle.
3. Tallentaa arvot MySQL-tietokantaan Linux-palvelimelle analysointia ja koneoppimista varten.
## Projektin toteutus eteni vaiheittain:
- Vaihe 1: Kiihtyvyysanturin integrointi ja ohjelmointi nRF5340 Development Kitillä.
- Vaihe 2: Bluetooth-yhteyden konfigurointi Raspberry Pi:n kanssa.
- Vaihe 3: Tietokannan suunnittelu ja yhteyden toteutus palvelimella.
- Vaihe 4: Kiihtyvyysanturin arvojen tallennus tietokantaan.
- Vaihe 5: Arvojen käyttäminen koneoppimistarkoituksiin
- Vaihe 6: Testaus, virheenkorjaus ja tekstitiedostojen viimeistely.
## Käytetyt Laitteet ja Teknologiat

- nRF5340 Development Kit (Kuva 1)
- Raspberry Pi 3 (Kuva 2)
- GY-61 ADXL335 Kolmiakselinen kiihtyvyysanturi (Kuva 3)
- Python: Käytettiin ohjelmointikielenä sekä nRF5340:ssä että Raspberry Pi:ssä.
- MySQL: Palvelimella käytetty tietokanta kiihtyvyysarvojen tallentamiseen.
- Linux-palvelin: Toimi keskeisenä tietokantapalvelimena

 ![image](https://github.com/user-attachments/assets/1154c2b3-b45e-4d4b-a344-be6c4a75de87)
 
1.	(nRF5340 Development Kit)

 ![image](https://github.com/user-attachments/assets/8a1605dc-d331-468e-a641-49ff65765393)
 
2.	(Raspberry Pi 3)

![image](https://github.com/user-attachments/assets/eac1498c-35f9-4b53-ad6c-eb86f3152ad3)
 
3.	(GY-61 ADXL335 3 akselinen kiihtyvyysanturi)

## Oppimiskokemukset ja haasteet
Projektin aikana opimme laajasti sekä ohjelmoinnin että järjestelmäintegraation käytännön soveltamista. Erityisesti Bluetooth-yhteyden vakauden varmistaminen sekä reaaliaikaisen tiedonkeruun ja tallennuksen yhteensovittaminen toivat arvokasta kokemusta. Haastavimmaksi osaksi paljastui koneoppimisen ymmärtäminen ja käyttäminen.

Haasteina olivat:
- Bluetooth-yhteyden konfigurointi eri laitteiden välillä.
- Anturien kalibrointi tarkkojen arvojen saamiseksi.
- Tietokantayhteyksien optimointi suurille datamäärille.
- Koneoppimisen KMeans algoritmin ymmärtäminen ja soveltaminen.
## Laitteiston linkit
[GY-61 Kiihtyvyysanturi](https://www.spelektroniikka.fi/p23824-gy-61-adxl335-3-akselinen-kiihtyvyysanturi-fi.html)

[nRF5340 Developement Kit](https://www.nordicsemi.com/Products/Development-hardware/nRF5340-DK)

[Raspberry Pi 3](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/)

## Yhteenveto
Tietoliikenteen Sovellusprojekti oli haastava ja hyvin taitoja testaava osa lukuvuotta, mutta todella opettavainen monesta eri alueesta alallamme. Projektin aikana saimme viettää monia tunteja ratkaisujen pohtimisessa, sekä eri toteutustapojen ideoimisessa. Vaikka projektin eri osat toivat monia haasteita, nämä haasteen tunteet saivat onnistumiset tuntumaan vain paremmalta.
