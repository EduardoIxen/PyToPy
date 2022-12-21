from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Return import Return
from src.Abstract.Expresion import Expresion
from src.Ast.Tipo import Tipo


class RangeInstr(Expresion):
    def __init__(self, inicio, fin, linea, columna):
        super().__init__(linea, columna)
        self.inicio = inicio
        self.fin = fin

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        rangoTemp = genC3D.agregarTemp()
        inicio = self.inicio.compilar(entorno)
        fin = self.fin.compilar(entorno)

        genC3D.agregarExpresion(rangoTemp, 'H', '', '')
        genC3D.setHeap('H', inicio.getValor())
        genC3D.siguienteHeap()
        genC3D.setHeap('H', fin.getValor())
        genC3D.siguienteHeap()

        return Return(rangoTemp, Tipo.RANGE, True)