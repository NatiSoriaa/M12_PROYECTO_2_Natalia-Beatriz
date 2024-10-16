#INSTANCIAS Y RUTAS

from flask import Flask, request, jsonify
from bd import    (
    llamadaCentroEducacion,
    llamadaCentroSanidad,
    insertarCentroEducacion,
    actualizarCentroEducacion,
    borrarCentroEducacion,
    actualizarCentroSanidad,
    insertarCentroSanidad,
    borrarCentroSanidad,
)
from auth import validarApiKey

app = Flask(__name__)

#RUTA A CENTRO EDUCACION

@app.route('/centro_educacion', methods=['GET','POST','PUT','DELETE'])
def ObtenerCentroEducacion():
    if not validarApiKey(request):
        return jsonify({"error": "Acceso no autorizado"}), 401
    
    #GET: obtener centro educativo
    if request.method == 'GET':
        codigoPostalE = request.args.get('codigo_postal_educacion')
        nombreE = request.args.get('nombre_educacion')
        fechaInicioE = request.args.get('fecha_inicio')
        respuestaE = llamadaCentroEducacion(codigoPostalE, nombreE, fechaInicioE)
        
        if respuestaE:
            return jsonify(respuestaE), 200
        else:
            return jsonify({"error": "no se encuentra el centro educativo"}), 404

    #POST: insertar nuevo centro educativo
    elif request.method == 'POST':
        data=request.get_json()
        nombreE=data.get('nombre_educacion')
        nombreBarrio=data.get('nombre_barrio')

        if not nombreE or not nombreBarrio:
            return jsonify({"error": "faltan campos requeridos"})
        try:
            insertarCentroEducacion(nombreE, nombreBarrio)
            return jsonify({"mensaje": "centro educativo agregado"}), 201
        except Exception as error:
            return jsonify({"error": "error al agregar"}), 500
    
    #PUT: actualizar fecha_inicio a nuevaFecha
    elif request.method == 'PUT':
        data=request.get_json()
        IdCentro=data.get('id_educacion')
        nuevaFecha = data.get('fecha_inicio')
    
        if not IdCentro:
            return jsonify({"mensaje": "faltan campos requeridos"}), 400
        try:
            actualizarCentroEducacion(IdCentro, nuevaFecha)
            return jsonify({"mensaje": "fecha de inicio actualizada"}), 200
        except Exception as error:
            return jsonify({"error": "error al actualizar"}), 500

    #DELETE: borrar centro educativo por ID
    elif request.method == "DELETE":
        data=request.get_json()
        IdCentro =data.get('id_educacion')
        nombreE=data.get('nombre_educacion')

        if not IdCentro and not nombreE:
            return jsonify({"mensaje": "faltan campos requeridos"}), 400
        try:
            borrarCentroEducacion(IdCentro, nombreE)
            return jsonify({"mensaje": "Centro educativo borrado"}), 204
        except Exception as error:
            return jsonify({"error":"error al borrar"}), 500


#RUTA A CENTRO SANIDAD



@app.route('/centro_sanidad', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ObtenerCentroSanidad():
    if not validarApiKey(request):
        return jsonify({"error": "Acceso no autorizado"}), 401
    
    if request.method == 'GET':
        codigoPostalS = request.args.get('codigo_postal_sanidad')
        nombreS = request.args.get('nombre_sanidad')
        barrioS = request.args.get('nombre_barrio')
        respuestaS = llamadaCentroSanidad(codigoPostalS, nombreS, barrioS)
        if respuestaS:
            return jsonify(respuestaS), 200
        else:
          return jsonify({"error": "no se encuentra el centro de sanidad"}), 404
        data=request.get_json()
        
    elif request.method == 'POST':
        data=request.get_json()
        nombreS=data.get('nombre_sanidad')
        nombreBarrio=data.get('nombre_barrio')

        if not nombreS or not nombreBarrio:
            return jsonify({"error": "faltan campos requeridos"}), 400
        try:
            insertarCentroSanidad(nombreS, nombreBarrio)
            return jsonify({"mensaje": "centro sanitario agregado"}), 201
        except Exception as error:
            return jsonify({"error": "error al agregar"}), 500
    
    elif request.method == 'PUT':
        data=request.get_json()
        nombreS=data.get('nombre_sanidad')
        nombreBarrio=data.get('nombre_barrio')
        codigoPostalS=data.get('codigo_postal_sanidad')

        if not nombreS or not nombreBarrio or not codigoPostalS:
            return jsonify({"error": "faltan campos requeridos"}), 400
        try:
            actualizarCentroSanidad(nombreS, nombreBarrio, codigoPostalS)
            return jsonify ({"mensaje": "centro sanitario actualizado"}), 200
        except Exception as error:
            return jsonify({"error": "error al actualizar"}), 500
    elif request.method == 'DELETE':
        data=request.get_json()
        codigoPostalS=data.get('codigo_postal_sanidad')

        if not codigoPostalS:
            return jsonify({"error":"faltan campos requeridos"}), 400
        try:
            borrarCentroSanidad(codigoPostalS)
            return jsonify({"mensaje": "centro sanitario eliminado"}), 204
        except Exception as error:
            return jsonify({"error": "error al eliminar"}), 500


if __name__ == '__main__':
    app.run(debug=True)


    
    


