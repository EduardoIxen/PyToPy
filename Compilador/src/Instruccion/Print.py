from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Ast.Tipo import Tipo

class Print(Instruccion):
    def __init__(self, expresion, linea, columna):
        super().__init__(linea, columna)
        self.expresion = expresion
        self.etiquetaTrue = ''
        self.etiquetaFalse = ''

    def compilar(self, entorno):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()

        for expre in self.expresion:
            simbolo = expre.compilar(entorno) # obtengo lo un objeto Return
            if simbolo is None:
                return
            if simbolo.getTipo() == Tipo.BOOLEAN:
                etiqTemp = genC3D.nuevaEtiqueta()
                genC3D.agregarEtiqueta(simbolo.etiquetaTrue)
                genC3D.imprimirTrue()
                genC3D.agregarGoto(etiqTemp)

                genC3D.agregarEtiqueta(simbolo.etiquetaFalse)
                genC3D.imprimirFalse()
                genC3D.agregarEtiqueta(etiqTemp)

            elif simbolo.getTipo() == Tipo.STRING:
                self.cadenaRecibida(genC3D, simbolo.getValor(), entorno)
            elif simbolo.getTipo() == Tipo.INT:
                genC3D.agregarPrint('d', simbolo.getValor())
            elif simbolo.getTipo() == Tipo.CHAR:
                temp = genC3D.agregarTemp()
                genC3D.getHeap(temp, simbolo.getValor())
                genC3D.agregarPrint("c", temp)
            elif simbolo.getTipo() == Tipo.LIST:
                temp = genC3D.agregarTemp()
                temp2 = genC3D.agregarTemp()
                genC3D.agregarExpresion(temp2, simbolo.getValor(), '1', '+')   #almacanar la posicion del arreglo
                genC3D.agregarPrint("c", '91')                                  # 91 -> [
                for atrib in range(len(simbolo.getAtributos())):
                    genC3D.getHeap(temp, temp2)
                    if simbolo.getAtributos()[atrib] == Tipo.INT:
                        genC3D.agregarPrint("d", temp)
                    elif simbolo.getAtributos()[atrib] == Tipo.STRING:
                        genC3D.agregarPrint("c", '34')                          #34 -> "
                        self.cadenaRecibida(genC3D, temp, entorno)
                        genC3D.agregarPrint("c", 34)                            #34 -> "
                    elif simbolo.getAtributos()[atrib] == Tipo.FLOAT:
                        genC3D.agregarPrint("f", temp)

                    elif simbolo.getAtributos()[atrib] == Tipo.LIST:
                        self.listaRecibida(temp, simbolo.getValores()[atrib], entorno)
                    if atrib != len(simbolo.getAtributos()) - 1:
                        genC3D.agregarPrint("c", 44)                            #44 -> ,
                    genC3D.agregarExpresion(temp2, temp2, 1, '+')
                genC3D.agregarPrint("c", 93)                                    #93 -> ]

            else:
                genC3D.agregarPrint("f", simbolo.getValor())

        genC3D.nuevaLinea()

    def cadenaRecibida(self, genC3D, valor, entorno):
        genC3D.agregarComentario("INICIO IMPRIMIR STRING")
        genC3D.agregarEspacio()
        genC3D.nativaPrint()
        tempParam = genC3D.agregarTemp()

        genC3D.agregarExpresion(tempParam, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(tempParam, tempParam, '1', '+')
        genC3D.setStack(tempParam, valor)

        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('nativa_print')

        tmp = genC3D.agregarTemp()
        genC3D.getStack(tmp, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())
        genC3D.agregarComentario('FIN IMPRIMIR STRING')
        genC3D.agregarEspacio()


    def listaRecibida(self, htemp, atributo, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        tmp = genC3D.agregarTemp()
        tmp2 = genC3D.agregarTemp()

        genC3D.agregarExpresion(tmp2, htemp, '1', '+')
        genC3D.agregarPrint("c", 91)                    #91 -> [
        for atrib in range(len(atributo.getAtributos())):
            genC3D.getHeap(tmp, tmp2)           #esto par recuperar cada item
            if atributo.getAtributos()[atrib] == Tipo.INT:
                genC3D.agregarPrint("d", tmp)
            elif atributo.getAtributos()[atrib] == Tipo.FLOAT:
                genC3D.agregarPrint("f", tmp)
            elif atributo.getAtributos()[atrib] == Tipo.STRING:
                genC3D.agregarPrint("c", 34)                    #34 -> "
                self.cadenaRecibida(genC3D, tmp, entorno)
                genC3D.agregarPrint("c", 34)                    #fin de cadena->"
            elif atributo.getAtributos()[atrib] == Tipo.LIST:
                self.listaRecibida(tmp, atributo.getValores()[atrib], [atrib], entorno)
            if atrib != len(atributo.getAtributos()) -1:
                genC3D.agregarPrint("c", '44')                  #44 -> ,
            genC3D.agregarExpresion(tmp2, tmp2, 1, '+')         #probar si no da error por ''
        genC3D.agregarPrint("c", 93)                            #93 -> ]
