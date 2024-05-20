from config.db import db,app,ma

class Payments(db.Model):
    __tablename__="tblpayments"
    id = db.Column(db.Integer, primary_key = True)
    datepaid = db.Column(db.datetime())
    valuepaid = db.Column(db.integer)
    idUser_fk = db.Column(db.Integer, db.ForeignKey('tblusers.id'))
    idOwner_fk = db.Column(db.Integer,db.ForeignKey('tblowners.id'))
    def __init__(self, datepaid,idUser_fk,idOwner_fk): 
        self.datepaid = datepaid
        self.idUser_fk= idUser_fk
        self.idOwner_fk=idOwner_fk

with app.app_context():
    db.create_all()

class PaymentsSchema(ma.Schema):
    class Meta:
        fields =('id', 'datetime', 'valuepaid', 'idUser_fk','idOwner_fk')