import sqlite3
from random import randint

global db
global sql



db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute(
   """    
   CREATE TABLE IF NOT EXISTS users( 
   login TEXT,
   password TEXT,
   cash INT
)
  """
)
def reg():
    db.commit()
    user_login = input('Login:')
    user_password = input('Password:')
    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?,?,?)",(user_login, user_password, 0))
        db.commit()
        print('Зарегистрировано')
    else:
        print("Такая запись имеется")

    for value in sql.execute("SELECT * FROM users"):
        print(value)

def delete_db():
    sql.execute(f"DELETE FROM users WHERE login = '{user_login}' ")
    db.commit()

    print('Запись удалена!')

def casino():
    global user_login
    user_login = input('Login in: ')
    number = randint(1, 2)
    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Такого логина не существует, Зарегистрируйтесь')
        reg()
    else:
        if number == 1:
            sql.execute(f"UPDATE users SET cash = '{1000 }' WHERE login = '{user_login}'")
            db.commit()
        else:
            print('ВЫ проиграли!')
            delete_db()
        
def enter():

    sql.execute('SELECT login, cash FROM users')
    row = sql.fetchall()[0][0]
    print(row)

def main():
    casino()
    enter()


main()
