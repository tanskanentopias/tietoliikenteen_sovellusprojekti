



# Tietoliikenteen sovellusprojekti
Tietoliikenteen sovellusprojekti on osa tieto- ja viestintätekniikan insinööriopintojen 2. vuoden kurssia. Tämä projekti yhdistää laitteisto-ohjelmoinnin, tietoliikenteen ja palvelinsovellukset. Projektin tavoitteena oli kehittää järjestelmä, joka pystyy tunnistamaan kiihtyvyysanturin asennon (ylös, alas, vasen, oikea, eteen ja taakse) sen antamista arvoista ja lähettää arvot Bluetoothin yli tietokantaan.
## Projektin arkkitehtuuri
![Blank document (1)](https://github.com/user-attachments/assets/f0e6158f-fa61-4aba-8872-5d509d09ca10)
## Saimme käytännön kokemusta seuraavista aihealueista:
•	kiihtyvyysantureiden ja kehitysalustojen käyttö

•	Bluetooth-tiedonsiirto ja väliasemien ohjelmointi
•	palvelin- ja tietokantasovellusten kehittäminen Pythonilla ja MySQL:llä
•	koodin kirjoitusta koneoppimistarkoitukseen
•	monivaiheisen järjestelmän testaus ja virheenkorjaus.

## Projektin tavoitteet
Projektin päätavoitteena oli rakentaa toimiva tiedonsiirtojärjestelmä, joka
1.	lukee kiihtyvyysanturin reaaliaikaisia arvoja (x-, y-, ja z-akselit)
2.	lähettää nämä arvot Bluetooth-yhteydellä Raspberry Pille
3.	tallentaa arvot MySQL-tietokantaan Linux-palvelimelle analysointia ja koneoppimista varten.

## Projektin toteutus vaiheittain
•	Vaihe 1: Kiihtyvyysanturin integrointi ja ohjelmointi nRF5340 Development Kitillä.
•	Vaihe 2: Bluetooth-yhteyden konfigurointi Raspberry Pin kanssa.
•	Vaihe 3: Tietokannan suunnittelu ja yhteyden toteutus palvelimella.
•	Vaihe 4: Kiihtyvyysanturin arvojen tallennus tietokantaan.
•	Vaihe 5: arvojen käyttäminen koneoppimistarkoituksiin
•	Vaihe 6: testaus, virheenkorjaus ja tekstitiedostojen viimeistely.

## Käytetyt Laitteet ja Teknologiat
•	nRF5340 Development Kit (kuva 1).
•	Raspberry Pi 3 (kuva 2).
•	GY-61 ADXL335 Kolmiakselinen kiihtyvyysanturi (kuva 3).
•	Python: Käytettiin ohjelmointikielenä sekä nRF5340:ssä että Raspberry Pi:ssä.
•	MySQL: Palvelimella käytetty tietokanta kiihtyvyysarvojen tallentamiseen.
•	Linux-palvelin: Toimi keskeisenä tietokantapalvelimena.


 ![image](https://github.com/user-attachments/assets/1154c2b3-b45e-4d4b-a344-be6c4a75de87)
 
KUVA 1. nRF5340 Development Kit

 ![image](https://github.com/user-attachments/assets/8a1605dc-d331-468e-a641-49ff65765393)
 
KUVA 2. Raspberry Pi 3

![image](https://github.com/user-attachments/assets/eac1498c-35f9-4b53-ad6c-eb86f3152ad3)
 
KUVA 3. GY-61 ADXL335 3-akselinen kiihtyvyysanturi

## Oppimiskokemukset ja haasteet
Projektin aikana opimme laajasti sekä ohjelmoinnin että järjestelmäintegraation käytännön soveltamista. Erityisesti Bluetooth-yhteyden vakauden varmistaminen sekä reaaliaikaisen tiedonkeruun ja tallennuksen yhteensovittaminen toivat arvokasta kokemusta. Haastavimmaksi osaksi paljastui koneoppimisen ymmärtäminen ja käyttäminen.

Haasteina olivat
•	Bluetooth-yhteyden konfigurointi eri laitteiden välillä
•	anturien kalibrointi tarkkojen arvojen saamiseksi
•	tietokantayhteyksien optimointi suurille datamäärille.
•	koneoppimisen KMeans-algoritmin ymmärtäminen ja soveltaminen.
•	tietotekniset ongelmat ja niiden ratkaisut.

## Laitteiston linkit
[GY-61 Kiihtyvyysanturi](https://www.spelektroniikka.fi/p23824-gy-61-adxl335-3-akselinen-kiihtyvyysanturi-fi.html)

[nRF5340 Developement Kit](https://www.nordicsemi.com/Products/Development-hardware/nRF5340-DK)

[Raspberry Pi 3](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/)

## Yhteenveto
Tietoliikenteen sovellusprojekti oli haastava ja hyvin taitoja testaava osa lukuvuotta, mutta todella opettavainen monesta eri alueesta alallamme. Projektin tavoitteena oli saada koodaamamme ohjelma tunnistamaan kiihtyvyysanturin asento sen antamista arvoista ja lähettämään nämä arvot Bluetoothin yli ensin Raspberry Pille, josta ne lähetettiin eteenpäin Linux serverille, missä MySQL-tietokanta sijaitsee. Myöhemmin arvot otettiin käyttöön koneoppimistehtävässä. Saimme viettää monia tunteja ratkaisujen pohtimisessa sekä eri toteutustapojen ideoimisessa projektin aikana.  Pääsimme asetettuihin tavoitteisiin haasteista ja ongelmista huolimatta, ja olimme tyytyväisiä tulokseen.
