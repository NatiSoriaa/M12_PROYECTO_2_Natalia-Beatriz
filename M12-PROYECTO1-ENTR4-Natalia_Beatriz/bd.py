# BASE DE DATOS

import mysql.connector as mysql

def conectarDB():
    try:
        db = mysql.connect(
            host='localhost',
            database='centros',  
            user='root',
            passwd=''  
        )
        return db
    except mysql.Error as error:
        print(f"Error al intentar conectarse a la base de datos: {error}")
        return None



# CENTRO EDUCACION



# LLAMADA AL CENTRO EDUCATIVO

def llamadaCentroEducacion(id_educacion=None, codigo_postal_educacion=None, nombre_educacion=None, fecha_inicio=None):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)
    
    try:
        consulta = 'SELECT id_educacion, codigo_postal_educacion, nombre_educacion, fecha_inicio FROM centro_educacion'
        condiciones = []
        valores = []

        if id_educacion:
            condiciones.append("id_educacion = %s")
            valores.append(id_educacion)
        if codigo_postal_educacion:
            condiciones.append("codigo_postal_educacion = %s")
            valores.append(codigo_postal_educacion)
        if nombre_educacion:
            condiciones.append("nombre_educacion ILIKE %s")  
            valores.append(f"%{nombre_educacion}%")  
        if fecha_inicio:
            condiciones.append("fecha_inicio = %s")
            valores.append(fecha_inicio)

        if condiciones:
            consulta += ' WHERE ' + ' AND '.join(condiciones)

        cursor.execute(consulta, tuple(valores))
        resultado_educacion = cursor.fetchall()
        return resultado_educacion

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "Error en consulta"}
    
    finally: 
        cursor.close()
        db.close()

# INSERTAR CENTRO EDUCATIVO

def insertarCentroEducacion(nombre_educacion, codigo_postal_educacion=None, fecha_inicio=None):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor()

    try:
        consulta = "INSERT INTO centro_educacion (nombre_educacion, codigo_postal_educacion, fecha_inicio) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (nombre_educacion, codigo_postal_educacion, fecha_inicio))
        db.commit()

        if cursor.rowcount > 0:
            return {"mensaje": "Centro educativo insertado"}, 201
        else:
            return {"error": "No se pudo insertar el centro educativo"}, 500
    
    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "Error en consulta"}
    
    finally:
        cursor.close()
        db.close()

# ACTUALIZAR CENTRO EDUCATIVO

def actualizarCentroEducacion(id_educacion, nombre_educacion, codigo_postal_educacion=None, fecha_inicio=None):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor()
    
    try:
        consulta = "UPDATE centro_educacion SET nombre_educacion = %s, codigo_postal_educacion = %s, fecha_inicio = %s WHERE id_educacion = %s"
        cursor.execute(consulta, (nombre_educacion, codigo_postal_educacion, fecha_inicio, id_educacion))
        db.commit()

        if cursor.rowcount > 0:
            return {"mensaje": "Centro de educacion actualizado"}, 200
        else:
            return {"error": "No se encontro el centro para actualizar"}, 404

    except mysql.Error as error:
        print(f"Error al actualizar centro educativo: {error}")
        return {"error": "Error al actualizar"}

    finally:
        cursor.close()
        db.close()

# BORRAR CENTRO EDUCATIVO POR ID

def borrarCentroEducacion(id_educacion):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor()

    try:
        consulta = "DELETE FROM centro_educacion WHERE id_educacion = %s"
        cursor.execute(consulta, (id_educacion,))
        db.commit()
        
        if cursor.rowcount > 0:
            return {"mensaje": "Centro educativo eliminado"}, 204
        else:
            return {"error": "No se encontro el centro para eliminar"}, 404

    except mysql.Error as error:
        print(f"Error al borrar centro educativo: {error}")
        return {"error": "Error al borrar"}

    finally:
        cursor.close()
        db.close()



# CENTRO SANIDAD



# LLAMADA AL CENTRO SANITARIO

def llamadaCentroSanidad(id_sanidad=None, codigo_postal_sanidad=None, nombre_sanidad=None, nombre_barrio=None):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor(dictionary=True)

    try:
        consulta = 'SELECT id_sanidad, codigo_postal_sanidad, nombre_sanidad, nombre_barrio FROM centro_sanidad'
        condiciones = []
        valores = []

        if id_sanidad:
            condiciones.append("id_sanidad = %s")
            valores.append(id_sanidad)
        if codigo_postal_sanidad:
            condiciones.append("codigo_postal_sanidad = %s")
            valores.append(codigo_postal_sanidad)
        if nombre_sanidad:
            condiciones.append("nombre_sanidad ILIKE %s")
            valores.append(f"%{nombre_sanidad}%")
        if nombre_barrio:
            condiciones.append("nombre_barrio = %s")
            valores.append(nombre_barrio)

        if condiciones:
            consulta += ' WHERE ' + ' AND '.join(condiciones)

        cursor.execute(consulta, tuple(valores))
        resultado_sanidad = cursor.fetchall()
        return resultado_sanidad

    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "Error en consulta"}
    
    finally:
        cursor.close()
        db.close()

# INSERTAR NUEVO CENTRO SANITARIO

def insertarCentroSanidad(nombre_sanidad, codigo_postal_sanidad=None, nombre_barrio=None):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor()

    try:
        consulta = "INSERT INTO centro_sanidad (nombre_sanidad, codigo_postal_sanidad, nombre_barrio) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (nombre_sanidad, codigo_postal_sanidad, nombre_barrio))
        db.commit()

        if cursor.rowcount > 0:
            return {"mensaje": "Centro sanidad insertado"}, 201
        else:
            return {"error": "No se pudo insertar el centro de sanidad"}, 500
    
    except mysql.Error as error:
        print(f"Error en consulta: {error}")
        return {"error": "Error en consulta"}
    
    finally:
        cursor.close()
        db.close()

# ACTUALIZAR CENTRO SANITARIO

def actualizarCentroSanidad(id_sanidad, nombre_sanidad, codigo_postal_sanidad=None, nombre_barrio=None):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor()

    try:
        consulta = "UPDATE centro_sanidad SET nombre_sanidad = %s, codigo_postal_sanidad = %s, nombre_barrio = %s WHERE id_sanidad = %s"
        cursor.execute(consulta, (nombre_sanidad, codigo_postal_sanidad, nombre_barrio, id_sanidad))
        db.commit()

        if cursor.rowcount > 0:
            return {"mensaje": "Centro de sanidad actualizado"}, 200
        else:
            return {"error": "No se encontrO el centro para actualizar"}, 404

    except mysql.Error as error:
        print(f"Error al actualizar centro sanitario: {error}")
        return {"error": "Error al actualizar"}
    
    finally:
        cursor.close()
        db.close()

# BORRAR CENTRO SANITARIO POR ID

def borrarCentroSanidad(id_sanidad):
    db = conectarDB()
    if not db:
        return {"error": "Error de conexion en base de datos"}

    cursor = db.cursor()

    try:
        consulta = "DELETE FROM centro_sanidad WHERE id_sanidad = %s"
        cursor.execute(consulta, (id_sanidad,))
        db.commit()
        
        if cursor.rowcount > 0:
            return {"mensaje": "Centro sanitario eliminado"}, 204
        else:
            return {"error": "No se encontro el centro sanitario para eliminar"}, 404

    except mysql.Error as error:
        print(f"Error al borrar centro sanitario: {error}")
        return {"error": "Error al borrar"}




    finally:
        cursor.close()
        db.close()
