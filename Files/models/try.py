import sqlite3

number = 9284893854
connect = sqlite3.connect("storage.db")
cursor = connect.cursor()
cursor.execute("SELECT Amount FROM rechargedata where MobNo=?",(number,))
user_info = cursor.fetchone()

connect.close()
print(user_info[0])
