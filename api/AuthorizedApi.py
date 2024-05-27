from flask import Flask,Blueprint,request,redirect,render_template,jsonify
from config.db import app,db,ma

from models.AuthorizedModel import Authorized,AuthorizedSchema

ruta_authorized = Blueprint("route_authorized",__name__)

Authorized_schema = AuthorizedSchema()
Authorized_schema = AuthorizedSchema(many=True) 

@ruta_authorized.route("/authorized" , methods=["GET"])
def getAllauthorized():
    authorized = Authorized.query.all() 
    result = Authorized_schema.dump(authorized)
    return jsonify(result)  

@ruta_authorized.route('/addauthorized',methods=['POST'])
def addauthorized():  
    placaauthorized = request.json['placaauthorized']
    nameauthorized=request.json['nameauthorized']
    dateinit=request.json['dateinit']
    dateend=request.json['dateend']
    status=request.json['status']
    iduser_fk=request.json['iduser_fk']
    idowner_fk=request.json['idowner_fk']
    authorized = Authorized(placaauthorized, nameauthorized, dateinit, dateend, status,iduser_fk,idowner_fk)
    db.session.add(authorized)
    db.session.commit()
    return "Guardado"

@ruta_authorized.route("/deleteAuthorized/<id>", methods=["DELETE"])
def deleteAuthorized(id):        
    authorizeddb = Authorized.query.get(id)        
    db.session.delete(authorizeddb)                     
    db.session.commit()    
    return "Eliminado con exito"

@ruta_authorized.route("/updateAuthorized", methods= ["PUT"])
def updateAuthorized(): 
    id = request.json['id']
    Authorized = Authorized.query.get(id)
    Authorized.placaauthorized = request.json['placaauthorized']
    Authorized.nameauthorized = request.json['nameauthorized']
    Authorized.dateinit = request.json['dateinit']
    Authorized.dateend = request.json['dateend']
    Authorized.status = request.json['status']
    Authorized.iduser_fk = request.json['iduser_fk']
    Authorized.idowner_fk = request.json['idowner_fk']
    db.session.commit()                        
    return "Actualizado exitosamente"   

if __name__ == '__main__':
    app.run(debug=True)     
