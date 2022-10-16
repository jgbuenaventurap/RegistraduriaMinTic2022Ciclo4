from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
cors = CORS(app)
from Controladores.ControladorAdministrador import ControladorAdministrador
miControladorAdministrador=ControladorAdministrador()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/Candidatos",methods=['GET'])
def getEstudiantes():
    json=miControladorAdministrador.index()
    return jsonify(json)

@app.route("/Candidatos",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorAdministrador.create(data)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorAdministrador.show(id)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorAdministrador.update(id,data)
    return jsonify(json)

@app.route("/Candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorAdministrador.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

