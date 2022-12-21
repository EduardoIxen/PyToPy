from src.Abstract.Instruccion import Instruccion
from src.Ast.GeneradorC3D import GeneradorC3D

class BreakInstr(Instruccion):
    def __init__(self, linea, columna):
        super().__init__(linea, columna)

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.agregarGoto(entorno.etiquetaBreak)