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
            elif simbolo.getTipo() == Tipo.LIST:
                #codigo para imprimir listas
                pass
            else:
                genC3D.agregarPrint("f", simbolo.getValor())

        genC3D.nuevaLinea()




    def cadenaRecibida(self, genC3D, valor, entorno):
        genC3D.agregarComentario("INICIO IMPRIMIR STRING")
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
