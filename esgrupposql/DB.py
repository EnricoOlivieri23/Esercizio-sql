import mysql.connector

class Connessione:
    def __init__(self, **config):
        self.miaconnession= None
        self.miaconnession = mysql.connector.connect(**config)

    def richiesta_connessione(self, query):
        mycursor= self.miaconnession.cursor()
        mycursor.execute(query)
        return mycursor.fetchall()

    def close(self):
        if self.miaconnession is not None:
            self.miaconnession.close()



