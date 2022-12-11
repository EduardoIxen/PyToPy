from flask import Flask, request
from flask_cors import CORS


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
    salidaC3D = ""

    try:
        entrada = request.json['entrada']
        print(entrada)
        return {"result": "todo bien2",
                "err": "[]",
                "symbol": simbolos},200
    except:
        return {"result":salidaC3D,
                "err": errores,
                "symbol": simbolos},200


if __name__ == '__main__':
    app.debug = True
    app.run()