import mysql.connector
import csv

db = mysql.connector.connect(host='localhost',database='mydb',user='root',password='root')

cur = db.cursor()

print('Saving...')

with open('Final_Normalized_name_basic.csv', encoding="utf8") as tsvfile:
  reader = csv.reader(tsvfile, delimiter=',')
  for row in reader:

    cur.execute("INSERT INTO people2 VALUES (%s,%s,%s,%s,%s,%s)",(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    db.commit(

    )

db.close()

print('Done!')


