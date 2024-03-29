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
        genC3D.agregarComentario("***************** INICIO FOR *****************")
        genC3D.agregarEspacio()
        valor = self.expresion.compilar(entorno)

        temp = genC3D.agregarTemp()
        genC3D.liberarTemp(temp)

        if valor.getTipo() == Tipo.RANGE:
            genC3D.agregarEspacio()
            var = nuevoEntorno.setVariable(self.id, Tipo.INT, True)     #agrego la variable del range "i" a la TS
            genC3D.liberarTemp(valor.getValor())

            etiquetaContinue = genC3D.nuevaEtiqueta()                   #etiq conti = evaluar la condicion
            etiquetaBreak = genC3D.nuevaEtiqueta()                      #etiq break = falsa de la condicion

            nuevoEntorno.etiquetaContinue = etiquetaContinue
            nuevoEntorno.etiquetaBreak = etiquetaBreak

            tempI = genC3D.agregarTemp()
            finTemp = genC3D.agregarTemp()
            genC3D.liberarTemp(finTemp)
            genC3D.agregarComentario("RECUPERANDO VARIABLES DE CONTROL DE RANGO")
            genC3D.agregarEspacio()
            genC3D.getHeap(tempI, valor.getValor())     #recuperando el inicio
            genC3D.agregarExpresion(valor.getValor(), valor.getValor(), '1', '+')  #aumentamos en 1 para llegar al end
            genC3D.getHeap(finTemp, valor.getValor())

            genC3D.agregarEtiqueta(etiquetaContinue)    #salto al inicio de nuevo

            genC3D.agregarExpresion(temp, 'P', var.posicion, '+')
            genC3D.agregarComentario("ACTUALIZANDO VAL VARIABLE")
            genC3D.agregarEspacio()
            genC3D.setStack(temp, tempI)            #para cambiar el valor del ID ingresado
            genC3D.agregarComentario("EVALUANDO RANGO")
            genC3D.agregarEspacio()
            genC3D.agregarIf(tempI, finTemp, '>', etiquetaBreak)
            genC3D.agregarExpresion(tempI, tempI, '1', '+')       # i = i + 1

            for instr in self.instrucciones:
                instr.compilar(nuevoEntorno)

            genC3D.agregarGoto(etiquetaContinue)
            genC3D.agregarEtiqueta(etiquetaBreak)
            genC3D.agregarEspacio()

        elif valor.getTipo() == Tipo.STRING:
            var = nuevoEntorno.setVariable(self.id, Tipo.CHAR, True)
            genC3D.agregarComentario("GUARDO LA CADENA")
            genC3D.agregarEspacio()
            genC3D.agregarExpresion(temp, 'P', var.posicion, '+')
            genC3D.setStack(temp, valor.getValor())

            etiquetaContinue = genC3D.nuevaEtiqueta()
            etiquetaBreak = genC3D.nuevaEtiqueta()

            nuevoEntorno.etiquetaContinue = etiquetaContinue
            nuevoEntorno.etiquetaBreak = etiquetaBreak

            tempI = genC3D.agregarTemp()
            genC3D.agregarComentario("OBTENGO LA POSICION DEL STRING")
            genC3D.agregarEspacio()
            genC3D.agregarExpresion(temp, 'P', var.posicion, '+')
            genC3D.getStack(tempI, temp)
            genC3D.agregarComentario("INICIO DEL CICLO")
            genC3D.agregarEspacio()
            genC3D.agregarEtiqueta(etiquetaContinue)        #para volver al inicio del for
            hTemp = genC3D.agregarTemp()
            genC3D.getHeap(hTemp, tempI)                    #para encontrar el -1 del fin de la cadena
            genC3D.setStack(temp, tempI)                    #almacenamos el nuevo valor
            genC3D.agregarComentario("ACTUALIZAR POSICION DEL STRING")
            genC3D.agregarEspacio()
            genC3D.agregarExpresion(tempI, tempI, '1', '+') #incrementamos el index
            genC3D.agregarComentario("EVALUAR CONDICION")
            genC3D.agregarEspacio()
            genC3D.agregarIf(hTemp, '-1', '==', etiquetaBreak)

            genC3D.agregarComentario("instrucciones")
            genC3D.agregarEspacio()
            for instr in self.instrucciones:
                instr.compilar(nuevoEntorno)

            genC3D.agregarGoto(etiquetaContinue)
            genC3D.agregarEtiqueta(etiquetaBreak)

        else: #llegó un arreglo
            tipoVal = valor.getTipo()
            tipoFinal = None
            #if valor.getTipo() == Tipo.LIST: #TipoLista
            if isinstance(valor.getTipo(), TipoLista) or valor.getTipo() == Tipo.LIST:
                if valor.getTipo() == Tipo.LIST:
                    tipoFinal = valor.getAtributos()[0]
                else:
                    while tipoVal.valor is not None:
                        tipoFinal = tipoVal.valor         #ver si no da error
                        if type(tipoFinal) is not TipoLista: break
                        tipoVal = tipoVal.valor

                #if type(valor.getTipo()) == TipoLista:
                #    tipoFinal = valor.getTipo()
                genC3D.agregarEspacio()
                var = nuevoEntorno.setVariable(self.id, tipoFinal, True)
                genC3D.liberarTemp(valor.getValor())
                etiquetaContinue = genC3D.nuevaEtiqueta()
                etiquetaBreak = genC3D.nuevaEtiqueta()
                nuevoEntorno.etiquetaContinue = etiquetaContinue
                nuevoEntorno.etiquetaBreak = etiquetaBreak

                tempFin = genC3D.agregarTemp()
                genC3D.liberarTemp(tempFin)
                temp2 = genC3D.agregarTemp()
                genC3D.liberarTemp(temp2)
                contTemp = genC3D.agregarTemp()
                genC3D.liberarTemp(contTemp)
                tempI = genC3D.agregarTemp()
                genC3D.liberarTemp(tempI)

                genC3D.agregarComentario("RECUPERAR TAMAÑO LISTA")
                genC3D.agregarEspacio()
                genC3D.getHeap(tempFin, valor.getValor())       #recuperar el tamaño de la lista
                genC3D.agregarExpresion(temp2, valor.getValor(), '1', '+')

                genC3D.agregarExpresion(contTemp, '1', '', '')
                genC3D.agregarComentario("COMENZANDO LAS ITERACIONES")
                genC3D.agregarEspacio()
                genC3D.agregarEtiqueta(etiquetaContinue)        #comenzando las iteraciones
                genC3D.agregarComentario("OBTENER EL ITEM")
                genC3D.agregarEspacio()
                genC3D.getHeap(tempI, temp2)                    #obteniendo item

                genC3D.agregarExpresion(temp, 'P', var.posicion, '+')
                genC3D.agregarComentario("MODIFICANDO VALOR VARIABLE = ITEM")
                genC3D.agregarEspacio()
                genC3D.setStack(temp, tempI)                    #modificando el val de la variable
                genC3D.agregarComentario("EVALUAR CONDICION")
                genC3D.agregarEspacio()
                genC3D.agregarIf(contTemp, tempFin, '>', etiquetaBreak)         #evaluo la condicion
                genC3D.agregarComentario("SIGUIENTE ELEMENTO DEL HEAP")
                genC3D.agregarEspacio()
                genC3D.agregarExpresion(temp2, temp2, '1', '+')     #i = i + 1
                genC3D.agregarComentario("CONTADOR DE ELEMENTOS")
                genC3D.agregarEspacio()
                genC3D.agregarExpresion(contTemp, contTemp, '1', '+')   #i = i+1

                genC3D.agregarComentario("instrucciones")
                genC3D.agregarEspacio()
                for instr in self.instrucciones:
                    instr.compilar(nuevoEntorno)
                genC3D.agregarGoto(etiquetaContinue)        #retornar al inicio
                genC3D.agregarEtiqueta(etiquetaBreak)       #fin del for

                genC3D.agregarEspacio()
            else:
                genC3D.setExcepcion(Excepcion("Semantico", "La expresion del for debe ser un STRING, una LISTA o un RANGE", self.linea, self.columna))
                return

        genC3D.agregarComentario("***************** FIN FOR *****************")
        genC3D.agregarEspacio()
        genC3D.agregarEspacio()



