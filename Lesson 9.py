import sqlite3

connection = sqlite3.connect("db.sl3", timeout=5)
cur = connection.cursor()

# ======= CREATE TABLE =========
# cur.execute("CREATE TABLE Users (login TEXT UNIQUE, phone TEXT);")
# connection.commit()

# ======= INSERT =========
login = input("login: ")
phone = input("phone: ")
cur.execute(f"INSERT INTO Users (login, phone) VALUES ('{login}', '{phone}');")
connection.commit()


# =======  SELECT ========
# login = input("login: ")
# cur.execute(f"SELECT * FROM Users ORDER BY login DESC;")  #WHERE login='anna'
# connection.commit()
# res = cur.fetchall()
# # print(res[1][1])
# #print(res)
# for el in res:
#     print(el[0], el[1])


# ======= UPDATE ========
# login = input("login: ")
# cur.execute(f"SELECT rowid FROM Users WHERE login='{login}';")
# connection.commit()
# res = cur.fetchall()
# if res != []:
#     phone = input("phone: ")
#     cur.execute(f"UPDATE Users SET phone='{phone}' WHERE login='{login}';")  #WHERE login='anna'
#     connection.commit()
#     print("Phone update")
# else:
#     print("Not login in DB")


# ======= DELETE =======
# login = input("login: ")
# cur.execute(f"DELETE FROM Users WHERE login='{login}';")
# connection.commit()


connection.close()