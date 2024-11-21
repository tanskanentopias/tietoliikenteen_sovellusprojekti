



# Tietoliikenteen sovellusprojekti
Tietoliikenteen sovellusprojekti on osa tieto- ja viestintätekniikan insinööriopintojen 2. vuoden kurssia. Tämä projekti yhdistää laitteisto-ohjelmoinnin, tietoliikenteen ja palvelinsovellukset. Projektin tavoitteena oli kehittää järjestelmä, joka pystyy keräämään, siirtämään ja tallentamaan reaaliaikaisia kiihtyvyysarvoja tietokantaan.
## Architecture
![Blank document (1)](https://github.com/user-attachments/assets/f0e6158f-fa61-4aba-8872-5d509d09ca10)
## Saimme käytännön kokemusta seuraavista aihealueista:
- Kiihtyvyysantureiden ja kehitysalustojen käyttö.
- Bluetooth-tiedonsiirto ja väliasemien ohjelmointi.
- Palvelin- ja tietokantasovellusten kehittäminen Pythonilla ja MySQL:llä.
- Monivaiheisen järjestelmän testaus ja virheenkorjaus.
## Projektin tavoitteet ja toteutus
Projektin päätavoitteena oli rakentaa toimiva tiedonsiirtojärjestelmä, joka:
1. Lukee kiihtyvyysanturin reaaliaikaisia arvoja (x-, y-, ja z-akselit).
2. Lähettää nämä arvot Bluetooth-yhteydellä Raspberry Pi:lle.
3. Tallentaa arvot MySQL-tietokantaan Linux-palvelimelle analysointia varten.
## Projektin toteutus eteni vaiheittain:
- Vaihe 1: Kiihtyvyysanturin integrointi ja ohjelmointi nRF5340 Development Kitillä.
- Vaihe 2: Bluetooth-yhteyden konfigurointi Raspberry Pi:n kanssa.
- Vaihe 3: Tietokannan suunnittelu ja yhteyden toteutus palvelimella.
- Vaihe 4: Testaus, virheenkorjaus ja tekstitiedostojen viimeistely.
## Käytetyt Laitteet ja Teknologiat
![image](https://github.com/user-attachments/assets/1154c2b3-b45e-4d4b-a344-be6c4a75de87)
- nRF5340 Development Kit (Kuva 1)
- 
![image](https://github.com/user-attachments/assets/8a1605dc-d331-468e-a641-49ff65765393)
- Raspberry Pi 3 (Kuva 2)
![image](https://github.com/user-attachments/assets/eac1498c-35f9-4b53-ad6c-eb86f3152ad3)
- GY-61 ADXL335 Kolmiakselinen kiihtyvyysanturi (Kuva 3)
- Python: Käytettiin ohjelmointikielenä sekä nRF5340:ssä että Raspberry Pi:ssä.
- MySQL: Palvelimella käytetty tietokanta kiihtyvyysarvojen tallentamiseen.
- Linux-palvelin: Toimi keskeisenä tietokantapalvelimena
 
1.	(nRF5340 Development Kit)
 
2.	(Raspberry Pi 3)
 
3.	(GY-61 ADXL335 3 akselinen kiihtyvyysanturi)

## Oppimiskokemukset ja haasteet
Projektin aikana opimme laajasti sekä ohjelmoinnin että järjestelmäintegraation käytännön soveltamista. Erityisesti Bluetooth-yhteyden vakauden varmistaminen sekä reaaliaikaisen tiedonkeruun ja tallennuksen yhteensovittaminen toivat arvokasta kokemusta.

Haasteina olivat:
- Bluetooth-yhteyden konfigurointi eri laitteiden välillä.
- Anturien kalibrointi tarkkojen arvojen saamiseksi.
- Tietokantayhteyksien optimointi suurille datamäärille.
## Laitteiston linkit
GY-61 Kiihtyvyysanturi
nRF5340 Developement Kit
Raspberry Pi 3
## Yhteenveto
