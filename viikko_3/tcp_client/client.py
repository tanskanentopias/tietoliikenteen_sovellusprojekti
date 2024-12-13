import requests
import csv

# Fetch the data from the server
response = requests.get("http://172.20.241.42/read_database.php", verify=True)

# Split data into entries based on the <br> tag
entries = response.text.split('<br>')

# Open the CSV file to write
with open('hae_tiedot.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Iterate through each entry
    for entry in entries:
        # Skip empty lines
        if not entry.strip():
            continue

        # Split fields by '-'
        fields = [field.strip() for field in entry.split(' , ')]

        # Write the fields as a new row
        writer.writerow(fields)
