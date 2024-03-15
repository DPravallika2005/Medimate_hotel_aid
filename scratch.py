from mysql.connector import connect

conn = connect(
    host = 'localhost',
    user = 'root',
    Count = '0',
    database  = 'Tablets'
)

cur = conn.cursor()
cur.execute('select * from Tablet_details')
data = cur.fetchall()

print(data)