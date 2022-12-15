from src.Abstract.Expresion import Expresion
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Return import Return
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo

class Unaria(Expresion):
    def __init__(self, expresion , linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        self.etiquetaTrue = ''
        self.etiquetaFalse = ''

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        temp = genC3D.agregarTemp()
        valor = self.expresion.compilar(entorno)
        if valor.tipo != Tipo.INT and valor.tipo != Tipo.FLOAT:
            genC3D.setExcepcion(Excepcion("Semantico", "Solo se puede negar datos de tipo numerico", self.linea, self.columna))
            return
        genC3D.agregarExpresion(temp, '0', valor.getValor(), '-')
        return Return(temp, valor.getTipo(), True)

