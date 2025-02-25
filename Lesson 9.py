import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# ======= CREATE TABLE =========
# cur.execute("CREATE TABLE Users (login TEXT);")
# connection.commit()

# ======= INSERT =========
login = input("login: ")
cur.execute(f"INSERT INTO Users (login) VALUES ('{login}');")
connection.commit()


connection.close()