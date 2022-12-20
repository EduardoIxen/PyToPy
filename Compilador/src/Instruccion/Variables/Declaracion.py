from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo
from src.Instruccion.Listas.TipoLista import TipoLista

class Declaracion(Instruccion):
    def __init__(self, id, expresion, tipo, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.expresion = expresion
        self.tipo = tipo

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        if isinstance(self.id, str):  #se obtiene un id
            if isinstance(self.expresion, str):
                valor = self.expresion.compilar(entorno)
            else:
                if self.tipo is None:
                    valor = self.expresion.compilar(entorno)

                else:
                    valor = self.expresion.compilar(entorno)
                    tipoVar = self.tipo

                    if isinstance(tipoVar, str):
                        #compilar struct
                        pass
                    if valor.getTipo() == Tipo.STRUCT or valor.getTipo() == Tipo.MUTSTRUCT:
                        if self.tipo != valor.getTipoAux():
                            genC3D.setExcepcion(Excepcion("Semantico", "Tipo incorrecto en struct", self.linea, self.columna))
                            return
                    else:
                        if type(tipoVar) == TipoLista:
                            if tipoVar.tipo != valor.getTipo():
                                genC3D.setExcepcion(Excepcion("Semantico", "Tipo de datos incompatibles.", self.linea, self.columna))
                                return
                        else:
                            if tipoVar != valor.getTipo():
                                genC3D.setExcepcion(Excepcion("Semantico", "El tipo de la variable no es el mismo que el de la expresion", self.linea, self.columna))
                                return

            nuevaVariable = entorno.getVariable(self.id) #veo si la variable existe para obtener su posicion en el heap
            if nuevaVariable == None: #si no existe la creo
                if valor.getTipo() == Tipo.STRUCT or valor.getTipo() == Tipo.MUTSTRUCT:
                    nuevaVariable = entorno.setVariable(self.id, valor.getTipo(), True, valor.getTipoAux(), valor.getAtributos(), valor.getValores())
                elif valor.getTipo() == Tipo.LIST:
                    if type(self.tipo) == TipoLista:
                        tipoVar = self.tipo
                    else:
                        tipoVar = Tipo.LIST
                    nuevaVariable = entorno.setVariable(self.id, tipoVar, True, valor.getTipoAux(), valor.getAtributos(), valor.getValores())
                else:
                    nuevaVariable = entorno.setVariable(self.id, valor.getTipo(), False)
            else:
                #Se actualiza la variable por si el valor cambia y el tipo tambien
                nuevaVariable = entorno.actualizarVar(self.id, valor.getTipo())

            posicionTemp = nuevaVariable.posicion

            if not nuevaVariable.esGlobal:
                posicionTemp = genC3D.agregarTemp()
                genC3D.agregarExpresion(posicionTemp, 'P', nuevaVariable.posicion, "+")

            if valor.getTipo() == Tipo.BOOLEAN:
                etiquTemp = genC3D.nuevaEtiqueta()
                genC3D.agregarEtiqueta(valor.etiquetaTrue)
                genC3D.setStack(posicionTemp, "1")
                genC3D.agregarGoto(etiquTemp)
                genC3D.agregarEtiqueta(valor.etiquetaFalse)
                genC3D.setStack(posicionTemp, "0")
                genC3D.agregarEtiqueta(etiquTemp)
            else:
                genC3D.setStack(posicionTemp, valor.valor)
            genC3D.agregarEspacio()
        else:  #asignacion para structs
            pass

