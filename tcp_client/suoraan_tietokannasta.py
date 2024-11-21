import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="172.20.241.42",
  user="dbaccess_ro",
  password="1111",
  database="measurements"
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