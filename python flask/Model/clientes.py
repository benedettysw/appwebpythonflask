from conexion import db , app , ma

class clientes(db.Model):
    __tablename__ = "clientes"

#ATRIBUTOS DE LA TABLA 
    id = db.Column(db.Integer , primary_key = True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))


    def __init__(self , nombre , apellido ):
        self.nombre = nombre
        self.apellido = apellido

with app.app_context():
    db.create_all()

    
        
