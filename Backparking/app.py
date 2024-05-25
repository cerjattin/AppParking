from flask import Flask,request,redirect,render_template
from config.db import app

from api.UsersApi import ruta_user
from api.CategoryApi import ruta_category
from api.OwnerApi import ruta_owners
from api.AuthorizedApi import ruta_authorized
from api.InputsOutputApi import ruta_inputsoutput
from api.PaymentsApi import ruta_payments

app.register_blueprint(ruta_user,url_prefix="/api")
app.register_blueprint(ruta_category,url_prefix="/api")
app.register_blueprint(ruta_owners,url_prefix="/api")
app.register_blueprint(ruta_category,url_prefix="/api")
app.register_blueprint(ruta_inputsoutput,url_prefix="/api")
app.register_blueprint(ruta_payments,url_prefix="/api")

@app.route("/")
def index():
    return "Hola"

if __name__=="__main__":
    app.run(debug=True,port=5000,host="0.0.0.0")
    