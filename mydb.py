import mysql.connector
cnx = mysql.connector.connect(user='root', password='2001', database='sakila')
cursor = cnx.cursor()
#Insertar
sql = ("INSERT INTO actor (first_name,last_name) VALUES(%s,%s)")
data = ("CLAUDIA", "SAAVEDRA")
cursor.execute(sql,data)
cnx.commit()
#Mostrar
cursor.execute("SELECT * FROM actor")
for row in cursor.fetchall():
    print(row[0],'-', row[1],'-', row[2],'-' ,row[3].strftime('%d/%m/%Y'))