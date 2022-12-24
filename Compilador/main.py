from flask import Flask, request
from flask_cors import CORS
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Ast.Entorno import Entorno
from Gramatica import gramatica
from Gramatica.Optimizador import optimizadorGramatica

app = Flask(__name__)
CORS(app)

route = 'api'

@app.route('/')
def index():
    return {"msg": "Eduardo Ixen 201800524"}

@app.post("/compilar")
def compilar():
    errores = ""
    simbolos = ""
    salidaGo = ""

    try:
        entrada = request.json['entrada']

        nuevaInstanciaC3D = GeneradorC3D()
        nuevaInstanciaC3D.resetGenerador()
        genC3D = nuevaInstanciaC3D.getInstance()

        resultado = gramatica.parse(entrada)

        nuevoEntorno = Entorno(None)
        nuevoEntorno.setNombre('global')
        resultado.compilar(nuevoEntorno)

        resultado.getSimbolos()
        salidaGo = genC3D.obtenerC3D()
        errores = genC3D.getExcepciones()

        for simb in resultado.getSimbolos():
            simbolos += resultado.getSimbolos()[simb]

        simbolos = "[" + simbolos[:-1] + "]"        #no ,

        return {"result": salidaGo,
                "err": errores,
                "symbol": simbolos}, 200
    except Exception as e:
        print(e)
        errores = genC3D.getExcepciones()
        return {"result":salidaGo,
                "err": errores,
                "symbol": simbolos}, 200

@app.post("/mirilla")
def mirilla():
    entrada = request.json['input']
    data = ejecutarMirilla(entrada)
    print(data)
    return {"data": data}, 200

def ejecutarMirilla(entrada):
    try:
        instrucciones = optimizadorGramatica.parse(entrada)
        instrucciones.mirilla()
        salida = instrucciones.get_code()
        print(salida, "salidaaaaaaa")
        return str(salida)
    except:
        return {'Optimizador', 'Error al ejecutar'}

if __name__ == '__main__':
    app.debug = True
    app.run()
