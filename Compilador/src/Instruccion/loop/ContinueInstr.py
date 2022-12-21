from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion

class ContinueInstr(Instruccion):
    def __init__(self, linea, columna):
        super().__init__(linea, columna)

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.agregarGoto(entorno.etiquetaContinue)