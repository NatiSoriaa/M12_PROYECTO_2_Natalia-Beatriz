#LLAMADAS BASE DE DATOS

import mysql.connector as mysql
from cryptography import encriptar_datos, desencriptar_datos, generar_clave

def conectarDB():
    try:
        db = mysql.connect(
            host = 'localhost',
            database = 'centros',
            user = 'root',
            passwd = ''
        )
        return db
    
    except mysql.Error as error:
        print(f"Error al intentar conectarse a la base de datos: {error}")
        return None

def llamadaCentroEducacion(codigo_postal_educacion, nombre_educacion, fecha_inicio):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        consulta = 'SELECT codigo_postal_educacion, nombre_educacion, fecha_inicio FROM centro_educacion'
        cursor.execute(consulta, (codigo_postal_educacion, nombre_educacion, fecha_inicio))
        resultado_educacion = cursor.fetchone()

        #desencriptar datos que se necesiten
        for row in resultado_educacion:
            row['nombre_educacion'] = desencriptar_datos(row['nombre_educacion'])
            row['fecha_inicio'] = desencriptar_datos(row['fecha_inicio'])
            row['codigo_postal_educacion'] = desencriptar_datos(row['codigo_postal_educacion'])

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "error en consulta"}
    
    finally: 
        cursor.close()
        db.close()
    
    return resultado_educacion


def insertarCentroEducacion(nombre_educacion, nombre_barrio):
    db = conectarDB()
    cursor=db.cursor(dictionary=True)

    #encriptar datos antes de insertar
    nombre_educacion_encriptado=encriptar_datos(nombre_educacion)
    nombre_barrio_encriptado=encriptar_datos(nombre_barrio)
    
    consulta = "INSERT INTO centro_educacion (nombre_educacion, nombre_barrio) VALUES (%s, %s)"
    cursor.execute(consulta, (nombre_educacion_encriptado,nombre_barrio_encriptado))
    db.commit()

    cursor.close()
    db.close()


def actualizarCentroEducacion(id_educacion, fecha_inicio):
    db = conectarDB()
    cursor=db.cursor(dictionary=True)
    
    consulta = "UPDATE centro_educacion SET fecha_inicio = %s WHERE id_educacion = %s"
    cursor.execute(consulta,(id_educacion, fecha_inicio))
    db.commit()

    cursor.close()
    db.close()


def borrarCentroEducacion(id_educacion=None, nombre_educacion=None):
    db = conectarDB()
    cursor=db.cursor(dictionary=True)
    
    consulta = "DELETE FROM centro_educacion WHERE 1=1"
    valores = []

    if id_educacion:
        consulta+= "AND id_educacion = %s"
        valores.append(encriptar_datos(id_educacion))
    
    if nombre_educacion:
        consulta+= "AND nombre_educacion=%s"
        valores.append(encriptar_datos(nombre_educacion))
    
    if not valores:
        return{"error": "se necesita al menos un parámetro para poder eliminar el centro"}
    
    cursor.execute(consulta,(valores))
    db.commit()

    cursor.close()
    db.close()


def llamadaCentroSanidad(codigo_postal_sanidad, nombre_sanidad, nombre_barrio):
    db = conectarDB()

    if not db:
        return {"error": "error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        consulta = 'SELECT codigo_postal_sanidad, nombre_sanidad, nombre_barrio FROM centro_sanidad'
        cursor.execute(consulta, (codigo_postal_sanidad, nombre_sanidad, nombre_barrio))
        resultado_sanidad = cursor.fetchall()

        for row in resultado_sanidad:
            row['nombre_sanidad']=desencriptar_datos(row['nombre_sanidad'])
            row['codigo_postal_sanidad']=desencriptar_datos(row[codigo_postal_sanidad])
            row['nombre_barrio']=desencriptar_datos(row[nombre_barrio])

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "error en consulta"}
    
    finally:
        cursor.close()
        db.close()
    
    return resultado_sanidad

def insertarCentroSanidad(nombre_sanidad, nombre_barrio):
    db = conectarDB()
    cursor=db.cursor(dictionary=True)
    
    #encriptar antes de insertar
    nombre_sanidad_encriptado = encriptar_datos(nombre_sanidad)
    nombre_barrio_encriptado = encriptar_datos(nombre_barrio)

    consulta = "INSERT INTO centro_sanidad (nombre_sanidad, nombre_barrio) VALUES (%s, %s)"
    cursor.execute(consulta, (nombre_sanidad_encriptado, nombre_barrio_encriptado))
    db.commit()

    cursor.close()
    db.close()

def actualizarCentroSanidad(nombre_sanidad, nombre_barrio, codigo_postal_sanidad):
    db = conectarDB()
    cursor=db.cursor(dictionary=True)
    
    consulta = "UPDATE centro_sanidad SET nombre_barrio = %s WHERE codigo_postal_sanidad = %s"
    cursor.execute(consulta,(nombre_sanidad, nombre_barrio, codigo_postal_sanidad))
    db.commit()

    cursor.close()
    db.close()

def borrarCentroSanidad(codigo_postal_sanidad):
    db = conectarDB()
    cursor=db.cursor(dictionary=True)

    consulta="DELETE FROM centro_sanidad WHERE codigo_postal_sanidad = %s"
    cursor.execute(consulta, (codigo_postal_sanidad))
    db.commit()

    cursor.close()
    db.close()
    
generar_clave()