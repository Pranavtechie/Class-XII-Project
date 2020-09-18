from prettytable import PrettyTable
import mysql.connector as m

pt = PrettyTable()
conn = m.connect(host = 'localhost', user = 'root', password = 'student', database = 'medic')
cursor = conn.cursor()

pt.field_names = ['Medicine Name','Usage / Indications','Quantity']

cursor.execute("SELECT * FROM medicine")
data = cursor.fetchall()

for med,ind,qty in data:
    pt.add_row([med,ind, qty])
