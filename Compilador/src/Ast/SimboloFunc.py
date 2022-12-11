class SimboloFunc:
    def __init__(self, id, tipo, tamanio, parametros, linea, columna):
        self.id = id
        self.tipo = tipo
        self.tamanio = tamanio
        self.parametros = parametros
        self.linea = linea
        self.columna = columna
        self.entorno = ''
        self.tipoAux = ''

    def getId(self):
        return self.id

    def getTipo(self):
        return self.tipo

    def getLinea(self):
        return self.linea

    def getColumna(self):
        return self.columna

    def getEntorno(self):
        return self.entorno

    def setEntorno(self, entorno):
        self.entorno = entorno

    def getTipoAux(self):
        return self.tipoAux

    def setTipoAux(self, tipoAux):
        self.tipoAux = tipoAux
