from src.Abstract.Instruccion import Instruccion
from Tipo import Tipo


class AST(Instruccion):
    def __init__(self, instrucciones, linea, columna):
        super().__init__(linea, columna)
        self.instrucciones = instrucciones
        self.entornoGlobal = None

    def compilador(self, entorno):
        for instr in self.instrucciones:
            instr.compilar(entorno)
        self.entornoGlobal = entorno

    def getSimbolo(self):
        simbolos = {}
        for id in self.entornoGlobal.getVariables():
            valor = self.entornoGlobal.getVariables()[id]
            if valor.getTipoAux() != '':
                _tipo = valor.getTipoAux()
            else:
                _tipo = self.getTipo(valor)

            cadena = f"\"column1\": \"{valor.getId()}\", \"column2\": \"{_tipo}\", \"column3\": \"{valor.getEntorno()}\", \"column4\": \"{valor.getLinea()}\", \"column5\": \"{valor.getColumna()}\""
            cadena = "{" + cadena + "},"
            simbolos[valor.getId()] = cadena

        for id in self.entornoGlobal.getFunciones():
            valor = self.entornoGlobal.getFunciones()[id]
            cadena = f"\"column1\": \"{valor.getId()}\", \"column2\": \"{self.getTipo(valor)}\", \"column3\": \"{valor.getEntorno()}\", \"column4\": \"{valor.getLinea()}\", \"column5\": \"{valor.getColumna()}\""
            cadena = "{" + cadena + "}"
            simbolos[valor.getId()] = cadena

        return simbolos

    def getTipo(self, value):
        if (value.getTipo() == Tipo.INT):
            return "int"
        elif (value.getTipo() == Tipo.FLOAT):
            return "float"
        elif (value.getTipo() == Tipo.STRING):
            return "string"
        elif (value.getTipo() == Tipo.BOOLEAN):
            return "bool"
        elif (value.getTipo() == Tipo.CHAR):
            return "char"
        elif (value.getTipo() == Tipo.LIST):
            return "list"
        elif (value.getTipo() == Tipo.ANY):
            return "Any"
        elif (value.getTipo() == Tipo.FUNCION):
            return "funcion"
        elif (value.getTipo() == Tipo.STRUCT):
            return "struct"
        elif (value.getTipo() == Tipo.NULL):
            return "None"
