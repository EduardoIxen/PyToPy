from src.Ast.Tipo import Tipo
from src.Ast.SimboloFunc import SimboloFunc
from src.Ast.Simbolo import Simbolo


class Entorno:
    def __init__(self, anterior):
        self.anterior = anterior
        self.nombre = ""
        self.variables = {}
        self.funciones = {}
        self.structs = {}
        self.simboloStructs = {}

        self.tamanio = 0
        self.etiquetaBreak = ''
        self.etiquetaContinue = ''
        self.etiquetaReturn = ''
        self.funcionActual = None

        if anterior is not None:
            self.tamanio = self.anterior.tamanio
            self.etiquetaBreak = self.anterior.etiquetaBreak
            self.etiquetaContinue = self.anterior.etiquetaContinue
            self.etiquetaReturn = self.anterior.etiquetaReturn
            self.funcionActual = self.anterior.funcionActual

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def getVariables(self):
        return self.variables

    def getStructs(self):
        return self.structs

    def getFunciones(self):
        return self.funciones

    def getVariable(self, id):
        _entorno = self
        while _entorno is not None:
            if id in _entorno.variables.keys():
                return _entorno.variables[id]
            _entorno = _entorno.anterior
        return None

    def setVariable(self, id, tipo, posHeap, tipoAux='', tipoAtributos = [], valores = []):
        if id in self.variables.keys():
            print(f"Error// La variable {id} ya existe")
        else:
            nuevoSimbolo = Simbolo(id, tipo, self.tamanio, self.anterior == None, posHeap)
            nuevoSimbolo.setTipoAux(tipoAux)
            nuevoSimbolo.setAtributos(tipoAtributos)
            nuevoSimbolo.setValores(valores)
            nuevoSimbolo.setEntorno(self.nombre)
            self.tamanio += 1
            self.variables[id] = nuevoSimbolo
        return self.variables[id]

    def getEntornoGlobal(self):
        entorno = self
        while entorno.anterior is not None:
            entorno = entorno.anterior
        return entorno

    def getEntornoIf(self):
        entorno = self
        while entorno.anterior is not None:
            if entorno.nombre != "if":
                break
            entorno = entorno.anterior
        return entorno

    def getEntornoFor(self):
        entorno = self
        while entorno.anterior is not None:
            if entorno.nombre != "for":
                break
            entorno = entorno.anterior
        return entorno

    def getTamanio(self):
        return self.tamanio

    def getGlbl(self):
        ento = self
        while ento.prev is not None:
            ento = ento.prev
        return ento

    def setEntornoFuncion(self, funcionActual, etiquetaReturn):
        self.etiquetaReturn = etiquetaReturn
        self.tamanio = 1
        self.funcionActual = funcionActual

    def getFuncion(self, identificador):
        return self.funciones[identificador]

    def obtenerFuncion(self, identificador):
        entorno = self
        while entorno is not None:
            if identificador in entorno.funciones.keys():
                return entorno.funciones[identificador]
            entorno = entorno.anterior

        return None

    def setStruct(self, identificador, struct, tipo):
        nuevoSimbolo = Simbolo(id, tipo, self.tamanio, self.anterior == None, False)
        nuevoSimbolo.setTipoAux(identificador)
        nuevoSimbolo.setAtributos(struct.atributos)
        self.structs[identificador] = nuevoSimbolo

    def getStruct(self, identificador):
        entorno = self
        while entorno is not None:
            if identificador in entorno.structs.keys():
                return entorno.structs[identificador]
            entorno = entorno.anterior
        return None


    def agregarFuncion(self, identificador, funcion):
        tipoAux = ''
        if identificador not in self.funciones.keys():
            if funcion.tipo == Tipo.ANY:
                _tipo = Tipo.INT
            else:
                _tipo = funcion.tipo
                tipoAux = _tipo
                if isinstance(_tipo, str):
                    _tipo = self.getStruct(_tipo).getTipo()

            structFunc = SimboloFunc(identificador, _tipo, len(funcion.parametros), funcion.parametros, funcion.linea, funcion.columna)
            structFunc.setEntorno(self.nombre)
            structFunc.setTipoAux(tipoAux)
            self.funciones[identificador] = structFunc
            return True
        return False
