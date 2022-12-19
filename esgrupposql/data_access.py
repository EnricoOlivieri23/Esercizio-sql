import mysql.connector
from DB import Connessione  

def film(lista):
    mycursor= lista.cursor()
    mycursor.execute("select title from film")
    result= mycursor.fetchall()
    for i in result:
        print(i)

def actor(lista):
    mycursor= lista.cursor()
    mycursor.execute("select first_name, last_name from actor")
    result= mycursor.fetchall()
    for i in result:
        print(i)
