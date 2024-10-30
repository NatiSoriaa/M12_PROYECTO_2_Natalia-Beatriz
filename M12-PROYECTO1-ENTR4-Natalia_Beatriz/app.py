# APP CON CONEXION SWAGGER

from flask import Flask, jsonify, request
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import FlaskApiSpec, doc, use_kwargs
from flask_swagger_ui import get_swaggerui_blueprint
from marshmallow import Schema, fields
from bd import (
    llamadaCentroEducacion,
    insertarCentroEducacion,
    actualizarCentroEducacion,
    borrarCentroEducacion,
    llamadaCentroSanidad,
    insertarCentroSanidad,
    actualizarCentroSanidad,
    borrarCentroSanidad
)

app = Flask(__name__)


# CONFIGURACION DE SWAGGER
app.config.update({
    'APISPEC_SPEC': APISpec(
        title="API Centros",
        version="1.0.0",
        plugins=[MarshmallowPlugin()],
        openapi_version="3.0.2"
    ),
    'APISPEC_SWAGGER_URL': '/swagger.json',  
})

# Inicializar y registrar documentacion
docs = FlaskApiSpec(app)

# Configuracion de seguridad
app.config['APISPEC_SWAGGER_URL'] = '/swagger/'  
app.config['APISPEC_SWAGGER_UI'] = True

# Definicion de la API Key en la configuracion de Swagger
app.config['APISPEC_SPEC'].components.security_scheme(
    'apiKey',
    {
        'type': 'apiKey',
        'name': 'x-api-key',  
        'in': 'header'  
    }
)

# CONFIGURACIÓN DE SWAGGER UI
SWAGGER_URL = '/swagger-ui'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={
        'app_name': "API Centros"  
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# RUTA SWAGGER JSON
@app.route('/swagger.json')
def swagger_json():
    return jsonify(docs.spec.to_dict())  

# Funcion para verificar la API Key
def verificar_api_key(api_key):
    return api_key == "123"

# Definicion de Schemas para validacion
class CentroEducacionSchema(Schema):
    nombre_educacion = fields.String(required=True)
    codigo_postal_educacion = fields.String(required=False)
    fecha_inicio = fields.String(required=False)

class CentroSanidadSchema(Schema):
    nombre_sanidad = fields.String(required=True)
    codigo_postal_sanidad = fields.String(required=False)
    nombre_barrio = fields.String(required=False)




# RUTAS PARA CENTRO EDUCACION




# GET EDUCACION

@app.route('/centro_educacion', methods=['GET'])
@doc(description="Obtener todos los centros educativos", tags=['Centro Educacion'])
@use_kwargs({
    'id_educacion': fields.Integer(required=False, description="Filtrar por ID del centro educativo"),
    'codigo_postal_educacion': fields.String(required=False, description="Filtrar por codigo postal"),
    'nombre_educacion': fields.String(required=False, description="Filtrar por nombre del centro educativo"),
    'fecha_inicio': fields.String(required=False, description="Filtrar por fecha de inicio"),
}, location="query")
# OBTENER CENTRO 
def obtenerCentroEducacion(id_educacion=None, codigo_postal_educacion=None, nombre_educacion=None, fecha_inicio=None):
    resultados = llamadaCentroEducacion(
        id_educacion=id_educacion,
        codigo_postal_educacion=codigo_postal_educacion,
        nombre_educacion=nombre_educacion,
        fecha_inicio=fecha_inicio
    )
    return jsonify(resultados)

# POST EDUCACION

@app.route('/centro_educacion', methods=['POST'])
@use_kwargs(CentroEducacionSchema, location="json")
@doc(description="Insertar un nuevo centro educativo", tags=['Centro Educacion'])
# CREAR CENTRO 
def crearCentroEducacion(nombre_educacion, codigo_postal_educacion=None, fecha_inicio=None):
    return insertarCentroEducacion(nombre_educacion, codigo_postal_educacion, fecha_inicio)

# PUT EDUCACION

@app.route('/centro_educacion/<int:id_educacion>', methods=['PUT'])
@use_kwargs(CentroEducacionSchema, location="json")
@doc(description="Actualizar un centro educativo", tags=['Centro Educacion'])
# ACTUALIZAR CENTRO 
def actualizarCentroEducacionRoute(id_educacion, nombre_educacion, codigo_postal_educacion=None, fecha_inicio=None):
    return actualizarCentroEducacion(id_educacion, nombre_educacion, codigo_postal_educacion, fecha_inicio)

# DELETE EDUCACION

@app.route('/centro_educacion/<int:id_educacion>', methods=['DELETE'])
@doc(description="Eliminar un centro educativo", tags=['Centro Educacion'])
# BORRAR CENTRO 
def borrarCentroEducacionRoute(id_educacion):
    return borrarCentroEducacion(id_educacion)




# RUTAS PARA CENTRO SANIDAD




# GET SANIDAD

@app.route('/centro_sanidad', methods=['GET'])
@doc(description="Obtener todos los centros de sanidad", tags=['Centro Sanidad'])
@use_kwargs({
    'id_sanidad': fields.Integer(required=False, description="Filtrar por ID del centro de sanidad"),
    'codigo_postal_sanidad': fields.String(required=False, description="Filtrar por codigo postal"),
    'nombre_sanidad': fields.String(required=False, description="Filtrar por nombre del centro de sanidad"),
    'nombre_barrio': fields.String(required=False, description="Filtrar por nombre del barrio"),
}, location="query")
# OBTENER CENTRO 
def obtenerCentroSanidad(id_sanidad=None, codigo_postal_sanidad=None, nombre_sanidad=None, nombre_barrio=None):
    resultados = llamadaCentroSanidad(
        id_sanidad=id_sanidad,
        codigo_postal_sanidad=codigo_postal_sanidad,
        nombre_sanidad=nombre_sanidad,
        nombre_barrio=nombre_barrio
    )
    return jsonify(resultados)

#POST SANIDAD

@app.route('/centro_sanidad', methods=['POST'])
@use_kwargs(CentroSanidadSchema, location="json")
@doc(description="Insertar un nuevo centro de sanidad", tags=['Centro Sanidad'])
# CREAR CENTRO 
def crearCentroSanidad(nombre_sanidad, codigo_postal_sanidad=None, nombre_barrio=None):
    return insertarCentroSanidad(nombre_sanidad, codigo_postal_sanidad, nombre_barrio)

# PUT SANIDAD

@app.route('/centro_sanidad/<int:id_sanidad>', methods=['PUT'])
@use_kwargs(CentroSanidadSchema, location="json")
@doc(description="Actualizar un centro de sanidad", tags=['Centro Sanidad'])
# ACTUALIZAR CENTRO
def actualizarCentroSanidadRoute(id_sanidad, nombre_sanidad, codigo_postal_sanidad=None, nombre_barrio=None):
    return actualizarCentroSanidad(id_sanidad, nombre_sanidad, codigo_postal_sanidad, nombre_barrio)

# DELETE SANIDAD

@app.route('/centro_sanidad/<int:id_sanidad>', methods=['DELETE'])
@doc(description="Eliminar un centro de sanidad", tags=['Centro Sanidad'])
# BORRAR CENTRO
def borrarCentroSanidadRoute(id_sanidad):
    return borrarCentroSanidad(id_sanidad)



# REGISTRO DE LAS RUTAS



docs.register(obtenerCentroEducacion, endpoint='obtenerCentroEducacion')
docs.register(crearCentroEducacion, endpoint='crearCentroEducacion')
docs.register(actualizarCentroEducacionRoute, endpoint='actualizarCentroEducacionRoute')
docs.register(borrarCentroEducacionRoute, endpoint='borrarCentroEducacionRoute')
docs.register(obtenerCentroSanidad, endpoint='obtenerCentroSanidad')
docs.register(crearCentroSanidad, endpoint='crearCentroSanidad')
docs.register(actualizarCentroSanidadRoute, endpoint='actualizarCentroSanidadRoute')
docs.register(borrarCentroSanidadRoute, endpoint='borrarCentroSanidadRoute')



if __name__ == '__main__':
    app.run(debug=True, port=5001)
