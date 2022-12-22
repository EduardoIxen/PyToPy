from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo
from src.Instruccion.Listas.TipoLista import TipoLista

class Declaracion(Instruccion):
    def __init__(self, id, expresion, tipo, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.expresion = expresion
        self.tipo = tipo

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        if isinstance(self.id, str):  #se obtiene un id
            if isinstance(self.expresion, str):
                valor = self.expresion.compilar(entorno)
            else:
                if self.tipo is None:
                    valor = self.expresion.compilar(entorno)
                    if valor is None:
                        return

                else:
                    valor = self.expresion.compilar(entorno)
                    tipoVar = self.tipo

                    if isinstance(tipoVar, str):
                        tipoVar = entorno.getStruct(tipoVar).getTipo()

                    if valor.getTipo() == Tipo.STRUCT or valor.getTipo() == Tipo.MUTSTRUCT:
                        if self.tipo != valor.getTipoAux():
                            genC3D.setExcepcion(Excepcion("Semantico", "Tipo incorrecto en struct", self.linea, self.columna))
                            return
                    else:
                        if type(tipoVar) == TipoLista:
                            if tipoVar.tipo != valor.getTipo():
                                genC3D.setExcepcion(Excepcion("Semantico", "Tipo de datos incompatibles.", self.linea, self.columna))
                                return
                        else:
                            if tipoVar != valor.getTipo():
                                genC3D.setExcepcion(Excepcion("Semantico", "El tipo de la variable no es el mismo que el de la expresion", self.linea, self.columna))
                                return

            nuevaVariable = entorno.getVariable(self.id) #veo si la variable existe para obtener su posicion en el heap
            if nuevaVariable == None: #si no existe la creo
                if valor.getTipo() == Tipo.STRUCT or valor.getTipo() == Tipo.MUTSTRUCT:
                    nuevaVariable = entorno.setVariable(self.id, valor.getTipo(), True, valor.getTipoAux(), valor.getAtributos(), valor.getValores())
                elif valor.getTipo() == Tipo.LIST:
                    if type(self.tipo) == TipoLista:
                        tipoVar = self.tipo
                    else:
                        tipoVar = Tipo.LIST
                    nuevaVariable = entorno.setVariable(self.id, tipoVar, True, valor.getTipoAux(), valor.getAtributos(), valor.getValores())
                else:
                    nuevaVariable = entorno.setVariable(self.id, valor.getTipo(), False)
            else:
                #Se actualiza la variable por si el valor cambia y el tipo tambien
                nuevaVariable = entorno.actualizarVar(self.id, valor.getTipo())

            posicionTemp = nuevaVariable.posicion

            if not nuevaVariable.esGlobal:
                posicionTemp = genC3D.agregarTemp()
                genC3D.agregarExpresion(posicionTemp, 'P', nuevaVariable.posicion, "+")

            if valor.getTipo() == Tipo.BOOLEAN:
                etiquTemp = genC3D.nuevaEtiqueta()
                genC3D.agregarEtiqueta(valor.etiquetaTrue)
                genC3D.setStack(posicionTemp, "1")
                genC3D.agregarGoto(etiquTemp)
                genC3D.agregarEtiqueta(valor.etiquetaFalse)
                genC3D.setStack(posicionTemp, "0")
                genC3D.agregarEtiqueta(etiquTemp)
            else:
                genC3D.setStack(posicionTemp, valor.valor)
            genC3D.agregarEspacio()
        else:  #asignacion para structs
            var = entorno.getVariable(self.id[0])

            if var is None:
                genC3D.setExcepcion(Excepcion("Semantico", f"{self.id}, no esta definido", self.linea, self.columna))
                return

            if var.getTipo() == Tipo.STRUCT or var.getTipo() == Tipo.MUTSTRUCT:
                genC3D.agregarComentario("INICIO DE STRUCT")
                genC3D.agregarEspacio()

                valor = self.expresion.compilar(entorno)
                struct = entorno.getStruct(var.getTipoAux())

                hTemp = genC3D.agregarTemp()
                for nivelStruct in range(len(self.id) - 1):
                    nivelStruct += 1        #posicion 0 es el id
                    contador = 0
                    for atrib in struct.atributos:
                        if atrib['id'] == self.id[nivelStruct]:
                            genC3D.getStack(hTemp, var.posicion)
                            genC3D.agregarExpresion(hTemp, hTemp, contador, '+')
                            genC3D.setHeap(hTemp, valor.getValor())
                            break
                        contador += 1
                genC3D.agregarComentario("FIN STRUCT")
            else:   #es una lista
                self.declarar_lista(var, entorno, self.id[1])

    def declarar_lista(self, valor, entorno, acceso):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        tempId = genC3D.agregarTemp()
        genC3D.agregarExpresion(tempId, 'P',valor.posicion, '+')
        genC3D.getStack(tempId, tempId)

        tamanio = len(acceso)
        itemTemp = genC3D.agregarTemp() #almacena el puntero de la posicion
        anterior = 0
        for i in range(tamanio):
            if i == 0:
                genC3D.agregarComentario("INICIO ACCESO A LISTA")
                genC3D.agregarEspacio()
                etiquTrue = genC3D.nuevaEtiqueta()
                etiquFalse = genC3D.nuevaEtiqueta()
                etiquSalida = genC3D.nuevaEtiqueta()

                accesoTemp = genC3D.agregarTemp()    #index al cual acceder
                temp = genC3D.agregarTemp()

                index = acceso[i].compilar(entorno)     #compilar lo obtenido
                genC3D.agregarExpresion(accesoTemp, index.getValor(), '', '')
                genC3D.agregarExpresion(temp, tempId, '', '')
                genC3D.getHeap(itemTemp, temp)

                #index out of range
                genC3D.agregarIf(accesoTemp, '1', '<', etiquTrue)  #limite inferior
                genC3D.agregarIf(accesoTemp, itemTemp, '>', etiquTrue)  #limite superior
                genC3D.agregarGoto(etiquFalse)
                genC3D.agregarEtiqueta(etiquTrue)
                genC3D.imprimirBoundsError()
                genC3D.agregarExpresion(itemTemp, '0', '', '')  #asegurando un resultado 0
                genC3D.agregarGoto(etiquSalida)
                genC3D.agregarEtiqueta(etiquFalse)          #saltar cuando esta dentro de los limites

                genC3D.agregarExpresion(itemTemp, temp, accesoTemp, '+')
                val = self.expresion.compilar(entorno)
                if i == tamanio - 1:
                    genC3D.setHeap(itemTemp, val.getValor())        #se almacena el nuevo valor
                else:
                    genC3D.getHeap(itemTemp, itemTemp)              #se devuelve la posicion del arreglo
                genC3D.agregarEtiqueta(etiquSalida)
                genC3D.agregarComentario("FIN ACCESO A LISTA")
                genC3D.agregarEspacio()
            else:
                genC3D.agregarComentario("INICIO ACCESO A LISTA")
                genC3D.agregarEspacio()
                etiquTrue = genC3D.nuevaEtiqueta()
                etiquFalse = genC3D.nuevaEtiqueta()
                etiquSalida = genC3D.nuevaEtiqueta()

                accesoTemp = genC3D.agregarTemp()  # index al cual acceder
                temp = genC3D.agregarTemp()

                acceso = acceso[i].compilar(entorno)  # compilar lo obtenido

                genC3D.agregarExpresion(accesoTemp, acceso.getValor(), '', '')
                genC3D.agregarExpresion(temp, itemTemp, '', '')
                genC3D.getHeap(itemTemp, temp)

                # index out of range
                genC3D.agregarIf(accesoTemp, '1', '<', etiquTrue)  # limite inferior
                genC3D.agregarIf(accesoTemp, itemTemp, '>', etiquTrue)  # limite superior
                genC3D.agregarGoto(etiquFalse)
                genC3D.agregarEtiqueta(etiquTrue)
                genC3D.imprimirBoundsError()
                genC3D.agregarExpresion(itemTemp, '0', '', '')  # asegurando un resultado 0
                genC3D.agregarGoto(etiquSalida)
                genC3D.agregarEtiqueta(etiquFalse)  # saltar cuando esta dentro de los limites

                genC3D.agregarExpresion(itemTemp, temp, accesoTemp, '+')
                val = self.expresion.compilar(entorno)
                if i == tamanio - 1:
                    genC3D.setHeap(itemTemp, val.getValor())  # se almacena el nuevo valor
                else:
                    genC3D.getHeap(itemTemp, itemTemp)  # se devuelve la posicion del arreglo
                genC3D.agregarEtiqueta(etiquSalida)
                genC3D.agregarComentario("FIN ACCESO A LISTA")
                genC3D.agregarEspacio()


#revisado