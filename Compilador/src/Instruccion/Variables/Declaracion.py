from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Tipo import Tipo

class Declaracion(Instruccion):
    def __init__(self, id, expresion, tipo, linea, columna):
        super().__init__(linea, columna)
        self.id = id
        self.expresion = expresion
        self.tipo = tipo

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        if isinstance(self.id, str):  #es solo un id
            if isinstance(self.expresion, str):
                valor = self.expresion.compilar(entorno)
            else:
                if self.tipo is None:
                    valor = self.expresion.compilar(entorno)
                    #print(valor.getTipo()) si tiene
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
                        if type(tipoVar) == "TypeArray":
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
                    if type(self.tipo) == "TypeArray":
                        tipoVar = self.tipo
                    else:
                        tipoVar = Tipo.LIST
                    nuevaVariable = entorno.setVariable(self.id, tipoVar, True, valor.getTipoAux(), valor.getAtributos(), valor.getValores())
                else:
                    nuevaVariable = entorno.setVariable(self.id, valor.getTipo(), False)

            posicionTemp = nuevaVariable.posicion

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

