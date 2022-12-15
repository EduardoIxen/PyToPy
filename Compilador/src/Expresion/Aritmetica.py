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
        if self.tipoOperacion == TipoOperacion.POTENCIA:
            genC3D.nativaPotencia()
            return self.genPotencia(entorno, izq.getValor(), der.getValor(), izq, der)

        obtenerTipo = TablaTipo()
        tipoResultado = obtenerTipo.obtenerTipo(izq.getTipo(), der.getTipo())

        if tipoResultado == Tipo.ERROR:
            genC3D.setExcepcion(Excepcion("Semantico", f'La operacion ingresada no se puede realizar {izq.getTipo()} {self.tipoOperacion} {der.getTipo()}'), self.linea, self.columna)
            return

        tmp = genC3D.agregarTemp()
        operacion = ''
        if self.tipoOperacion == TipoOperacion.SUMA:
            operacion = '+'
        elif self.tipoOperacion == TipoOperacion.RESTA:
            operacion = '-'
        elif self.tipoOperacion == TipoOperacion.MULTIPLICACION:
            operacion = '*'
        elif self.tipoOperacion == TipoOperacion.DIVISION:
            operacion = '/'
            tipoResultado = Tipo.FLOAT
            izq.valor = float(izq.getValor())
        elif self.tipoOperacion == TipoOperacion.MODULO:
            operacion = '%'

        genC3D.liberarTemp(izq.getValor())
        genC3D.liberarTemp(der.getValor())
        if operacion == '%' or operacion == '/':
            etiquTrue = genC3D.nuevaEtiqueta()
            etiquSalida = genC3D.nuevaEtiqueta()
            genC3D.agregarIf(der.getValor(), '0', '!=', etiquTrue)  #COMPARACION DINAMIVA DIVIDIDO 0
            genC3D.imprimirMathError()
            genC3D.agregarExpresion(tmp, '0', '','')
            genC3D.agregarGoto(etiquSalida)
            genC3D.agregarEtiqueta(etiquTrue)

            if operacion == '%':
                genC3D.math = True
                genC3D.agregarExponModulo(tmp, izq.getValor(), der.getValor())
            else:
                if der.getValor() == '0':
                    der.valor = '0.00001'
                genC3D.agregarExpresion(tmp, izq.getValor(), der.getValor(), operacion)
            genC3D.agregarEtiqueta(etiquSalida)
        else:
            genC3D.agregarExpresion(tmp, izq.getValor(), der.getValor(), operacion)

        return Return(tmp, tipoResultado, True)





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

    def genPotencia(self, entorno, numero, exponente, izq, der):
        inst = GeneradorC3D()
        genC3D = inst.getInstance()
        #numero
        numTemp = genC3D.agregarTemp()
        genC3D.agregarExpresion(numTemp, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(numTemp, numTemp, '1', '+')
        genC3D.setStack(numTemp, numero)
        #exponente
        expTemp = genC3D.agregarTemp()
        genC3D.agregarExpresion(expTemp, numTemp, '1', '+')
        genC3D.setStack(expTemp, exponente)

        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('natPotencia')
        temp = genC3D.agregarTemp()
        genC3D.getStack(temp, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())

        obtenerTipo = TablaTipo()
        tipoResultado = obtenerTipo.obtenerTipo(izq.getTipo(), der.getTipo())

        return Return(temp, tipoResultado, True)
