import sqlite3

## Crea la conexion y la tabla
def crear_conexion():
    conexion = sqlite3.connect('games.db')
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Games("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, "+
                    "Nombre TEXT NOT NULL, "+
                    "Genero TEXT NOT NULL, "+
                    "Fecha INTEGER NOT NULL, "+
                    "Empresa TEXT NOT NULL, "+
                    "Plataforma TEXT NOT NULL"+
                    ")")
    conexion.commit()
    return conexion

## Busca todas las entradas de la tabla ordenandolas de forma ascendente
def get_juegos(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM games ORDER BY nombre ASC")
    juegos = cursor.fetchall()    
    return juegos

## Guarda un registro en la base de datos
def save_game(conexion, nombre, genero, fecha, empresa, plataforma):
    conexion.execute("INSERT INTO games (Nombre, Genero, Fecha, Empresa, Plataforma) VALUES (?, ?, ?, ?, ?)", (nombre, genero, fecha, empresa, plataforma))
    conexion.commit()
    conexion.close()

## Borra un registro en la base de datos
def delete_game(conexion, nombre):    
    cursor = conexion.cursor()
    consulta = "DELETE FROM Games WHERE nombre = ?"
    cursor.execute(consulta, (nombre,))
    conexion.commit()    

## Ordena por fecha
def order_by_date(conexion):      
    cursor = conexion.cursor()    
    cursor.execute("SELECT * FROM games ORDER BY fecha ASC")
    order = cursor.fetchall()
    return order

## Busca un registro por "Nombre" en la base de datos
def search_game(conexion, nombre_juego):    
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM games WHERE LOWER(nombre) LIKE '%' || ? || '%'", (nombre_juego.lower(),))
    resultados = cursor.fetchall()
    return resultados

## Valida que una entrada este repetida
def validation(conexion, nombre):    
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM Games WHERE LOWER(nombre)=LOWER(?)", (nombre,))
    existe_juego = cursor.fetchone()[0]
    return existe_juego

## Cuenta el total de registros en la base de datos
def totales():
    conexion = sqlite3.connect('games.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT (*) FROM games")
    resultado = cursor.fetchone()
    total = resultado[0]
    return total