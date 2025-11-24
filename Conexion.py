from mysql.connector import connect 
import os
from dotenv import load_dotenv
from modelos import Serie,Pelicula




load_dotenv()
print(os.getenv("host"),os.getenv("port"),os.getenv("user"),os.getenv("password"),os.getenv("database"))
def GetPeliculas():
    peliculasinstanciadas = []
    conn = connect(
            host=os.getenv("host"),
            port=os.getenv("port"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            database=os.getenv("database")
        )
    print("Conectado a la base de datos")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contenidos WHERE tipo = 'pelicula'")
    peliculas = cursor.fetchall()
    cursor.close()
    conn.close()
    for peli in peliculas:
        peliculasinstanciadas.append(Pelicula(peli[0],peli[1],peli[2],peli[3],peli[4],peli[5],peli[6]))
    return peliculasinstanciadas

def GetSeries():
    seriesinstanciadas = []
    conn = connect(
            host=os.getenv("host"),
            port=os.getenv("port"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            database=os.getenv("database")
        )
    print("Conectado a la base de datos")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contenidos WHERE tipo = 'serie'")
    series = cursor.fetchall()
    cursor.close()
    conn.close()
    for serie in series:
        seriesinstanciadas.append(Serie(serie[0],serie[1],serie[2],serie[3],serie[4],serie[5],serie[6]))
    return seriesinstanciadas
