import mysql.connector
import csv
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_name = os.getenv("NAME")

mydb = mysql.connector.connect(
  host=db_host,
  user=db_user,
  password=db_password,
  database=db_name
)

mycursor = mydb.cursor()

sql = "SELECT x,y,z FROM rawdata;"

# Execute the query
mycursor.execute(sql)

# Fetch all rows from the executed query
results = mycursor.fetchall()

with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y', 'z'])  # Write header
    writer.writerows(results)        # Write data rows

mycursor.close()
mydb.close()