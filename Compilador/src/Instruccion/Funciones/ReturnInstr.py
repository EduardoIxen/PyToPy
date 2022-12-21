from src.Abstract.Expresion import Expresion
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo

class ReturnInstr(Expresion):
    def __init__(self, valorRet, linea, columna):
        super().__init__(linea, columna)
        self.valorRet = valorRet

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        if entorno.etiquetaReturn == '':
            genC3D.setExcepcion(Excepcion("Semantico", "Return fuera de una funcion.", self.linea, self.columna))
            return

        valor = self.valorRet.compilar(entorno)
        if valor.tipo == Tipo.BOOLEAN:
            etiquTemp = genC3D.nuevaEtiqueta()
            genC3D.agregarEtiqueta(valor.etiquetaTrue)
            genC3D.setStack('P', '1')
            genC3D.agregarGoto(etiquTemp)
            genC3D.agregarEtiqueta(valor.etiquetaFalse)
            genC3D.setStack('P', '0')
            genC3D.agregarEtiqueta(etiquTemp)
        else:
            genC3D.setStack('P', valor.valor)
        genC3D.agregarGoto(entorno.etiquetaReturn)
