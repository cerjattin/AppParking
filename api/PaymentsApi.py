from flask import Flask,Blueprint,request,redirect,render_template,jsonify
from config.db import app,db,ma

from models.PaymentsModel import Payments,PaymentsSchema

ruta_payments = Blueprint("route_payments",__name__)

payment_schema = PaymentsSchema
payments_schema = PaymentsSchema(many=True) 

@ruta_payments.route("/payments" , methods=["GET"])
def getAllPayments():
    payment = Payments.query.all() 
    result = payments_schema.dump(payment)
    return jsonify(result)  

@ruta_payments.route('/addpayments',methods=['POST'])
def addpaymets():  
    datepaid = request.json['datepaid']
    valuepaid=request.json['valuepaid']
    idUser_fk=request.json['idUser_fk']
    idOwner_fk=request.json['idOwner_fk']
    new_payment = Payments(datepaid,valuepaid,idUser_fk,idOwner_fk)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message":"Payment added successfully"})
    

@ruta_payments.route("/deletePayments/<id>", methods=["DELETE"])
def deletePayments(id):        
    paymentsBd = Payments.query.get(id)        
    db.session.delete(paymentsBd)                     
    db.session.commit()    
    return "Eliminado con exito"

@ruta_payments.route("/updatePayments", methods= ["PUT"])
def updatePayments(): 
    id = request.json['id']
    Payments = Payments.query.get(id)       
    Payments.datepaid = request.json['datepaid']                           
    Payments.valuepaid = request.json['valuepaid']
    Payments.idUser_fk = request.json['idUser_fk']
    Payments.idOwner_fk = request.json['idOwner_fk']
    db.session.commit()                        
    return "Actualizado exitosamente"   

if __name__ == '__main__':
    app.run(debug=True)     
