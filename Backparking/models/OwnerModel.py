from config.db import db,app,ma
class Owner(db.Model):
    __tablename__='tblowners'
    id = db.Column(db.Integer,primary_key=True)
    nameowner = db.Column(db.String(30))
    lastnameowner = db.Column(db.String(30))
    addressowner = db.Column(db.String(50))
    phoneowner = db.Column(db.String(20))
    documentowner = db.Column(db.String(20))
    
    def __init__(self,documentowner):
        self.documentowner = documentowner
   
with app.app_context():
    db.create_all()

class OwnerSchema(ma.Schema):
    class Meta:
        fields=('id','nameowner','lastnameowner','addressowner','phoneowner','documentowner')