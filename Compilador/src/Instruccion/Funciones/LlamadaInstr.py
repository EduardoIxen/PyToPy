from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Expresion import Expresion
from src.Excepcion.Excepcion import Excepcion
from src.Abstract.Return import Return
from src.Ast.Tipo import Tipo
from src.Instruccion.Listas.TipoLista import TipoLista

class LlamadaInstr(Expresion):
    def __init__(self, id, parametros, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.parametros = parametros
        self.linea = linea
        self.columna = columna

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        #agregar funciones nativas

        simbFunc = entorno.obtenerFuncion(self.id)
        struct = entorno.getStruct(self.id)

        if struct is None:
            if simbFunc is None:
                genC3D.setExcepcion(Excepcion("Semantico", f"La funcion {self.id} no esta definida", self.linea, self.columna))
                return

            valorParams = []
            tamanio = genC3D.guardarTemporales(entorno)
            tamParamFun = len(simbFunc.parametros)      #para comparar parametros declarados con los recibidos
            tamParamRec = len(self.parametros)

            if tamParamFun != tamParamRec:
                genC3D.setExcepcion(Excepcion("Semantico", "La cantidad de parametros declarados no coincide con los recibidos.", self.linea, self.columna))
                return
            i = 0
            for param in self.parametros:
                parametroCompi = param.compilar(entorno)
                tipoAlmacenado = simbFunc.parametros[i]['tipo']
                tipoObtenido = parametroCompi.getTipo()

                if isinstance(tipoAlmacenado, TipoLista):
                    if isinstance(tipoObtenido, TipoLista):
                        if tipoAlmacenado.tipo != tipoObtenido.tipo:
                            genC3D.setExcepcion(Excepcion("Semantico", f"Parametro de tipo {tipoObtenido} no es compatible con {tipoAlmacenado}", self.linea, self.columna))
                            return
                    else:
                        if tipoAlmacenado.tipo != tipoObtenido.tipo:
                            genC3D.setExcepcion(Excepcion("Semantico", f"Se espera un argumento de tipo {tipoAlmacenado} pero se obtuvo uno de tipo {tipoObtenido}", self.linea, self.columna))
                            return
                else:
                    if isinstance(tipoAlmacenado, str):
                        struct = entorno.getStruct(tipoAlmacenado)
                        if struct.getTipo() != tipoObtenido:
                            genC3D.setExcepcion(Excepcion("Semantico", f"Se esperaba un argumento de tipo {tipoAlmacenado} pero se recibio {tipoObtenido}", self.linea, self.columna))
                            return
                    elif tipoAlmacenado == Tipo.ANY:
                        tipoAlmacenado = tipoObtenido
                    elif tipoObtenido != tipoAlmacenado and tipoAlmacenado != Tipo.ANY:
                        genC3D.setExcepcion(Excepcion("Semantico", f"La variable ingresada de tipo {tipoObtenido} no coincide con lo declarado {tipoAlmacenado}", self.linea, self.columna))
                        return

                if tipoObtenido == Tipo.BOOLEAN:
                    temp = genC3D.agregarTemp()
                    genC3D.liberarTemp(temp)
                    etiquTemp = genC3D.nuevaEtiqueta()
                    genC3D.agregarEtiqueta(parametroCompi.etiquetaTrue)
                    genC3D.agregarExpresion(temp, 'P', entorno.tamanio + i + 1, '+')
                    genC3D.setStack(temp, '1')
                    genC3D.agregarGoto(etiquTemp)
                    genC3D.agregarEtiqueta(parametroCompi.etiquetaFalse)
                    genC3D.agregarExpresion(temp, 'P', entorno.tamanio + i + 1, '+')
                    genC3D.setStack(temp, '0')
                    genC3D.agregarEtiqueta(etiquTemp)

                valorParams.append(parametroCompi)
                i += 1

            temp = genC3D.agregarTemp()
            genC3D.liberarTemp(temp)
            if len(valorParams) != 0:
                genC3D.agregarExpresion(temp, 'P', entorno.tamanio + 1, '+')
                pos = 0
                for val in valorParams:
                    if val.getTipo() != Tipo.BOOLEAN:
                        genC3D.liberarTemp(val.getValor())
                        genC3D.setStack(temp, val.getValor())
                    if pos != len(valorParams) - 1:
                        genC3D.agregarExpresion(temp, temp, '1', '+')

            genC3D.nuevoEntorno(entorno.tamanio)
            genC3D.llamarFunc(self.id)
            genC3D.getStack(temp, 'P')
            genC3D.retornarEntorno(entorno.tamanio)
            genC3D.obtenerTemporales(entorno, tamanio)
            genC3D.agregarAlmacTemp(temp)

            if simbFunc.getTipo() != Tipo.BOOLEAN:
                retornar = Return(temp, simbFunc.getTipo(), True)
                retornar.setTipoAux(simbFunc.getTipoAux())
                return retornar

            auxRetornar = Return('', simbFunc.getTipo(), False)
            if self.etiquetaTrue == '':
                self.etiquetaTrue = genC3D.nuevaEtiqueta()
            if self.etiquetaFalse == '':
                self.etiquetaFalse = genC3D.nuevaEtiqueta()
            genC3D.agregarIf(temp, '1', '==', self.etiquetaTrue)
            genC3D.agregarGoto(self.etiquetaFalse)
            auxRetornar.etiquetaTrue = self.etiquetaTrue
            auxRetornar.etiquetaFalse = self.etiquetaFalse
            return auxRetornar
        else:   #es un struct
            tempStruct = genC3D.agregarTemp()
            tempH = genC3D.agregarTemp()
            genC3D.agregarExpresion(tempStruct, 'H', '', '')
            genC3D.agregarExpresion(tempH, tempStruct, '', '')

            if len(self.parametros) != len(struct.atributos):
                genC3D.setExcepcion(Excepcion("Semantico", f"La cantidad de atributos son incorrectos {self.id}", self.linea, self.columna))
                return
            genC3D.agregarExpresion('H', 'H', len(self.parametros), '+')  #posiciones para referencias a los atributos

            tiposAuxiliares = []
            valoresAuxiliares = []
            for par in self.parametros:
                valor = par.compilar(entorno)
                genC3D.setHeap(tempH, valor.getValor())
                genC3D.agregarExpresion(tempH, tempH, '1', '+')
                tiposAuxiliares.append(valor.getTipo())
                valoresAuxiliares.append(valor)

            auxReturn = Return(tempStruct, struct.getTipo(), False, self.id)
            auxReturn.setAtributos(tiposAuxiliares)
            auxReturn.setValores(valoresAuxiliares)
            return auxReturn

