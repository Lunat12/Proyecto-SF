import sqlite3 as sql
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def sql_connection():
    try:
        con = sql.connect('mydatabase.db')#creates BBDD
        #:memory: #this saves the BBDD on ram
        print('conection stablished')

        return con

    except Error:
        print(Error)
    
    #finally:
        #con.close() #buenas practicas cerrarlo al final para guardasr memoria

def sql_table(conn):
    CursorObj = conn.cursor()#creates cursor to execute comands

    CursorObj.execute('CREATE TABLE users(id integer PRIMARY KEY, name text, password text)')#creamos tabla con CREATE TABLE

    conn.commit()#subimos los cambios a la BBDD
    #necesitaremos un lector de .db para abrir el archivo y verlo (me siento pro ayuda)



def addInfo(IDs, currentName, currentPasword):
    global currentID
    currentID = 1
    currentID += len(IDs)
 

    entities = (currentID, currentName, currentPasword)
    return(entities)

def sql_insert(conn, entities):
    
    CursorObj = conn.cursor()
    print(entities)

    CursorObj.execute('INSERT INTO users(id, name, password) VALUES(?, ?, ?)', entities)
    conn.commit()
    print('Information saved')

def sql_fetchID(conn):
    CursorObj = conn.cursor()
    
    CursorObj.execute('SELECT id FROM users')
    IDs = CursorObj.fetchall()
    return IDs


def sql_fetchUsername(conn):
    CursorObj = conn.cursor()

    #CursorObj.execute('SELECT * FROM users') #select everything in a table
    #CursorObj.execute('SELECT id, name FROM users') #select colums in this case two
    
    CursorObj.execute('SELECT name FROM users')
    usernames = CursorObj.fetchall()
    return usernames

def sql_fetchPassword(conn):
    CursorObj = conn.cursor()
    
    CursorObj.execute('SELECT password FROM users')
    passwords = CursorObj.fetchall()
    return passwords

def logIn(usernames, passwords,currentName,currentPasword):

    
    users = []
    passw = []
    for u in usernames:
        users.append(u[0])
    for p in passwords:
        passw.append(p[0])

    if currentName in users:
        counter = 0
        for n in users:
            if currentName == n:
                break
            counter +=1
        if currentPasword == passw[counter]:
            print('loggedIn')
            return True
            
        else:
            print('Incorrect password')
            return False
    else:
        print('User not found')
        return False


#sql_table(sql_connection())
#sql_insert(sql_connection(), addInfo(sql_fetchID(sql_connection())))
#logIn(sql_fetchUsername(sql_connection()),sql_fetchPassword(sql_connection()),'Ermys','12345')