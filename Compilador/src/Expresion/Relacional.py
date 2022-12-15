from src.Abstract.Expresion import Expresion
from src.Abstract.Return import Return
from src.Ast.TablaTipo import Tipo
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Ast.Tipo import TipoOperacion

class Relacional(Expresion):
    def __init__(self, izq, der, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.izq = izq
        self.der = der
        self.tipo = tipo

    def compilar(self, entorno):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()

        opIzq = self.izq.compilar(entorno)
        opDer = None

        retResult = Return(None, Tipo.BOOLEAN, False)

        if opIzq.getTipo() != Tipo.BOOLEAN:
            opDer = self.der.compilar(entorno)
            if ((opIzq.getTipo() == Tipo.INT or opIzq.getTipo() == Tipo.FLOAT) and
                (opDer.getTipo() == Tipo.INT or opDer.getTipo() == Tipo.FLOAT) or opIzq.getTipo() == Tipo.ANY):
                self.verifEtiqTrueFalse()
                genC3D.liberarTemp(opIzq.getValor())
                genC3D.liberarTemp(opDer.getValor())
                genC3D.agregarIf(opIzq.getValor(), opDer.getValor(), self.obtenerOpRel(), self.etiquetaTrue)
                genC3D.agregarGoto(self.etiquetaFalse)
            elif (opIzq.getTipo() == Tipo.STRING and opDer.getTipo() == Tipo.STRING):
                self.verifEtiqTrueFalse()
                genC3D.nativaCompararCad()
                genC3D.liberarTemp(opIzq.getValor())
                genC3D.liberarTemp(opDer.getValor())
                genC3D.agregarIf(self.compararCadena(entorno, opIzq.getValor(), opDer.getValor()), '1', '==', self.etiquetaTrue)
                genC3D.agregarGoto(self.etiquetaFalse)
        else:
            derGoto = genC3D.nuevaEtiqueta()
            tmpIzq = genC3D.agregarTemp()
            genC3D.liberarTemp(tmpIzq)

            genC3D.agregarEtiqueta(opIzq.etiquetaTrue)
            genC3D.agregarExpresion(tmpIzq, '1', '', '')
            genC3D.agregarGoto(derGoto)

            genC3D.agregarEtiqueta(opIzq.etiquetaFalse)
            genC3D.agregarExpresion(tmpIzq, '0', '', '')
            genC3D.agregarEtiqueta(derGoto)

            opDer = self.der.compilar(entorno)
            if opDer.tipo != Tipo.BOOLEAN:
                return

            gotoFin = genC3D.nuevaEtiqueta()
            tmpDer = genC3D.agregarTemp()
            genC3D.liberarTemp(tmpDer)
            genC3D.agregarEtiqueta(opDer.etiquetaTrue)

            genC3D.agregarExpresion(tmpDer, '1', '', '')
            genC3D.agregarGoto(gotoFin)
            genC3D.agregarEtiqueta(opDer.etiquetaFalse)
            genC3D.agregarExpresion(tmpDer, '0', '', '')
            genC3D.agregarEtiqueta(gotoFin)

            self.verifEtiqTrueFalse()
            genC3D.agregarIf(tmpIzq, tmpDer, self.obtenerOpRel(), self.etiquetaTrue)
            genC3D.agregarGoto(self.etiquetaFalse)

        genC3D.agregarEspacio()
        retResult.etiquetaTrue = self.etiquetaTrue
        retResult.etiquetaFalse = self.etiquetaFalse
        return retResult

    def verifEtiqTrueFalse(self):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()

        if self.etiquetaTrue == '':
            self.etiquetaTrue = genC3D.nuevaEtiqueta()
        if self.etiquetaFalse == '':
            self.etiquetaFalse = genC3D.nuevaEtiqueta()

    def obtenerOpRel(self):
        if self.tipo == TipoOperacion.MENOR:
            return '<'
        elif self.tipo == TipoOperacion.MAYOR:
            return '>'
        elif self.tipo == TipoOperacion.MENORIGUAL:
            return '<='
        elif self.tipo == TipoOperacion.MAYORIGUAL:
            return '>='
        elif self.tipo == TipoOperacion.IGUAL:
            return '=='
        elif self.tipo == TipoOperacion.DIFERENTE:
            return '!='

    def compararCadena(self, entorno, cad1, cad2):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()

        cad1Temp = genC3D.agregarTemp() #primera cadena (pasar param)
        genC3D.agregarExpresion(cad1Temp, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(cad1Temp, cad1Temp, '1', '+')
        #genC3D.getStack(cad1Temp, cad1)
        genC3D.setStack(cad1Temp, cad1)

        cad2Temp = genC3D.agregarTemp() #segunda cadena (pasar param)
        genC3D.agregarExpresion(cad2Temp, cad1Temp, '1', '+')
        genC3D.setStack(cad2Temp, cad2)

        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('natCompararCadena')
        tmp = genC3D.agregarTemp()
        genC3D.getStack(tmp, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())
        return tmp
