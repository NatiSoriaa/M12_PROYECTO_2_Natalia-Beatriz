#API KEY
import bcrypt
import mysql.connector as mysql
from flask import Flask, json

app= Flask(__name__)

def conectarDB():
    try:
        db = mysql.connect(
            host='localhost',
            database='apikey_user',
            user='root',
            passwd=''
        )
        return db
    except mysql.Error as error:
        print(f"Error al intentar conectarse a la base de datos: {error}")
        return None
    
#api key hashteada una vez y almacenada 
hashed_api_key = bcrypt.hashpw(b'123', bcrypt.gensalt())

api_keys = {
    "usuario1": hashed_api_key
}

def insertarUsuario(nombre_user, password):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexión a la base de datos"}

    cursor = db.cursor()
    
    # Hashear la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        consulta = "INSERT INTO users_key (nombre_user, password_hash) VALUES (%s, %s)"
        cursor.execute(consulta, (nombre_user, hashed_password))
        db.commit()

        if cursor.rowcount > 0:
            return {"mensaje": "Usuario insertado correctamente"}, 201
        else:
            return {"error": "No se pudo insertar el usuario"}, 500
    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "Error en consulta"}
    finally:
        cursor.close()
        db.close()

#insertar user si no existe
resultado = insertarUsuario("usuario1", "123")
print(resultado)

def validarApiKey(request):
    api_key = request.headers.get('x-api-key') or request.args.get('api_key')

    if not api_key:
        return False
    
    api_key_bytes = api_key.encode('utf-8')

    #comprobar que la api key coincide y es válida
    return any(bcrypt.checkpw(api_key_bytes, hashed_key) for hashed_key in api_keys.values())

def mostrarUsuarios():
    db = conectarDB()
    
    if not db:
        return json.dumps({"error": "Error de conexión a la base de datos"})

    cursor = db.cursor(dictionary=True)
    
    try:
        consulta = "SELECT * FROM users_key"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        
        if resultado:
            return json.dumps(resultado)  # Convertir resultado a JSON
        else:
            return json.dumps({"mensaje": "No hay usuarios en la tabla."})
    
    except mysql.Error as error:
        return json.dumps({"error": f"Error en consulta: {error}"})
    
    finally:
        cursor.close()
        db.close()

resultado_json = mostrarUsuarios()
print(resultado_json)  # Imprimir el resultado en JSON

# @app.route('/api/users', methods=['GET'])
# def obtener_usuarios():
#     api_key = request.headers.get('x-api-key') or request.args.get('api_key')

#     if not validarApiKey(api_key):
#         return jsonify({"error": "API Key no válida"}), 403

#     db = conectarDB()
    
#     if not db:
#         return jsonify({"error": "Error de conexión a la base de datos"}), 500

#     cursor = db.cursor(dictionary=True)
    
#     try:
#         consulta = "SELECT * FROM users_key"
#         cursor.execute(consulta)
#         resultado = cursor.fetchall()
        
#         # Devolver los resultados en formato JSON
#         return jsonify(resultado), 200

#     except mysql.Error as error:
#         print(f"Error en consulta: {error}")
#         return jsonify({"error": "Error en consulta"}), 500
    
#     finally:
#         cursor.close()
#         db.close()

if __name__ == '__main__':
    app.run(port=5001, debug=True)

url_educacion = 'http://localhost:5000/centro_educacion'
url_sanidad = 'http://localhost:5000//centro_sanidad'

#http://localhost:5001/centro_educacion?api_key=123
#http://localhost:5001/centro_sanidad?api_key=123

headers={
    'x-api-key': '123' 
}
