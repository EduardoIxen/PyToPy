from Tipo import Tipo

class GeneradorC3D:
    generadorC3D = None

    def __init__(self):
        self.contTemp = 0
        self.contEtiq = 0
        self.contExcepc = 0
        self.codigo = ''
        self.funciones = ''
        self.nativas = ''
        self.enFuncion = False
        self.enNativas = False
        self.temporales = []

        #agregar funciones nativas
        self.printStr = False
        self.math = False
        self.excepciones = []
        self.almacenamientoTemp = {}

    def getInstance(self):
        if GeneradorC3D.generadorC3D == None:
            GeneradorC3D.generadorC3D = GeneradorC3D()
            return GeneradorC3D.generadorC3D

    def resetGenerador(self):
        self.contTemp = 0
        self.contEtiq = 0
        self.codigo = ''
        self.funciones = ''
        self.nativas = ''
        self.enNativas = ''
        self.enFuncion = ''
        self.temporales = []
        self.printStr = False
        self.almacenamientoTemp = {}
        GeneradorC3D.generadorC3D = GeneradorC3D()

    def getEncabezado(self):
        if self.math:
            encab = """
            /*---------------ENCABEZADO---------------*/
            import(
                "fmt"
                "math"
            );
            """
        else:
            encab = """
            /*---------------ENCABEZADO---------------*/
            import(
                "fmt"
            );
            
            """

        if len(self.temporales) > 0:
            encab += 'var '
            for i in range(len(self.temporales)):
                encab += self.temporales[i]
                if i != (len(self.temporales) - 1):
                    encab += ", "
            encab += " float64;\n"
        encab += "var P, H float64;" \
                 "var stack [20180052]float64;" \
                 "var heap [20180052]float64;\n"
        return encab

    def obtenerC3D(self):
        return f"{self.getEncabezado()}" \
               f"{self.nativas}" \
               f"{self.funciones}" \
               f"func main(){{\n{self.codigo}\n\t}}"

    def insertarCodigo(self, codigo, tab="\t"):
        if self.enNativas:
            if self.nativas == '':
                self.nativas = self.nativas + '/*----------- NATIVAS -----------*/\n'
            self.nativas = self.nativas + tab + codigo
        elif self.enFuncion:
            if self.funciones == '':
                self.funciones = self.funciones + '/*--------- FUNCIONES -----------*/\n'
            self.funciones = self.funciones + tab + codigo
        else:
            self.codigo += '\n' + codigo

    def agregarComentario(self, comentario):
        self.insertarCodigo(f"/* {comentario} */")

    def agregarEspacio(self):
        self.insertarCodigo("\n")

    def agregarTemp(self):
        temp = f"t{self.contTemp}"
        self.contTemp += 1
        self.temporales.append(temp)
        self.almacenamientoTemp[temp] = temp
        return temp

    def agregarExpresion(self, resultado, izq, der, operacion):
        self.liberarTemp(izq)
        self.liberarTemp(der)
        self.insertarCodigo(f"{resultado} = {izq}{operacion}{der};\n")

    def agregarExponModulo(self, resultado, izq, der):
        self.insertarCodigo(f"{resultado} = math.Mod({izq}, {der});\n")

    def liberarTemp(self, temp):
        if temp in self.almacenamientoTemp.keys():
            del self.almacenamientoTemp[temp]

    def agregarPrint(self, tipo, valor):
        self.liberarTemp(valor)
        if tipo == 'f':
            self.insertarCodigo(f'fmt.Printf("%{tipo}", {valor});\n')
        else:
            self.insertarCodigo(f'fmt.Printf("%{tipo}", int({valor}));\n')

    def imprimirTrue(self):
        self.agregarPrint("c", 116)
        self.agregarPrint("c", 114)
        self.agregarPrint("c", 117)
        self.agregarPrint("c", 101)

    def imprimirFalse(self):
        self.agregarPrint("c", 102)
        self.agregarPrint("c", 97)
        self.agregarPrint("c", 108)
        self.agregarPrint("c", 115)
        self.agregarPrint("c", 101)

    def imprimirNone(self):
        self.agregarPrint("c", 78)  # N
        self.agregarPrint("c", 111) # o
        self.agregarPrint("c", 110) # n
        self.agregarPrint("c", 101) # e

    def imprimirMathError(self):
        self.agregarPrint("c", 77)  # M
        self.agregarPrint("c", 97)  # a
        self.agregarPrint("c", 116) # t
        self.agregarPrint("c", 104) # h
        self.agregarPrint("c", 69)  # E
        self.agregarPrint("c", 114) # r
        self.agregarPrint("c", 114) # r
        self.agregarPrint("c", 111) # o
        self.agregarPrint("c", 114) # r
        self.agregarPrint("c", 10)  # \n

    def imprimirBoundsError(self):
        self.agregarPrint("c", 66)  # B
        self.agregarPrint("c", 111) # o
        self.agregarPrint("c", 117) # u
        self.agregarPrint("c", 110) # n
        self.agregarPrint("c", 100) # d
        self.agregarPrint("c", 115) # s
        self.agregarPrint("c", 69)  # E
        self.agregarPrint("c", 114) # r
        self.agregarPrint("c", 114) # r
        self.agregarPrint("c", 111) # o
        self.agregarPrint("c", 114) # r
        self.agregarPrint("c", 10)  # \n

    def nuevaLinea(self):
        self.agregarPrint("c", 10)

    def nuevaEtiqueta(self):
        etiq = f'L{self.contEtiq}'
        self.contEtiq += 1
        return etiq

    def agregarEtiqueta(self, etiqueta):
        self.insertarCodigo(f'{etiqueta}:\n')

    def agregarGoto(self, etiqueta):
        self.insertarCodigo(f'goto {etiqueta};\n')

    def agregarInicioFunc(self, id):
        if not self.enNativas:
            self.enFuncion = True
        self.insertarCodigo(f'func {id}() {{\n', '')

    def agregarFinFunc(self):
        self.insertarCodigo('return;\n}\n')
        if not self.enNativas:
            self.enFuncion = False

    def agregarIf(self, izq, der, operacion, etiqueta):
        self.liberarTemp(izq)
        self.liberarTemp(der)
        self.insertarCodigo(f'if {izq} {operacion} {der} {{goto {etiqueta};}}\n')

    def setStack(self, posicion, valor):
        self.insertarCodigo(f'stack[int({posicion})] = {valor};\n')

    def getStack(self, destino, posicion):
        self.insertarCodigo(f'{destino} = stack[int({posicion})];\n')

    