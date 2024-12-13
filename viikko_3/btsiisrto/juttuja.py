
import asyncio
import struct
from bleak import BleakClient
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

DEVICE_ADDRESS = "CF:42:16:CF:E2:5F"  # Korvaa BLE-osoitteella
CHARACTERISTIC_UUID = "00001526-1212-efde-1523-785feabcd123"  # Korvaa UUID:llä

buffer = []  # Puskurimuuttuja arvoparien keräämiseksi

# Tietokantayhteys
conn = None

load_dotenv()

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_name = os.getenv("NAME")

async def connect_to_db():
    """Yhdistä tietokantaan ja palauta yhteysobjekti."""
    try:
        global conn
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
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
            value = struct.unpack('<h', data[i:i+2])[0] / 1  # Skaalaus
            buffer.append(value)

        while len(buffer) >= 3:  # Kolme arvoa kerrallaan
            x, y, z = buffer[:3]
            buffer = buffer[3:]
            print(f"X: {x:.2f} - Y: {y:.2f} - Z: {z:.2f}")

            '''if(x > y and x>z):
                {
                    #suunta demo
                }'''
            # Tallenna tietokantaan
            insert_data_to_db(x, y, z)
    else:
        print("Virhe: Data ei ole odotetun pituinen")

async def main():
    """BLE-yhteyden päälogiikka."""
    ##await connect_to_db()  # Yhdistä tietokantaan

    async with BleakClient(DEVICE_ADDRESS) as client:
        if client.is_connected:
            print("Yhdistetty laitteeseen!")
            await client.start_notify(CHARACTERISTIC_UUID, data_handler)
            print("Odotetaan dataa...")
            await asyncio.sleep(30)
            await client.stop_notify(CHARACTERISTIC_UUID)
            print("Yhteys lopetettu")
    
    if conn and conn.is_connected():
        conn.close()
        print("Tietokantayhteys suljettu.")

asyncio.run(main())


