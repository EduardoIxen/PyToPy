from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Abstract.Return import Return
from src.Ast.Tipo import Tipo


class Lista(Instruccion):
    def __init__(self, lstExpresiones, linea, columna):
        super().__init__(linea, columna)
        self.lstExpresiones = lstExpresiones

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.agregarComentario("--------------INICIO DE LISTA--------------")
        genC3D.agregarEspacio()
        hTemp = genC3D.agregarTemp()            #ptr para el heap
        h2Temp = genC3D.agregarTemp()           #cantidad de posiciones en la lista
        tam = len(self.lstExpresiones)
        genC3D.agregarComentario("OBTENGO EL VAL DE HEAP EN UNA TEMP")
        genC3D.agregarEspacio()
        genC3D.agregarExpresion(hTemp, 'H', '', '')       #almacenando la posicion de la lista
        genC3D.agregarExpresion(h2Temp, hTemp, '','')     #controla las posiciones de cada valor de la lista
        genC3D.agregarComentario("RESERVO EL ESPACIO PARA LOS ELEMENTOS")
        genC3D.agregarEspacio()
        genC3D.agregarExpresion('H', 'H', tam + 1, '+')   #a cada valor del arreglo se le reservan posiciones en el heap, sumando 1 para guardar la pos de la lista en la primera posicion

        genC3D.agregarComentario("EN EL 1ER ESPACIO AGREGO EL TAMAÑO DEL ARREGLO")
        genC3D.agregarEspacio()
        genC3D.setHeap(h2Temp, tam)                     #almacenando el tamaño del arreglo
        genC3D.agregarExpresion(h2Temp, h2Temp, '1', '+')

        tiposAux = []
        valoresAux = []
        contador = 1

        for exp in self.lstExpresiones:
            valor = exp.compilar(entorno)

            genC3D.setHeap(h2Temp, valor.getValor())  #guardar el valor de cada elemento de la lista en el heap
            if tam != contador:
                genC3D.agregarExpresion(h2Temp, h2Temp, '1', '+')

            contador += 1
            tiposAux.append(valor.getTipo())
            valoresAux.append(valor)

        retornar = Return(hTemp, Tipo.LIST, True)
        retornar.setAtributos(tiposAux)
        retornar.setValores(valoresAux)
        genC3D.agregarComentario("--------------- FIN LISTA ---------------")
        genC3D.agregarEspacio()
        genC3D.agregarEspacio()
        return retornar

#verificado