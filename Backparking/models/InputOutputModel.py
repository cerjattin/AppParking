from config.db import db,app,ma
class InputsOutputs(db.Model):
    __tablename__='tblinputsaoutputs'
    id = db.Column(db.Integer,primary_key=True)
    recorddate = db.Column(db.datetime)
    typerecord = db.Column(db.String(10))
    idauthorized_fk = db.Column(db.Integer,db.ForeignKey('tblauthorized.id'))
    
    def __init__(self,recorddate,idauthorized_fk):
        self.recorddate = recorddate
        self.idauthorized_fk= idauthorized_fk
   
with app.app_context():
    db.create_all()

class InputsOutputsSchema(ma.Schema):
    class Meta:
        fields=('id','recorddate','typerecord','idauthorized_fk')