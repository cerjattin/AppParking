from config.db import db,app,ma
class Authorized(db.Model):
    __tablename__='tblauthorized'
    id = db.Column(db.Integer,primary_key=True)
    placaauthorized = db.Column(db.String(10))
    nameauthorized = db.Column(db.String(50))
    dateinit = db.Column(db.DateTime)
    dateend = db.Column(db.DateTime)
    status = db.Column(db.String(1))
    iduser_fk = db.Column(db.Integer,db.ForeignKey('tblusers.id'))
    idowner_fk = db.Column(db.Integer,db.ForeignKey('tblowners.id'))
    
    def __init__(self,placaauthorized,iduser_fk,idowner_fk,status):
        self.placaauthorized = placaauthorized
        self.iduser_fk=iduser_fk
        self.idowner_fk=idowner_fk
        self.status=status
with app.app_context():
    db.create_all()

class AuthorizedSchema(ma.Schema):
    class Meta:
        fields=('id','placaauthorized','nameauthorized','dateinit','dateend','status','iduser_fk','idowner_fk')