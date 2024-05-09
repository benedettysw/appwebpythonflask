from conexion import db
from flask import Blueprint , request
from Model.clientes import clientes



routes_guardar = Blueprint ("routes_guardar" , __name__)

@routes_guardar.route("/guardar" , methods = ['POST'])
def guardar():

    nombre = request.json['nombre']
    apellido = request.json['apellido']

    #VALIDAR SI EL USUARIO YA ESTA REGISTRADO

    usuario_registrado = db.session.query(clientes).filter(clientes.nombre == nombre).first()

    if usuario_registrado:
        return "usuario existente"



    consulta = clientes(nombre , apellido)
    db.session.add(consulta)
    db.session.commit()

    return "datos guardados exitosamente"