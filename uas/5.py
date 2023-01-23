import MySQLdb as db

connection = db.connect('127.0.0.1', 'root', '', 'pos')

cursor = connection.cursor()

query = "SELECT * from product"

cursor.execute(query)
result = cursor.fetchall()
for items in result:
    print(items)