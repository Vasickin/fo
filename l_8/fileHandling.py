import sqlite3 as sl

# Сщздание подключения к БД

conn = sl.connect("FH.db")

# Создание курсора - основного объекта подключения SQL кода

cur = conn.cursor()

# Сосдадим таблицг Users, если она не создана

cur.execute()


