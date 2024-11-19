'''import asyncio
import struct
from bleak import BleakClient


DEVICE_ADDRESS = "CF:42:16:CF:E2:5F"  # Korvaa Nordic-laitteen BLE-osoitteella
CHARACTERISTIC_UUID = "00001526-1212-efde-1523-785feabcd123"  # Korvaa ominaisuuden UUID:llä


def data_handler(sender, data):
    # Tulosta vastaanotettu data (data on bytes-tyyppinen)
    print(f"Vastaanotettu data: {data.hex()}")




buffer = []  # Puskurimuuttuja arvoparien keräämiseksi

def data_handler(sender, data):
    global buffer
    # Oletetaan, että jokainen lukuarvo tulee 2 tavun pätkissä
    if len(data) % 2 == 0:  # Varmistetaan, että pituus on parillinen
        for i in range(0, len(data), 2):
            # Puretaan yksi 16-bittinen luku (allekirjoitettu, little-endian)
            value = struct.unpack('<h', data[i:i+2])[0] / 100.0  # Skaalaus
            buffer.append(value)  # Lisätään puskuriin

        # Tarkistetaan, onko puskuriin kertynyt riittävästi dataa (X, Y, Z)
        while len(buffer) >= 3:  # Kolme lukuarvoa tarvitaan
            x, y, z = buffer[:3]  # Otetaan ensimmäiset kolme arvoa
            buffer = buffer[3:]  # Poistetaan käsitellyt arvot puskurista
            print(f"X: {x:.2f} - Y: {y:.2f} - Z: {z:.2f}")
    else:
        print("Virhe: Data ei ole odotetun pituinen")


import mysql.connector

# Yhdistä MySQL-tietokantaan
def connect_to_db():
    return mysql.connector.connect(
        host="172.20.241.42",  # Vaihda MySQL-isännän mukaan
        user="dbaccess_rw",
        password="0000",
        database="measurements"
    )

# Datan tallentaminen MySQL:ään
def insert_data_to_db(data):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Tallenna data tietokantaan
    sql = "INSERT INTO rawdata (x, y, z) VALUES (%s, %s, %s)"
    cursor.execute(sql, (data,))
    conn.commit()

    print("Data tallennettu tietokantaan.")
    cursor.close()
    conn.close()
    
    

async def main():
    # Luo asiakas Nordic-laitteelle
    async with BleakClient(DEVICE_ADDRESS) as client:
        # Tarkista onko laite yhteydessä
        if client.is_connected:
            print("Yhdistetty laitteeseen!")

            # Aloita ilmoitusten vastaanotto ominaisuudesta
            await client.start_notify(CHARACTERISTIC_UUID, data_handler)
            print("Odotetaan dataa...")

            # Odota dataa 30 sekuntia (voit muuttaa ajan tarpeen mukaan)
            await asyncio.sleep(30)

            # Lopeta ilmoitusten vastaanotto
            await client.stop_notify(CHARACTERISTIC_UUID)
            print("Yhteys lopetettu")


asyncio.run(main())'''

import asyncio
import struct
from bleak import BleakClient
import mysql.connector
from mysql.connector import Error

DEVICE_ADDRESS = "CF:42:16:CF:E2:5F"  # Korvaa BLE-osoitteella
CHARACTERISTIC_UUID = "00001526-1212-efde-1523-785feabcd123"  # Korvaa UUID:llä

buffer = []  # Puskurimuuttuja arvoparien keräämiseksi

# Tietokantayhteys
conn = None

async def connect_to_db():
    """Yhdistä tietokantaan ja palauta yhteysobjekti."""
    try:
        global conn
        conn = mysql.connector.connect(
            host="172.20.241.42",
            user="dbaccess_rw",
            password="0000",
            database="measurements"
        )
        if conn.is_connected():
            print("Tietokantayhteys muodostettu.")
    except Error as e:
        print(f"Virhe tietokantayhteydessä: {e}")

def insert_data_to_db(x, y, z):
    """Tallenna data tietokantaan."""
    try:
        if conn and conn.is_connected():
            cursor = conn.cursor()
            sql = "INSERT INTO rawdata (groupid, from_mac, to_mac ,x, y, z) VALUES ('17',%s,'b8:27:eb:af:7f:ae',%s, %s,%s)"
            cursor.execute(sql, (DEVICE_ADDRESS,x, y, z))
            conn.commit()
            print(f"Data tallennettu: X={x}, Y={y}, Z={z}")
            cursor.close()
    except Error as e:
        print(f"Virhe tallennuksessa: {e}")

def data_handler(sender, data):
    """Käsittele BLE-data ja tallenna puskuriin."""
    global buffer
    if len(data) % 2 == 0:  # Varmistetaan parillinen pituus
        for i in range(0, len(data), 2):
            value = struct.unpack('<h', data[i:i+2])[0] / 100.0  # Skaalaus
            buffer.append(value)

        while len(buffer) >= 3:  # Kolme arvoa kerrallaan
            x, y, z = buffer[:3]
            buffer = buffer[3:]
            print(f"X: {x:.2f} - Y: {y:.2f} - Z: {z:.2f}")
            # Tallenna tietokantaan
            insert_data_to_db(x, y, z)
    else:
        print("Virhe: Data ei ole odotetun pituinen")

async def main():
    """BLE-yhteyden päälogiikka."""
    await connect_to_db()  # Yhdistä tietokantaan

    async with BleakClient(DEVICE_ADDRESS) as client:
        if client.is_connected:
            print("Yhdistetty laitteeseen!")
            await client.start_notify(CHARACTERISTIC_UUID, data_handler)
            print("Odotetaan dataa...")
            await asyncio.sleep(10)
            await client.stop_notify(CHARACTERISTIC_UUID)
            print("Yhteys lopetettu")
    
    if conn and conn.is_connected():
        conn.close()
        print("Tietokantayhteys suljettu.")

asyncio.run(main())


