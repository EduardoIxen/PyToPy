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
        if self.id == "upper":
            for param in self.parametros:
                ret = param.compilar(entorno)
                valor = ret.getValor()
                return Return(self.nativaUpper(entorno, valor), Tipo.STRING, False)
        elif self.id == "lower":
            for param in self.parametros:
                ret = param.compilar(entorno)
                valor = ret.getValor()
                return Return(self.nativaLower(entorno, valor), Tipo.STRING, False)
        elif self.id == "int":
            for param in self.parametros:
                expre = param.compilar(entorno)
                if expre.getTipo() == Tipo.STRING:
                    tempP = genC3D.agregarTemp()
                    tempP2 = genC3D.agregarTemp()
                    tempP3 = genC3D.agregarTemp()
                    tempP4 = genC3D.agregarTemp()
                    tempP5 = genC3D.agregarTemp()
                    genC3D.agregarExpresion(tempP, expre.getValor(), '', '')
                    genC3D.agregarExpresion(tempP3, '0', '', '')
                    compE = genC3D.nuevaEtiqueta()
                    avanE = genC3D.nuevaEtiqueta()
                    etiquSalida = genC3D.nuevaEtiqueta()
                    genC3D.agregarEtiqueta(compE)
                    genC3D.getHeap(tempP2, tempP)
                    genC3D.agregarIf(tempP2, '-1', '!=', avanE)
                    genC3D.agregarGoto(etiquSalida)
                    genC3D.agregarEtiqueta(avanE)
                    genC3D.agregarExpresion(tempP, tempP, '1', '+')
                    genC3D.agregarExpresion(tempP3, tempP3, '1', '+')
                    genC3D.agregarGoto(compE)
                    genC3D.agregarEtiqueta(etiquSalida)

                    compE = genC3D.nuevaEtiqueta()
                    avanE = genC3D.nuevaEtiqueta()
                    salidaE = genC3D.nuevaEtiqueta()
                    genC3D.agregarExpresion(tempP4, '1', '', '')
                    genC3D.agregarEtiqueta(compE)
                    genC3D.agregarIf(tempP3, '2', '>=', avanE)
                    genC3D.agregarGoto(salidaE)
                    genC3D.agregarEtiqueta(avanE)
                    genC3D.agregarExpresion(tempP4, tempP4, '10', '*')
                    genC3D.agregarExpresion(tempP3, tempP3, '1', '-')
                    genC3D.agregarGoto(compE)
                    genC3D.agregarEtiqueta(salidaE)

                    compE = genC3D.nuevaEtiqueta()
                    avanE = genC3D.nuevaEtiqueta()
                    salidaE = genC3D.nuevaEtiqueta()
                    genC3D.agregarExpresion(tempP, expre.getValor(), '', '')
                    genC3D.agregarExpresion(tempP5, '0', '', '')
                    genC3D.agregarEtiqueta(compE)
                    genC3D.getHeap(tempP2, tempP)
                    genC3D.agregarIf(tempP2, '-1', '!=', avanE)
                    genC3D.agregarGoto(salidaE)
                    genC3D.agregarEtiqueta(avanE)
                    genC3D.agregarExpresion(tempP2, tempP2, '48', '-')
                    genC3D.agregarExpresion(tempP2, tempP2, tempP4, '*')
                    genC3D.agregarExpresion(tempP5, tempP5, tempP2, '+')
                    genC3D.agregarExpresion(tempP4, tempP4, '10', '/')
                    genC3D.agregarExpresion(tempP, tempP, '1', '+')
                    genC3D.agregarGoto(compE)
                    genC3D.agregarEtiqueta(salidaE)
                    return Return(tempP5, Tipo.INT, True)
                elif expre.getTipo() == Tipo.FLOAT:
                    tempP = genC3D.agregarTemp()
                    genC3D.agregarExpresion(tempP, expre.getValor(), '', '')
                    tempP2 = genC3D.agregarTemp()
                    genC3D.addTrunc(tempP2, tempP)
                    return Return(tempP2, Tipo.INT, True)
                else:
                    genC3D.setExcepcion(Excepcion("Semantico", "Solo las cadenas se pueden convertir a int", self.linea, self.columna))
                    return
        elif self.id == "float":
            for param in self.parametros:
                expre = param.compilar(entorno)
                if expre.getTipo() == Tipo.STRING:
                    tempP = genC3D.agregarTemp()
                    tempP2 = genC3D.agregarTemp()
                    tempP3 = genC3D.agregarTemp()
                    tempP4 = genC3D.agregarTemp()
                    tempP5 = genC3D.agregarTemp()
                    genC3D.agregarExpresion(tempP, expre.getValor(), '', '')
                    genC3D.agregarExpresion(tempP3, '0', '', '')
                    compE = genC3D.nuevaEtiqueta()
                    avanE = genC3D.nuevaEtiqueta()
                    salidaE = genC3D.nuevaEtiqueta()
                    genC3D.agregarEtiqueta(compE)
                    genC3D.getHeap(tempP2, tempP)
                    genC3D.agregarIf(tempP2, '46', '!=', avanE)
                    genC3D.agregarGoto(salidaE)
                    genC3D.agregarEtiqueta(avanE)
                    genC3D.agregarExpresion(tempP, tempP, '1', '+')
                    genC3D.agregarExpresion(tempP3, tempP3, '1', '+')
                    genC3D.agregarGoto(compE)
                    genC3D.agregarEtiqueta(salidaE)

                    compE = genC3D.nuevaEtiqueta()
                    avanE = genC3D.nuevaEtiqueta()
                    salidaE = genC3D.nuevaEtiqueta()
                    genC3D.agregarExpresion(tempP4, '1', '', '')
                    genC3D.agregarEtiqueta(compE)
                    genC3D.agregarIf(tempP3, '2', '>=', avanE)
                    genC3D.agregarGoto(salidaE)
                    genC3D.agregarEtiqueta(avanE)
                    genC3D.agregarExpresion(tempP4, tempP4, '10', '*')
                    genC3D.agregarExpresion(tempP3, tempP3, '1', '-')
                    genC3D.agregarGoto(compE)
                    genC3D.agregarEtiqueta(salidaE)

                    compE = genC3D.nuevaEtiqueta()
                    avanE = genC3D.nuevaEtiqueta()
                    salidaE = genC3D.nuevaEtiqueta()
                    genC3D.agregarExpresion(tempP, expre.getValor(), '', '')
                    genC3D.agregarExpresion(tempP5, '0', '', '')
                    genC3D.agregarEtiqueta(compE)
                    genC3D.getHeap(tempP2, tempP)
                    genC3D.agregarIf(tempP2, '-1', '!=', avanE)
                    genC3D.agregarGoto(salidaE)
                    genC3D.agregarEtiqueta(avanE)
                    genC3D.agregarExpresion(tempP, tempP, '1', '+')
                    genC3D.agregarIf(tempP2, '46', '==', compE)
                    genC3D.agregarExpresion(tempP2, tempP2, '48', '-')
                    genC3D.agregarExpresion(tempP2, tempP2, tempP4, '*')
                    genC3D.agregarExpresion(tempP5, tempP5, tempP2, '+')
                    genC3D.agregarExpresion(tempP4, tempP4, '10', '/')
                    genC3D.agregarGoto(compE)
                    genC3D.agregarEtiqueta(salidaE)
                    return Return(tempP5, Tipo.FLOAT, True)
                elif expre.getTipo() == Tipo.INT:
                    tempP = genC3D.agregarTemp()
                    genC3D.agregarExpresion(tempP, expre.getValor(), '', '')
                    tempP2 = genC3D.agregarTemp()
                    genC3D.addTrunc(tempP2, tempP)
                    return Return(tempP2, Tipo.FLOAT, True)
                else:
                    genC3D.setExcepcion(Excepcion("Semantico", "Solo las cadenas se pueden convertir a float", self.linea, self.columna))
                    return
        elif self.id == "len":
            parametro = self.parametros[0].compilar(entorno)
            return Return(self.nativaLen(entorno, parametro.getValor()), Tipo.INT, False)

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

    def nativaUpper(self, entorno, valor):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.nativaUpper()
        paramTemp = genC3D.agregarTemp()
        genC3D.agregarExpresion(paramTemp, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(paramTemp, paramTemp, '1', '+')
        genC3D.setStack(paramTemp, valor)
        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('nativa_upper')
        temp = genC3D.agregarTemp()
        genC3D.getStack(temp, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())
        return temp

    def nativaLower(self, entorno, valor):
        nuevaIns = GeneradorC3D()
        genC3D = nuevaIns.getInstance()
        genC3D.nativaLower()

        tempParam = genC3D.agregarTemp()

        genC3D.agregarExpresion(tempParam, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(tempParam, tempParam, '1', '+')
        genC3D.setStack(tempParam, valor)

        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('nativa_lower')

        temp = genC3D.agregarTemp()
        genC3D.getStack(temp, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())
        return temp

    def nativaLen(self, entorno, valor):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.nativaLen()

        paramTemp = genC3D.agregarTemp()
        genC3D.agregarExpresion(paramTemp, 'P', entorno.getTamanio(), '+')
        genC3D.agregarExpresion(paramTemp, paramTemp, '1', '+')
        genC3D.setStack(paramTemp, valor)
        genC3D.nuevoEntorno(entorno.getTamanio())
        genC3D.llamarFunc('nativa_len')
        temp = genC3D.agregarTemp()
        genC3D.getStack(temp, 'P')
        genC3D.retornarEntorno(entorno.getTamanio())
        return temp

#revisado