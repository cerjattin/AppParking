from flask import Flask,Blueprint,request,redirect,render_template,jsonify
from config.db import app,db,ma

from models.InputOutputModel import InputsOutputsSchema,InputsOutputs

ruta_inputsoutput = Blueprint("route_inputsoutput",__name__)

inputoutput_schema = InputsOutputsSchema
inputoutputs_schema = InputsOutputsSchema(many=True) 

@ruta_inputsoutput.route("/inputoutput" , methods=["GET"])
def getAllinputoutput():
    inputoutput = InputsOutputs.query.all() 
    result = inputoutputs_schema.dump(inputoutput)
    return jsonify(result)  

@ruta_inputsoutput.route('/addInputOutput',methods=['POST'])
def addCategory():  
    recorddate = request.json['recorddate']
    typerecord= request.json['typerecord']
    recordtype= request.json['recordtype']
    idauthorized_fk=request.json['idauthorized_fk']
    newinputoutput = InputsOutputs(recorddate,typerecord,recordtype,idauthorized_fk)
    db.session.add(newinputoutput)
    db.session.commit()
    return "Guardado"

@ruta_inputsoutput.route("/deleteinputoutput/<id>", methods=["DELETE"])
def deleteInputOutput(id):        
    inputsoutputsBd = InputsOutputs.query.get(id)        
    db.session.delete(inputsoutputsBd)                     
    db.session.commit()    
    return "Eliminado con exito"

@ruta_inputsoutput.route("/updateinputoutput", methods= ["PUT"])
def updateInputOutput(): 
    id = request.json['id']
    InputsOutputs = InputsOutputs.query.get(id)
    InputsOutputs.recorddate = request.json['recorddate']
    InputsOutputs.typerecord= request.json['typerecord']
    InputsOutputs.recordtype= request.json['recordtype']
    InputsOutputs.idauthorized_fk=request.json['idauthorized_fk']       
    db.session.commit()                        
    return "Actualizado exitosamente"   

if __name__ == '__main__':
    app.run(debug=True)     
