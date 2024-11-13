import asyncio
from bleak import BleakClient


DEVICE_ADDRESS = "CF:42:16:CF:E2:5F"  # Korvaa Nordic-laitteen BLE-osoitteella
CHARACTERISTIC_UUID = "00001526-1212-efde-1523-785feabcd123"  # Korvaa ominaisuuden UUID:llä


def data_handler(sender, data):
    # Tulosta vastaanotettu data (data on bytes-tyyppinen)
    print(f"Vastaanotettu data: {data.hex()}")

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


asyncio.run(main())