# SCHEMAS 

from marshmallow import Schema, fields, validate


# SCHEMA EDUCACION

class CentroEducacionSchema(Schema):
    id_educacion = fields.Int(required=True, description="ID del centro de educacion")

    codigo_postal_educacion = fields.Str(
        description="Codigo postal del centro educativo",
        validate=validate.Length(max=10)
    )

    nombre_educacion = fields.Str(
        required=True,
        description="Nombre del centro educativo",
        validate=validate.Length(max=100)
    )

    fecha_inicio = fields.Date(description="Fecha de inicio del centro educativo")

# SCHEMA SANIDAD

class CentroSanidadSchema(Schema):
    id_sanidad = fields.Int(required=True, description="ID del centro de sanidad")

    codigo_postal_sanidad = fields.Str(
        description="Codigo postal del centro sanitario",
        validate=validate.Length(max=10)
    )

    nombre_sanidad = fields.Str(
        required=True,
        description="Nombre del centro sanitario",
        validate=validate.Length(max=100)
    )

    nombre_barrio = fields.Str(
        description="Nombre del barrio donde se ubica el centro",
        validate=validate.Length(max=50)
    )

# FILTRO EDUCACION

class FiltroEducacionSchema(Schema):
    id_educacion = fields.Int(required=False, description="Filtrar por ID del centro educativo")
    codigo_postal_educacion = fields.Str(required=False, description="Filtrar por codigo postal")
    nombre_educacion = fields.Str(required=False, description="Filtrar por nombre del centro educativo")
    fecha_inicio = fields.Date(required=False, description="Filtrar por fecha de inicio")

# FILTRO SANIDAD

class FiltroSanidadSchema(Schema):
    id_sanidad = fields.Int(required=False, description="Filtrar por ID del centro sanitario")
    codigo_postal_sanidad = fields.Str(required=False, description="Filtrar por codigo postal")
    nombre_sanidad = fields.Str(required=False, description="Filtrar por nombre del centro sanitario", validate=validate.Length(max=100))
    nombre_barrio = fields.Str(required=False, description="Filtrar por nombre del barrio", validate=validate.Length(max=50))
