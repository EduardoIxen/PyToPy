from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Expresion import Expresion
from src.Abstract.Return import Return
from src.Ast.Tipo import TipoOperacion
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo

class Logica(Expresion):
    def __init__(self, izq, der, tipoOp, linea, columna):
        super().__init__(linea, columna)
        self.izq = izq
        self.der = der
        self.tipoOp = tipoOp

    def compilar(self, entorno):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()
        self.verifEtiquTrueFalse()
        etiquAndOr = ''
        auxReturn = Return(None, Tipo.BOOLEAN, False)

        if self.tipoOp == TipoOperacion.AND:
            etiquAndOr = self.izq.etiquetaTrue = genC3D.nuevaEtiqueta()
            self.der.etiquetaTrue = self.etiquetaTrue
            self.izq.etiquetaFalse = self.der.etiquetaFalse = self.etiquetaFalse
        elif self.tipoOp == TipoOperacion.OR:
            self.izq.etiquetaTrue = self.der.etiquetaTrue = self.etiquetaTrue
            etiquAndOr = self.izq.etiquetaFalse = genC3D.nuevaEtiqueta()
            self.der.etiquetaFalse = self.etiquetaFalse
        else:
            '''auxReturn.etiquetaTrue = self.etiquetaFalse
            auxReturn.etiquetaFalse = self.etiquetaTrue
            return auxReturn'''
            self.izq.etiquetaTrue = self.der.etiquetaTrue = self.etiquetaFalse
            self.izq.etiquetaFalse = self.der.etiquetaFalse = self.etiquetaTrue

        opIzq = self.izq.compilar(entorno)
        if opIzq.getTipo() != Tipo.BOOLEAN:
            genC3D.setExcepcion(Excepcion("Semantico", "Solo se pueden operar operaciones booleanas", self.linea, self.columna))
            return

        if etiquAndOr != '':
            genC3D.agregarEtiqueta(etiquAndOr)

        opDer = self.der.compilar(entorno)
        if opDer.getTipo() != Tipo.BOOLEAN:
            genC3D.setExcepcion(Excepcion("Semantico", "Solo se pueden operar operaciones booleanas", self.linea, self.columna))
            return

        genC3D.agregarEspacio()
        auxReturn.etiquetaTrue = self.etiquetaTrue
        auxReturn.etiquetaFalse = self.etiquetaFalse
        return auxReturn

    def verifEtiquTrueFalse(self):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        if self.etiquetaTrue == '':
            self.etiquetaTrue = genC3D.nuevaEtiqueta()
        if self.etiquetaFalse == '':
            self.etiquetaFalse = genC3D.nuevaEtiqueta()
