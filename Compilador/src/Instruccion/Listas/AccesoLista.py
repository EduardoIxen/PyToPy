from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Abstract.Return import Return
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo


class AccesoLista(Instruccion):
    def __init__(self, id, accesInstr, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.accesInstr = accesInstr

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.agregarComentario("********* INICIO DEL ACCESO A LA LISTA *********")
        genC3D.agregarEspacio()

        valor = entorno.getVariable(self.id)
        if valor is None:
            genC3D.setExcepcion(Excepcion("Semantico", f"La variable {self.id} no esta declarada", self.linea, self.columna))
            return

        lstAtributos = []
        lstValores = []
        tipoFinal = Tipo.INT
        tmpItm = genC3D.agregarTemp()  #temporal para almacenar el valor encontrado
        tmpPtr = genC3D.agregarTemp()   #guardar el puntero
        tmpIndex = genC3D.agregarTemp() #puntero de la lista encontrada

        tamanio = len(self.accesInstr)
        _tipo = valor.getTipo()
        for i in range(tamanio):
            if i == 0:
                etiquetaTrue = genC3D.nuevaEtiqueta()
                etiquetaFalse = genC3D.nuevaEtiqueta()
                etiquetaSalida = genC3D.nuevaEtiqueta()

                valorElemento = self.accesInstr[i].compilar(entorno)   #compilo cada elemento de la lista
                tipoFinal = _tipo.valor
                genC3D.agregarComentario("ALMACENAR POSICION A ACCEDER")
                genC3D.agregarEspacio()
                genC3D.agregarExpresion(tmpPtr, valorElemento.getValor(), '', '')  #se almacena la posicion a acceder

                posicionTemporal = valor.posicion
                if not valor.esGlobal:
                    posicionTemporal = genC3D.agregarTemp()
                    genC3D.liberarTemp(posicionTemporal)
                    genC3D.agregarExpresion(posicionTemporal, 'P', valor.posicion, "+")

                genC3D.agregarComentario("OBTENER POSICION LISTA EN EL HEAP")
                genC3D.agregarEspacio()
                genC3D.getStack(tmpIndex, posicionTemporal)             #se recupera la lista
                genC3D.agregarComentario("ALMACENAR EL TAMAÑO")
                genC3D.agregarEspacio()
                genC3D.getHeap(tmpItm, tmpIndex)                        #obtener el tamaño

                genC3D.agregarComentario("VERIFICAR SI ESTA DENTRO DE LOS INDICES")
                genC3D.agregarEspacio()
                genC3D.agregarIf(tmpPtr, '1', '<', etiquetaTrue)
                genC3D.agregarIf(tmpPtr, tmpItm, '>', etiquetaTrue)
                genC3D.agregarGoto(etiquetaFalse)
                genC3D.agregarEtiqueta(etiquetaTrue)
                genC3D.imprimirBoundsError()
                genC3D.agregarExpresion(tmpItm, '0', '', '')
                genC3D.agregarGoto(etiquetaSalida)
                genC3D.agregarEtiqueta(etiquetaFalse)

                genC3D.agregarComentario("SUMO POSICION INICIO + INDICE = posicion del item")
                genC3D.agregarEspacio()
                genC3D.agregarExpresion(tmpIndex, tmpIndex, tmpPtr, '+')
                genC3D.agregarComentario("RECUPERO EL ITEM Y LO GUARDO EN UN TEMPORAL")
                genC3D.agregarEspacio()
                genC3D.getHeap(tmpItm, tmpIndex)
                genC3D.agregarEtiqueta(etiquetaSalida)
            else:
                tipoFinal = _tipo
                etiquetaTrue = genC3D.nuevaEtiqueta()
                etiquetaFalse = genC3D.nuevaEtiqueta()
                etiquetaSalida = genC3D.nuevaEtiqueta()

                valorElemento = self.accesInstr[i].compilar(entorno)        #compilo cada elemento del arreglo
                genC3D.agregarExpresion(tmpPtr, valorElemento.getValor(), '', '')
                genC3D.agregarExpresion(tmpIndex, tmpItm, '', '')
                genC3D.getHeap(tmpItm, tmpItm)

                #verificar BOUNDS ERROR
                genC3D.agregarIf(tmpPtr, '1', '<', etiquetaTrue)
                genC3D.agregarIf(tmpPtr, tmpItm, '>', etiquetaTrue)
                genC3D.agregarGoto(etiquetaFalse)
                genC3D.agregarEtiqueta(etiquetaTrue)
                genC3D.imprimirBoundsError()
                genC3D.agregarExpresion(tmpItm, '0', '', '')
                genC3D.agregarGoto(etiquetaSalida)
                genC3D.agregarEtiqueta(etiquetaFalse)           #si llega aca esta dentro de los limites
                genC3D.agregarComentario("--------------------------------------")
                genC3D.agregarExpresion(tmpIndex, tmpIndex, tmpPtr, '+')
                genC3D.getHeap(tmpItm, tmpIndex)
                genC3D.agregarComentario("--------------------------------------")
                genC3D.agregarEtiqueta(etiquetaSalida)

        genC3D.agregarComentario("FIN DE ACCESO A LA LISTA")
        genC3D.agregarEspacio()
        auxReturn = Return(tmpItm, tipoFinal, True)
        auxReturn.setAtributos(lstAtributos)
        auxReturn.setValores(lstValores)
        return auxReturn
