from flask import Flask, render_template
from Conexion import GetPeliculas, GetSeries
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')
    
@app.route('/peliculas')
def peliculas():
    return render_template('peliculas.html', pelis=GetPeliculas())

@app.route('/series')
def series():
    return render_template('series.html', series=GetSeries())

if __name__ == '__main__':
    app.run(debug=True)