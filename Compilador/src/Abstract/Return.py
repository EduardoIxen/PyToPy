class Return:
    def __init__(self, valor, tipo, esTemporal, tipoAuxiliar = ''):
        self.valor = valor
        self.tipo = tipo
        self.esTemporal = esTemporal
        self.tipoAuxiliar = tipoAuxiliar
        self.etiquetaTrue = ''
        self.etiquetaFalse = ''
        self.atributos = [] #lista de tipos de los atrib del struct que no se definieron
        self.valores = []

    def getValor(self):
        return self.valor

    def getTipo(self):
        return self.tipo

    def getTipoAux(self):
        return self.tipoAuxiliar

    def setTipoAux(self, tipoAux):
        self.tipoAuxiliar = tipoAux

    def setAtributos(self, atributos):
        self.atributos = atributos

    def getAtributos(self):
        return self.atributos

    def setValores(self, valores):
        self.valores = valores

    def getValores(self):
        return self.valores
