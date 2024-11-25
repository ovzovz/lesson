import sqlite3

connection=sqlite3.connect('db14_4.db')
def initiate_db():
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Products("
               "id INTEGER PRIMARY KEY,"
               "title TEXT NOT NULL,"
               "description TEXT,"
               "price INTEGER NOT NULL)")
    connection.commit()

def fill_table():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Products ( title, description, price)"
                   " VALUES (?,?,?)", ('Яблоко','вкусно',100))
    cursor.execute("INSERT INTO Products ( title, description, price)"
                   " VALUES (?,?,?)", ('Груша', 'вкусноооо', 200))
    cursor.execute("INSERT INTO Products ( title, description, price)"
                   " VALUES (?,?,?)", ('Вишня', 'вкуууусно', 300))
    cursor.execute("INSERT INTO Products ( title, description, price)"
                   " VALUES (?,?,?)", ('Абрикос', 'вкусно', 400))
    connection.commit()

def get_all_products():
    cursor = connection.cursor()
    products=cursor.execute("SELECT * FROM Products")
    return products.fetchall()

#initiate_db()
#fill_table()
#pr=get_all_products()
