from flask import Flask, request, render_template 
from flask_cors import CORS 
from datetime import datetime 
import requests

app=Flask(__name__,template_folder='templates')
CORS(app)

predios_list = [
    {'codigo':'123', 'area':'123', 'latitud':'123', 'longitud':'123'}
]

terrenos_list = { "Planicie", "Ladera", "Cenagoso", "Desertico"}

@app.route('/', methods=['GET'])
def crearPredio():
    return render_template('crearPredio.html', terrenos=terrenos_list) 


@app.route('/listarPredios', methods=['GET'])
def listarPredios():
    predios_list= requests.get('https://api-evergreen-728.azurewebsites.net/Predios').json()
    return render_template('listarPredios.html', predios=predios_list) 

@app.route('/guardarPredio',methods=['POST'])
def guardarPredio():
    predio = dict(request.values)
    predio['area'] = int(predio['area'])
    requests.post('https://api-evergreen-728.azurewebsites.net/Predios',json=predio)
    return (listarPredios())
