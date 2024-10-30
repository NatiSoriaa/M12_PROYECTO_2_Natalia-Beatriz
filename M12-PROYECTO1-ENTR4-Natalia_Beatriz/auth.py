import bcrypt
import mysql.connector as mysql
from flask import Flask, request, jsonify

app = Flask(__name__)

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

def validarApiKey(request):
    api_key = request.headers.get('x-api-key') or request.args.get('api_key')

    if not api_key:
        return False
    
    api_key_bytes = api_key.encode('utf-8')

    # Consultar la base de datos para verificar la API key
    db = conectarDB()
    if not db:
        return False

    cursor = db.cursor()
    try:
        consulta = "SELECT password_hash FROM users_key"
        cursor.execute(consulta)
        hashed_keys = cursor.fetchall()
        
        # Comprobar si la API key es válida
        return any(bcrypt.checkpw(api_key_bytes, hashed_key[0].encode('utf-8')) for hashed_key in hashed_keys)
    except mysql.Error as error:
        print(f"Error en validación de API key: {error}")
        return False
    finally:
        cursor.close()
        db.close()

@app.route('/usuarios', methods=['GET'])
def mostrarUsuarios():
    db = conectarDB()
    
    if not db:
        return jsonify({"error": "Error de conexión a la base de datos"})

    cursor = db.cursor(dictionary=True)
    
    try:
        consulta = "SELECT * FROM users_key"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        
        if resultado:
            return jsonify(resultado)  # Convertir resultado a JSON
        else:
            return jsonify({"mensaje": "No hay usuarios en la tabla."})
    
    except mysql.Error as error:
        return jsonify({"error": f"Error en consulta: {error}"})
    
    finally:
        cursor.close()
        db.close()

# Rutas de ejemplo (reemplaza estas con la implementación adecuada)
url_educacion = 'http://localhost:5000/centro_educacion'
url_sanidad = 'http://localhost:5000/centro_sanidad'

# Ejemplo de verificación de API key en una ruta
@app.route('/verificar', methods=['GET'])
def verificar_ruta():
    if validarApiKey(request):
        return jsonify({"mensaje": "API key válida"}), 200
    else:
        return jsonify({"error": "API key no válida"}), 403

if __name__ == '__main__':
    app.run(port=5001, debug=True)
