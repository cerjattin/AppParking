from flask import Flask,Blueprint,request,redirect,render_template,jsonify
from config.db import app,db,ma

from models.UsersModel import Users,UsersSchema

ruta_user = Blueprint("route_user",__name__)
usuario_schema = UsersSchema()
usuarios_shema= UsersSchema(many=True)

@ruta_user.route("/user",methods=["GET"])
def alluser():
    resultAll = Users.query.all()
    respo = usuario_schema(resultAll)
    return jsonify(respo)

@ruta_user.route("/AddUsers", methods=['POST'])
def addUsers():
    nameuser= request.json['nameuser']
    emailuser = request.json['emailuser']
    passworduser= request.json['passworduser']
    user = Users(nameuser, emailuser, passworduser)
    db.session.add(user)
    db.session.commit()
    return "Guardado"

@ruta_user.route("DeleteUsers", methods=['DELETE'])
def DeleteUsers():
    id = request.json['id'] 
    usuario = Users.query.get(id)    
    db.session.delete(usuario)
    db.session.commit()     
    return jsonify(usuario_schema.dump(usuario))
