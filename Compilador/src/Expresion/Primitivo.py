from src.Abstract.Expresion import Expresion
from src.Abstract.Return import Return
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Ast.Tipo import Tipo

class Primitivo(Expresion):
    def __init__(self, valor, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.tipo = tipo

    def compilar(self, entorno):
        nuevaInstancia = GeneradorC3D()
        genC3D = nuevaInstancia.getInstance()

        if self.tipo == Tipo.INT or self.tipo == Tipo.FLOAT:
            return Return(str(self.valor), self.tipo, False)
        if self.tipo == Tipo.BOOLEAN:
            if self.etiquetaTrue == '':
                self.etiquetaTrue = genC3D.nuevaEtiqueta()
            if self.etiquetaFalse == '':
                self.etiquetaFalse = genC3D.nuevaEtiqueta()
            if self.valor:
                genC3D.agregarGoto(self.etiquetaTrue)
                genC3D.agregarComentario("goto a boolean verdadero")
                genC3D.agregarEspacio()
                genC3D.agregarGoto(self.etiquetaFalse)
            else:
                genC3D.agregarGoto(self.etiquetaFalse)
                genC3D.agregarComentario("goto a boolean falso")
                genC3D.agregarEspacio()
                genC3D.agregarGoto(self.etiquetaTrue)

            retornar = Return(str(self.valor), self.tipo, False)
            retornar.etiquetaFalse = self.etiquetaFalse
            retornar.etiquetaTrue = self.etiquetaTrue
            return retornar

        elif self.tipo == Tipo.STRING:
            nuevoTemp = genC3D.agregarTemp()
            genC3D.agregarExpresion(nuevoTemp, 'H', '', '')

            for caracter in str(self.valor):
                genC3D.setHeap('H', ord(caracter))      #ord convierte el caracter a numero
                genC3D.siguienteHeap()
            genC3D.setHeap('H', '-1')                   #marco el final de la cadena con -1
            genC3D.siguienteHeap()
            return Return(nuevoTemp, Tipo.STRING, True)


