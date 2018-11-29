# import sqlite3

# connection = sqlite3.connect("kangethe.db")

# cursor = connection.cursor()

# try:
# 	create_table = "CREATE TABLE users (id int, username text, password text)"
# 	cursor.execute(create_table)
# except:
# 	print("Fail")

# user = (1, "Annita", "WatiriANNita")
# insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# cursor.execute(insert_query, user)

# users = [
# 	(2, "Lucy", "MuguLucyre"),
# 	(3, "Trizah", "WnjTrizAHbaBY")
# ]
# cursor.executemany(insert_query, users)

# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
# 	print(row)

# connection.commit()
# connection.close()