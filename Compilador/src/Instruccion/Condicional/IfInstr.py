from src.Abstract.Instruccion import Instruccion
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Ast.Tipo import Tipo
from src.Excepcion.Excepcion import Excepcion

class IfInstr(Instruccion):
    def __init__(self, condicion, instrucciones, instruccionesElse, instruccionesElif, linea, columna):
        super().__init__(linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.instruccionesElse = instruccionesElse
        self.instruccionesElif = instruccionesElif

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.agregarComentario("INICIO IF")
        genC3D.agregarEspacio()

        #evaluando la condicion recibida
        resultCondi = self.condicion.compilar(entorno)
        if resultCondi.getTipo() != Tipo.BOOLEAN:
            genC3D.setExcepcion(Excepcion("Semantico", f"La condicion ingresada no es de tipo bool.", self.linea, self.columna))
            return
        genC3D.agregarEtiqueta(resultCondi.etiquetaTrue)

        for instr in self.instrucciones:
            instr.compilar(entorno)

        if self.instruccionesElif is not None:
            etiquSalida = genC3D.nuevaEtiqueta()
            genC3D.agregarGoto(etiquSalida)
            genC3D.agregarEtiqueta(resultCondi.etiquetaFalse)
            for instrElif in self.instruccionesElif:
                instrElif.compilar(entorno)
            genC3D.agregarEtiqueta(etiquSalida)
        elif self.instruccionesElse is not None:
            etiquSalida = genC3D.nuevaEtiqueta()
            genC3D.agregarGoto(etiquSalida)
            genC3D.agregarEtiqueta(resultCondi.etiquetaFalse)
            for instrElse in self.instruccionesElse:
                instrElse.compilar(entorno)
            genC3D.agregarEtiqueta(etiquSalida)
        elif (self.instruccionesElif is None and self.instruccionesElse is None):
            genC3D.agregarEtiqueta(resultCondi.etiquetaFalse)

        genC3D.agregarComentario("END IF")
        genC3D.agregarEspacio()
