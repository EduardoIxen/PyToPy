class Simbolo:
    def __init__(self, id, tipo, pos = 0, varGlob = None, enHeap = None):
        self.id = id
        self.tipo = tipo
        self.posicion = pos
        self.esGlobal = varGlob
        self.enHeap = enHeap

        self.tipoAux = ''
        self.esTemporal = None
        self.etiquetaTrue = ''
        self.etiquetaFalse = ''
        self.atributos = []
        self.valores = []
        self.linea = 0
        self.columna = 0
        self.entorno = ""

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    def getLinea(self):
        return self.linea

    def getColumna(self):
        return self.columna

    def getTipoAux(self):
        return self.tipoAux

    def setTipoAux(self, tipoAux):
        self.tipoAux = tipoAux

    def getEsTemporal(self):
        return self.esTemporal

    def setEsTemp(self, esTemp):
        self.esTemporal = esTemp

    def getAtributos(self):
        return self.atributos

    def setAtributos(self, atributos):
        self.atributos = atributos

    def getEntorno(self):
        return self.entorno

    def setEntorno(self, entorno):
        self.entorno = entorno

    def getValores(self):
        return self.valores

    def setValores(self, valores):
        self.valores = valores
