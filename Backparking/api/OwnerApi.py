from flask import Flask,Blueprint,request,redirect,render_template,jsonify
from config.db import app,db,ma

from models.OwnerModel import Owner,OwnerSchema

ruta_owners = Blueprint("route_owners",__name__)

Owner_schema = OwnerSchema()
Owner_schema = OwnerSchema(many=True) 

@ruta_owners.route("/owners" , methods=["GET"])
def getAllOwners():
    owners = owners.query.all() 
    result = Owner_schema.dump(owners)
    return jsonify(result)  

@ruta_owners.route('/addowners',methods=['POST'])
def addOwners():  
    nameowner = request.json['nameowner']
    lastnameowner= request.json['lastnameowner']
    addressowner=request.json['addressowner']
    phoneowner=request.json['phoneowner']
    emailowner=request.json['emailowner']
    Newowner = Owner(nameowner,lastnameowner,addressowner,phoneowner,emailowner)
    db.session.add(Newowner)
    db.session.commit()
    return "Guardado"

@ruta_owners.route("/deleteOwner/<id>", methods=["DELETE"])
def deleteOwner(id):        
    ownerdb = Owner.query.get(id)        
    db.session.delete(ownerdb)                     
    db.session.commit()    
    return "Eliminado con exito"

@ruta_owners.route("/updateOwner", methods= ["PUT"])
def updateOwner(): 
    id = request.json['id']
    Owner = Owner.query.get(id)
    Owner.nameowner = request.json['nameowner']
    Owner.lastnameowner = request.json['lastnameowner']
    Owner.addressowner = request.json['addressowner']
    Owner.phoneowner = request.json['phoneowner']
    Owner.emailowner = request.json['emailowner']
    db.session.commit()                        
    return "Actualizado exitosamente"   

if __name__ == '__main__':
    app.run(debug=True)     
