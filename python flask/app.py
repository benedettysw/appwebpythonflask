from flask import Flask, render_template 

from conexion import app , db





#IMPORTACIONES DEL MODELO

from Model import clientes


#IMPORTACIONES DEL API "PROCEDIMIENTO"

from api.guardar import routes_guardar

app.register_blueprint(routes_guardar , url_prefix ="/fronted")



#VISTA PRINCIPAL
@app.route("/")
def inicio():
    return render_template("index.html")



#SENGUNDA VISTA 
@app.route("/vista2")
def inicio1():
    return "VISTA NUMEO 2"




if __name__ == "__main__":
    app.run(port=5000 , debug=True)