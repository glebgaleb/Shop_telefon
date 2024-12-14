import sqlite3

connection = sqlite3.connect('database.slite')
cursor = sqlite3.Cursor(connection)

cursor.execute("DROP TABLE IF EXISTS phones")

request = ("CREATE TABLE IF NOT EXISTS phones"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "description VARCHAR(255),"
           "price INTEGER,"
           "memory INTEGER,"
           "colors VARCHAR(255),"
           "photo VARCHAR(255))")

cursor.execute(request)

insert_request = ("INSERT INTO phones"
                  "(name, description, price, memory, colors, photo) VALUES (?, ?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("iphone 13", "описание", "400", "128", "синий,белый,красный,чёрный", "iphone.png"))
cursor.execute(insert_request, ("samsung s21", "описание", "200", "128", "чёрный,белый,синий,серый", "samsung.webp"))
cursor.execute(insert_request, ("google pixel 6", "описание", "155", "128", "синий,чёрный,белый,розовый", "google.webp"))
cursor.execute(insert_request, ("vivo x100 ultra", "описание", "880", "256", "серый,чёрный,белый,синий", "vivo.jpg"))
cursor.execute(insert_request, ("samsung s24", "описание", "860", "128", "серый,чёрный,золотой,синий", "samsungs24.jpg"))
cursor.execute(insert_request, ("Iphone 16", "описание", "1500", "1000", "розовый,чёрный,зелёный,белый", "iphone.webp"))

connection.commit()
connection.close()