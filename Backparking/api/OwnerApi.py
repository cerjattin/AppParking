from flask import Flask,Blueprint,request,redirect,render_template,jsonify
from config.db import app,db,ma

from models.OwnerModel import Owner,OwnerSchema

ruta_owners = Blueprint("route_owners",__name__)

Owner_schema = OwnerSchema()
Owner_schema = OwnerSchema(many=True) 

@ruta_category.route("/owners" , methods=["GET"])
def getAllOwners():
    owners = owners.query.all() 
    result = Owner_schema.dump(owners)
    return jsonify(result)  

@ruta_category.route('/addowners',methods=['POST'])
def addOwners():  
    namecategory = request.json['namecategory']
    newcategory = Category(namecategory)
    db.session.add(newcategory)
    db.session.commit()
    return "Guardado"

@ruta_category.route("/deleteCategory/<id>", methods=["DELETE"])
def deleteCategory(id):        
    categoryBd = Category.query.get(id)        
    db.session.delete(categoryBd)                     
    db.session.commit()    
    return "Eliminado con exito"

@ruta_category.route("/updateCategory", methods= ["PUT"])
def updateCategory(): 
    id = request.json['id']
    category = Category.query.get(id)       
    category.namecategory = request.json['namecategory']                           
    db.session.commit()                        
    return "Actualizado exitosamente"   

if __name__ == '__main__':
    app.run(debug=True)     
