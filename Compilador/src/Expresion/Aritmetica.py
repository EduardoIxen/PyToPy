from src.Abstract.Expresion import Expresion
from src.Ast.Tipo import TipoOperacion
from src.Ast.TablaTipo import TablaTipo
from src.Ast.Tipo import Tipo
from src.Abstract.Return import Return
from src.Excepcion.Excepcion import Excepcion
from src.Ast.GeneradorC3D import GeneradorC3D

class Aritmetica(Expresion):
    def __init__(self, izquierda, derecha, tipoOperacion, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.izquierda = izquierda
        self.derecha = derecha
        self.tipoOperacion = tipoOperacion

    def compilar(self, entorno):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()

        izq = self.izquierda.compilar(entorno)
        der = self.derecha.compilar(entorno)

        if (izq.getTipo() == Tipo.STRING and der.getTipo() == Tipo.INT and
            self.tipoOperacion == TipoOperacion.MULTIPLICACION):     #"hola"*3="holaholahola"
            genC3D.nativaRepetirStr()
            return self.repetirCadena(entorno, izq.getValor(), der.getValor())
        if (izq.getTipo() == Tipo.STRING and der.getTipo() == Tipo.STRING and
            self.tipoOperacion == TipoOperacion.SUMA):              #"cadena"+"cadena"
            genC3D.nativaConcatenar()
            return self.concatenarCadena(entorno, izq.getValor(), der.getValor())



    def repetirCadena(self, entorno, cadena, multiplicidad):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()
        tmpParam = genC3D.agregarTemp()
        genC3D.agregarExpresion(tmpParam, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(tmpParam, tmpParam, '1', '+')
        genC3D.setStack(tmpParam, cadena)

        tmpMultipl = genC3D.agregarTemp()
        genC3D.agregarExpresion(tmpMultipl, tmpParam, '1', '+')
        genC3D.setStack(tmpMultipl, multiplicidad)

        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('repetirString')
        tempAux = genC3D.agregarTemp()
        genC3D.getStack(tempAux, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())
        return Return(tempAux, Tipo.STRING, True)

    def concatenarCadena(self, entorno, cadena1, cadena2):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        cadTemp = genC3D.agregarTemp()      #cadena 1
        genC3D.agregarExpresion(cadTemp, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(cadTemp, cadTemp, '1', '+')
        genC3D.setStack(cadTemp, cadena1)

        cad2Temp = genC3D.agregarTemp()     #cadena 2
        genC3D.agregarExpresion(cad2Temp, cadTemp, '1', '+')
        genC3D.setStack(cad2Temp, cadena2)

        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('concatenarCadena')

        tmp = genC3D.agregarTemp()
        genC3D.getStack(tmp, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())
        return Return(tmp, Tipo.STRING, True)
