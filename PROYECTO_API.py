from flask import Flask,render_template,request,redirect,url_for, session, flash, request, jsonify
import mysql.connector as mysql

db= {
    'host':'localhost', 
    'user':'root', 
    'password':'', 
    'db':'centros'
}

app = Flask(__name__)

@app.route('/')
def inicio():
    conexion = mysql.connect(
        host=db['host'],
        user=db['user'],
        password=db['password'],
        database=db['db']
    )

    cursor = conexion.cursor()

    cursor.execute("SHOW TABLES")

    tablas = cursor.fetchall()

    datos_tablas = {}
    for tabla in tablas:
            nombre_tabla = tabla[0]
            cursor.execute(f"SELECT * FROM {nombre_tabla}")  
            filas = cursor.fetchall()

            
            cursor.execute(f"SHOW COLUMNS FROM {nombre_tabla}")
            columnas = cursor.fetchall()
            nombres_columnas = [columna[0] for columna in columnas]
            
            datos_tablas[nombre_tabla] = {
                'columnas': nombres_columnas,
                'filas': filas
            }

    cursor.close()
    conexion.close()

    return render_template('index.html', datos_tablas=datos_tablas)

if __name__ == '__main__':
    app.run(debug=True)
    
    
#Mostrar centro sanitario
#@app.route('/sanitario', methods=['GET','POST','PUT','DELETE'])
    #def sanitario():
    #connection = get_db_connection()
    #cursor=conexion.cursor()

    #if request.method == 'GET':
    #cursor.execute("SELECT * FROM centro_sanidad")
    #result = cursor.fetchall()
    #return jsonify(result)

    #if request.method == 'GET':
    #cursor.execute("SELECT nombre_sanidad FROM centro_sanidad")
    #nombres_sanidad ) cursor.fetchall()

    #if request.method == 'GET':
        #cursor.execute("SELECT codigo_postal_sanidad FROM centro_sanidad")
        #codigos_postales = cursor.fetchall()

    #elif request.method == 'POST':
    
