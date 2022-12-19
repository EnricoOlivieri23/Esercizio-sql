import mysql.connector
from DB import Connessione

try:
    film= ("select title from film")
    attore= ("select first_name, last_name from actor")
    
    miaconnession= Connessione(host = "localhost" , user = "root" , passwd = "Chiellini3@",port="3306",database="sakila" )

    result= miaconnession.richiesta_connessione(film)
    for i in result:
        print(i)

    result= miaconnession.richiesta_connessione(attore)
    for i in result:
        print(i)

except mysql.connector.Error as errore:
    print("Si è verificato un errore") 
    print(errore)
finally:
    miaconnession.close()
    print("Connessione chiusa")