from src.Abstract.Expresion import Expresion
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Excepcion.Excepcion import Excepcion
from src.Abstract.Return import Return
from src.Ast.Tipo import Tipo


class Identificador(Expresion):
    def __init__(self, id, tipo, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.tipo = tipo

    def compilar(self, entorno):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()
        varId = entorno.getVariable(self.id)

        if varId is None:
            genC3D.setExcepcion(Excepcion("Semantico", f"La variable {self.id} no existe", self.linea, self.columna))
            return
        temp = genC3D.agregarTemp() #temp para almacenar la variable
        posTemp = varId.posicion    #se obtiene la posicion de la variable

        if not varId.esGlobal:
            posTemp = genC3D.agregarTemp()
            genC3D.liberarTemp(posTemp)
            genC3D.agregarExpresion(posTemp, 'P', varId.posicion, "+")

        genC3D.getStack(temp, posTemp)

        if varId.tipo != Tipo.BOOLEAN:
            ret = Return(temp, varId.tipo, True)
            ret.setTipoAux(varId.getTipoAux())
            ret.setAtributos(varId.getAtributos())
            ret.setValores(varId.getValores())
            genC3D.agregarEspacio()
            return ret

        if self.etiquetaTrue == '':
            self.etiquetaTrue = genC3D.nuevaEtiqueta()
        if self.etiquetaFalse == '':
            self.etiquetaFalse = genC3D.nuevaEtiqueta()

        genC3D.liberarTemp(temp)
        genC3D.agregarIf(temp, '1', '==', self.etiquetaTrue)
        genC3D.agregarGoto(self.etiquetaFalse)
        genC3D.agregarEspacio()

        ret = Return(None, Tipo.BOOLEAN, False)
        ret.etiquetaTrue = self.etiquetaTrue
        ret.etiquetaFalse = self.etiquetaFalse
        return ret

    def getId(self):
        return self.id