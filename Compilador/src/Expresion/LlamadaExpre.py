from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Expresion import Expresion
from src.Abstract.Return import Return
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo
from src.Instruccion.Listas.TipoLista import TipoLista

class LlamadaExpre(Expresion):
    def __init__(self, id, parametros, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.parametros = parametros

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        #agregar funciones nativas

        simbFuncion = entorno.obtenerFuncion(self.id)
        struct = entorno.getStruct(self.id)

        if struct is None:
            if simbFuncion is None:
                genC3D.setExcepcion(Excepcion("Semantico", f"No se encuentra a {self.id}", self.linea, self.columna))
                return

            valoresParametros = []
            tamanio = genC3D.guardarTemporales(entorno)
            tamAlmacenado = len(simbFuncion.parametros)
            tamRecibido = len(self.parametros)

            if tamAlmacenado != tamRecibido:
                genC3D.setExcepcion(Excepcion("Semantico", f"La cantidad de parametros no coincide, se esperaban {tamAlmacenado}", self.linea, self.columna))
                return

            index = 0
            for par in self.parametros:
                paramCompi = par.compilar(entorno)
                tipoAlmacenado = simbFuncion.parametros[index]['tipo']
                tipoRecibido = paramCompi.getTipo()

                if isinstance(tipoAlmacenado, TipoLista):
                    if tipoAlmacenado.tipo != tipoRecibido.tipo:
                        genC3D.setExcepcion(Excepcion("Semantico", f"Se esperaba un parametro de tipo {tipoAlmacenado} pero se recibio {tipoRecibido}", self.linea, self.columna))
                        return
                else:
                    if isinstance(tipoAlmacenado, str):
                        struct = entorno.getStruct(tipoRecibido)
                        if struct.getTipo() != tipoRecibido:
                            genC3D.setExcepcion(Excepcion("Semantico", f"Se esperaba un parametro de tipo {tipoAlmacenado} pero se recibio {tipoRecibido}", self.linea, self.columna))
                            return
                    elif tipoAlmacenado != tipoRecibido:
                        genC3D.setExcepcion(Excepcion("Semantico", f"Se esperaba un parametro de tipo {tipoAlmacenado} pero se recibio {tipoRecibido}", self.linea, self.columna))
                        return

                if tipoRecibido == Tipo.BOOLEAN:
                    temp = genC3D.agregarTemp()
                    genC3D.liberarTemp(temp)

                    etiquTemp = genC3D.nuevaEtiqueta()
                    genC3D.agregarEtiqueta(paramCompi.etiquetaTrue)
                    genC3D.agregarExpresion(temp, 'P', entorno.tamanio + index + 1, '+')
                    genC3D.setStack(temp, '1')
                    genC3D.agregarGoto(etiquTemp)
                    genC3D.agregarEtiqueta(paramCompi.etiquetaFalse)
                    genC3D.agregarExpresion(temp, 'P', entorno.tamanio + index + 1, '+')
                    genC3D.setStack(temp, '0')
                    genC3D.agregarEtiqueta(etiquTemp)

                valoresParametros.append(paramCompi)
                index += 1

            temp = genC3D.agregarTemp()
            genC3D.liberarTemp(temp)
            if len(valoresParametros) != 0:
                genC3D.agregarExpresion(temp, 'P', entorno.tamanio + 1, '+')
                i = 0
                for valor in valoresParametros:
                    if valor.getTipo() != Tipo.BOOLEAN:
                        genC3D.liberarTemp(valor.getValor())
                        genC3D.setStack(temp, valor.getValor())
                    if i != len(valoresParametros) - 1:
                        genC3D.agregarExpresion(temp, temp, '1', '+')

            genC3D.nuevoEntorno(entorno.tamanio)
            genC3D.llamarFunc(self.id)
            genC3D.getStack(temp, 'P')
            genC3D.retornarEntorno(entorno.tamanio)
            genC3D.obtenerTemporales(entorno, tamanio)
            genC3D.agregarAlmacTemp(temp)

            if simbFuncion.getTipo() != Tipo.BOOLEAN:
                auxReturn = Return(temp, simbFuncion.getTipo(), True)
                auxReturn.setTipoAux(simbFuncion.getTipoAux())
                return auxReturn
            auxReturn = Return('', simbFuncion.getTipo(), False)
            if self.etiquetaTrue == '':
                self.etiquetaTrue = genC3D.nuevaEtiqueta()
            if self.etiquetaFalse == '':
                self.etiquetaFalse = genC3D.nuevaEtiqueta()
            genC3D.agregarIf(temp, '1', '==', self.etiquetaTrue)
            genC3D.agregarGoto(self.etiquetaFalse)
            auxReturn.etiquetaTrue = self.etiquetaTrue
            auxReturn.etiquetaFalse = self.etiquetaFalse
            return auxReturn

        else: #es un struct
            structTemp = genC3D.agregarTemp()
            htemp = genC3D.agregarTemp()
            genC3D.agregarExpresion(structTemp, 'H', '', '')
            genC3D.agregarExpresion(htemp, structTemp, '', '')

            if len(self.parametros) != len(struct.atributos):
                genC3D.setExcepcion(Excepcion("Semantico", f"La cantidad de atributos no coincide con lo declarado - struct {self.id}", self.linea, self.columna))
                return
            genC3D.agregarExpresion('H', 'H', len(self.parametros), '+')

            tiposAuxiliares = []
            valoresAuxiliares = []
            for par in self.parametros:
                valor = par.compilar(entorno)
                genC3D.setHeap(htemp, valor.getValor())
                genC3D.agregarExpresion(htemp, htemp, '1', '+')
                tiposAuxiliares.append(valor.getTipo())
                valoresAuxiliares.append(valor)

            auxReturn = Return(structTemp, struct.getTipo(), False, self.id)
            auxReturn.setAtributos(tiposAuxiliares)
            auxReturn.setValores(valoresAuxiliares)
            return auxReturn
