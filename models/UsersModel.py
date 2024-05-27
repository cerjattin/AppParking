from config.db import db, app, ma

class Users(db.Model):
    __tablename__ ='tblusers'

    id = db.Column(db.Integer, primary_key = True) 
    nameuser = db.Column(db.String(50))
    emailuser = db.Column(db.String(50))
    passworduser = db.Column(db.String(50))
    idCategory_fk = db.Column(db.Integer,db.ForeignKey('tblcategorys.id'))

    def __init__(self, nameuser, emailuser,passworduser,idCategory_fk):
        self.nameuser = nameuser
        self.emailuser = emailuser
        self.passworduser = passworduser
        self.idCategory_fk=idCategory_fk
    
with app.app_context():
    db.create_all()
    
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','nameuser','emailuser','passworduser','idCategory_fk')