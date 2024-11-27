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
    cursor.execute("CREATE TABLE IF NOT EXISTS Users("
               "id INTEGER PRIMARY KEY,"
               "username TEXT NOT NULL,"
               "email TEXT NOT NULL,"
               "age INTEGER NOT NULL,"
               "balance INTEGER NOT NULL)")
    connection.commit()

def add_user(username, email, age):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance)  VALUES (?,?,?,1000)",(username,email,age))
    connection.commit()

def is_included(username):
    cursor = connection.cursor()
    check_user = cursor.execute(f'SELECT * FROM Users WHERE username="{username}"')
    if check_user.fetchone() is None:
        return False
    else:
        return True

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


initiate_db()
#if not is_included('An'):
 #  add_user('An', 'ann@mail.ru', 25)


