
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
        self.esPrint = False
        self.repetirString = False
        self.concatenarCadena = False
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
        self.esPrint = False
        self.almacenamientoTemp = {}
        GeneradorC3D.generadorC3D = GeneradorC3D()

    def getEncabezado(self):
        if self.math:
            encab = """/*---------------ENCABEZADO---------------*/\npackage main;\n\nimport (\n\t"fmt"\n\t"math"\n);\n\n"""
        else:
            encab = """/*---------------ENCABEZADO---------------*/\npackage main;\n\nimport (\n\t"fmt"\n);\n\n"""

        if len(self.temporales) > 0:
            encab += 'var '
            for i in range(len(self.temporales)):
                encab += self.temporales[i]
                if i != (len(self.temporales) - 1):
                    encab += ", "
            encab += " float64;\n"
        encab += "var P, H float64;\nvar stack [20180052]float64;\nvar heap [20180052]float64;\n"
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
        self.agregarPrint("c", 84)
        self.agregarPrint("c", 114)
        self.agregarPrint("c", 117)
        self.agregarPrint("c", 101)

    def imprimirFalse(self):
        self.agregarPrint("c", 70)
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

    def nuevoEntorno(self, tamanio):
        self.insertarCodigo(f'P = P + {tamanio};\n')

    def llamarFunc(self, id):
        self.insertarCodigo(f'{id}();\n')

    def retornarEntorno(self, tamanio):
        self.insertarCodigo(f'P = P - {tamanio};\n')

    def setHeap(self, posicion, valor):
        self.insertarCodigo(f'heap[int({posicion})] = {valor};\n')

    def getHeap(self, destino, posicion):
        self.insertarCodigo(f'{destino} = heap[int({posicion})];\n')

    def siguienteHeap(self):
        self.insertarCodigo('H = H + 1;\n')

    def getAlmacenamientoTemporal(self):
        return self.almacenamientoTemp

    def limpiarAlmacenamTemp(self):
        self.almacenamientoTemp = {}

    def setAlmacenamientTemp(self, almacenTemp):
        self.almacenamientoTemp = almacenTemp

    def agregarAlmacTemp(self, temp):
        if not temp in self.almacenamientoTemp.keys():
            self.almacenamientoTemp[temp] = temp

    def guardarTemporales(self, entorno):
        if len(self.almacenamientoTemp) > 0:
            temporal = self.agregarTemp()
            self.liberarTemp(temporal)

            tamanio = 0
            self.agregarEspacio()
            self.agregarComentario(" INICIO - GUARDANDO TEMPORALES ")
            self.agregarExpresion(temporal, 'P', entorno.tamanio, '+')

            for nombre in self.almacenamientoTemp:
                tamanio += 1
                self.setStack(temporal, self.almacenamientoTemp[nombre])
                if tamanio != len(self.almacenamientoTemp):
                    self.agregarExpresion(temporal, temporal, '1', '+')
            self.agregarComentario(" FIN - GUARDANDO TEMPORALES")
            self.agregarEspacio()

        puntero = entorno.tamanio
        entorno.tamanio = puntero + len(self.almacenamientoTemp)

        return puntero

    def obtenerTemporales(self, entorno, posicion):
        if len(self.almacenamientoTemp) > 0:
            temp = self.agregarTemp()
            self.liberarTemp(temp)

            tamanio = 0
            self.agregarEspacio()
            self.agregarComentario(" COMENZANDO A RECUPERAR TEMPORALES ")
            self.agregarExpresion(temp, 'P', posicion, '+')

            for nombre in self.almacenamientoTemp:
                tamanio += 1
                self.getStack(self.almacenamientoTemp[nombre], temp)
                if tamanio != len(self.almacenamientoTemp):
                    self.agregarExpresion(temp, temp, '1', '+')
            self.agregarComentario(" FIN RECUPERAR TEMPORALES ")
            self.agregarEspacio()
        entorno.tamanio = posicion

    def setExcepcion(self, valor):
        self.contExcepc += 1
        excepc = f"\"column1\": \"{self.contExcepc}\", \"column2\": \"{valor.getDescripcion()}\", \"column3\": \"{valor.getLinea()}\", \"column4\": \"{valor.getColumna()}\", \"column5\": \"{valor.getFechaHora()}\""
        excepc = "{" + excepc + "}"
        self.excepciones.append(excepc)

    def getExcepciones(self):
        errores = ''
        for err in self.excepciones:
            errores += err
        errores = "[" + errores[:-1] + "]"
        return errores

    # ESPACIO PARA LAS NATIVAS
    def nativaPrint(self):
        if self.esPrint:
            return
        self.esPrint = True
        self.enNativas = True

        '''Agregamos el nombre de la funcion nativa, una etiqueta para salir de la funcion y otra
        para comparar el fin de la cadena que se ingresa'''
        self.agregarInicioFunc('nativa_print')
        etiqReturn = self.nuevaEtiqueta()
        etiqComparacion = self.nuevaEtiqueta()

        '''Punteros para el stack P y para el heap H'''
        pTemporal = self.agregarTemp()
        self.liberarTemp(pTemporal)

        hTemp = self.agregarTemp()
        self.liberarTemp(hTemp)

        '''Comparar cada uno de los caracteres del string hasta encontrar el -1, cuando no lo encuentre
        se agrega una etiqueta ara imprimir el caracter y cuando encuentre el -1 se realiza un salto a
        la etiqueta return'''

        self.agregarExpresion(pTemporal, 'P', '1', '+')
        self.getStack(hTemp, pTemporal)

        tempComp = self.agregarTemp()
        self.liberarTemp(tempComp)

        self.agregarEtiqueta(etiqComparacion)

        self.getHeap(tempComp, hTemp)

        self.agregarIf(tempComp, '-1', '==', etiqReturn)

        self.agregarPrint('c', tempComp)

        self.agregarExpresion(hTemp, hTemp, '1', '+')

        self.agregarGoto(etiqComparacion)

        self.agregarEtiqueta(etiqReturn)

        self.agregarFinFunc()

        self.enNativas = False


    def nativaRepetirStr(self):
        if self.repetirString:
            return
        self.repetirString = True
        self.enNativas = True
        self.agregarInicioFunc("repetirString")
        tempNStr = self.agregarTemp()
        self.liberarTemp(tempNStr)

        tempContador = self.agregarTemp()
        self.liberarTemp(tempContador)

        tmpR = self.agregarTemp()
        self.liberarTemp(tmpR)
        tmpP = self.agregarTemp()
        self.liberarTemp(tmpP)
        tmpP2 = self.agregarTemp()
        self.liberarTemp(tmpP2)
        tmpH = self.agregarTemp()
        self.liberarTemp(tmpH)

        etiquSalida = self.nuevaEtiqueta()
        etiquInicio = self.nuevaEtiqueta()

        self.agregarExpresion(tempNStr, 'H', '', '')  #save start string
        self.agregarExpresion(tempContador, '1', '', '')

        self.agregarExpresion(tmpP, 'P', '1', '+')
        self.getStack(tmpP, tmpP)

        self.agregarExpresion(tmpP2, 'P', '2', '+')
        self.getStack(tmpP2, tmpP2)

        self.agregarExpresion(tmpR, tmpP, '','')       #iniciando el recorrido
        self.agregarEtiqueta(etiquInicio)

        self.getHeap(tmpH, tmpP)                        #sacando valores del heap

        etiqTrue = self.nuevaEtiqueta()
        self.agregarIf(tmpH, '-1', '==', etiqTrue)

        self.setHeap('H', tmpH)
        self.agregarExpresion(tmpP, tmpP, '1', '+')
        self.siguienteHeap()

        self.agregarGoto(etiquInicio)               #volviendo al inicio
        self.agregarEtiqueta(etiqTrue)              #termina el string
        self.agregarIf(tmpP2, tempContador, '==', etiquSalida)
        self.agregarExpresion(tempContador, tempContador, '1', '+')
        self.agregarExpresion(tmpP, tmpR, '','')    #devolver el puntero para realizar el recorrido nuevamente
        self.agregarGoto(etiquInicio)

        self.agregarEtiqueta(etiquSalida)
        self.setHeap('H', '-1')
        self.siguienteHeap()

        self.setStack('P', tempNStr)
        self.agregarFinFunc()
        self.enNativas = False


    def nativaConcatenar(self):
        if self.concatenarCadena:
            return
        self.concatenarCadena = True
        self.enNativas = True
        self.agregarInicioFunc("concatenarCadena")
        tmpStr = self.agregarTemp()

        tmpP = self.agregarTemp()
        self.liberarTemp(tmpP)
        tmpP2 = self.agregarTemp()
        self.liberarTemp(tmpP2)
        tmpH = self.agregarTemp()
        self.liberarTemp(tmpH)

        etiquReturn = self.nuevaEtiqueta()  #etiqueta para salir
        etiquInicio = self.nuevaEtiqueta()

        self.agregarExpresion(tmpStr, 'H', '','') #almacenando inicio de concatenacion
        self.agregarExpresion(tmpP, 'P', '1', '+')
        self.getStack(tmpP, tmpP)
        self.agregarExpresion(tmpP2, 'P', '2', '+')
        self.getStack(tmpP2, tmpP2)

        self.agregarGoto(etiquInicio) #iniciando recorrido
        self.agregarEtiqueta(etiquInicio)

        self.getHeap(tmpH, tmpP)

        etiquTrue = self.nuevaEtiqueta() #para la primera cadena
        etiquFalse = self.nuevaEtiqueta()

        self.agregarIf(tmpH, '-1', '==', etiquFalse)
        self.agregarGoto(etiquTrue)
        self.agregarEtiqueta(etiquTrue)

        self.setHeap('H', tmpH)     #concatenando la cadena
        self.siguienteHeap()
        self.agregarExpresion(tmpP, tmpP, '1', '+')
        self.agregarGoto(etiquInicio)

        self.agregarEtiqueta(etiquFalse)
        self.getHeap(tmpH, tmpP2)   #sacando valores del heap

        etiquTrue = self.nuevaEtiqueta()    #etiqueta para la segunda cadena
        self.agregarIf(tmpH, '-1', '==', etiquReturn)
        self.agregarGoto(etiquTrue)
        self.agregarEtiqueta(etiquTrue)

        self.setHeap('H', tmpH)
        self.siguienteHeap()
        self.agregarExpresion(tmpP2, tmpP2, '1', '+')
        self.agregarGoto(etiquFalse)

        self.agregarEtiqueta(etiquReturn)
        self.setHeap('H', '-1') #agregar simbolo para saber donde termina al cadena
        self.siguienteHeap()

        self.setStack('P', tmpStr)
        self.agregarFinFunc()
        self.enNativas = False



