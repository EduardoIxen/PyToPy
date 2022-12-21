from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo
from src.Ast.Entorno import Entorno
from src.Instruccion.Listas.TipoLista import TipoLista


class ForInstr(Instruccion):
    def __init__(self, id, expresion, instrucciones, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.expresion = expresion
        self.instrucciones = instrucciones

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        nuevoEntorno = Entorno(entorno)
        genC3D.agregarComentario("INICIO FOR")
        valor = self.expresion.compilar(entorno)

        temp = genC3D.agregarTemp()
        genC3D.liberarTemp(temp)

        if valor.getTipo() == Tipo.RANGE:
            genC3D.agregarEspacio()
            var = nuevoEntorno.setVariable(self.id, Tipo.INT, True)
            genC3D.liberarTemp(valor.getValor())

            etiquetaContinue = genC3D.nuevaEtiqueta()
            etiquetaBreak = genC3D.nuevaEtiqueta()

            nuevoEntorno.etiquetaContinue = etiquetaContinue
            nuevoEntorno.etiquetaBreak = etiquetaBreak

            tempI = genC3D.agregarTemp()
            finTemp = genC3D.agregarTemp()
            genC3D.liberarTemp(finTemp)

            genC3D.getHeap(tempI, valor.getValor())     #recuperando el inicio
            genC3D.agregarExpresion(valor.getValor(), valor.getValor(), '1', '+')  #aumentamos en 1 para llegar al end
            genC3D.getHeap(finTemp, valor.getValor())

            genC3D.agregarEtiqueta(etiquetaContinue)    #salto al inicio de nuevo

            genC3D.agregarExpresion(temp, 'P', var.posicion, '+')
            genC3D.setStack(temp, tempI)            #para cambiar el valor del ID ingresado
            genC3D.agregarIf(tempI, finTemp, '>', etiquetaBreak)
            genC3D.agregarExpresion(tempI, tempI, '1', '+')       # i = i + 1

            for instr in self.instrucciones:
                instr.compilar(nuevoEntorno)

            genC3D.agregarGoto(etiquetaContinue)
            genC3D.agregarEtiqueta(etiquetaBreak)
            genC3D.agregarEspacio()

        elif valor.getTipo() == Tipo.STRING:
            var = nuevoEntorno.setVariable(self.id, Tipo.CHAR, True)
            genC3D.agregarExpresion(temp, 'P', var.posicion, '+')
            genC3D.setStack(temp, valor.getValor())

            etiquetaContinue = genC3D.nuevaEtiqueta()
            etiquetaBreak = genC3D.nuevaEtiqueta()

            nuevoEntorno.etiquetaContinue = etiquetaContinue
            nuevoEntorno.etiquetaBreak = etiquetaBreak

            tempI = genC3D.agregarTemp()
            genC3D.agregarExpresion(temp, 'P', var.posicion, '+')
            genC3D.getStack(tempI, temp)

            genC3D.agregarEtiqueta(etiquetaContinue)        #para volver al inicio del for
            hTemp = genC3D.agregarTemp()
            genC3D.getHeap(hTemp, tempI)                    #para encontrar el -1 del fin de la cadena
            genC3D.setStack(temp, tempI)                    #almacenamos el nuevo valor
            genC3D.agregarExpresion(tempI, tempI, '1', '+') #incrementamos el index
            genC3D.agregarIf(hTemp, '-1', '==', etiquetaBreak)

            for instr in self.instrucciones:
                instr.compilar(nuevoEntorno)

            genC3D.agregarGoto(etiquetaContinue)
            genC3D.agregarEtiqueta(etiquetaBreak)

        else: #por si es un arreglo
            pass

        genC3D.agregarComentario("FIN FOR")
        genC3D.agregarEspacio()



