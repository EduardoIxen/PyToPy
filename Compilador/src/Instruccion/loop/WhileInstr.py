from src.Ast.GeneradorC3D import GeneradorC3D
from src.Abstract.Instruccion import Instruccion
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Entorno import Entorno
from src.Ast.Tipo import Tipo

class WhileInstr(Instruccion):
    def __init__(self, condicion, instrucciones, linea, columna):
        super().__init__(linea, columna)
        self.condicion = condicion
        self.instrucciones = instrucciones

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()

        genC3D.agregarComentario("INICIO WHILE")
        genC3D.agregarEspacio()

        etiquetaContinuar = genC3D.nuevaEtiqueta()      #se utiliza para regresar a la condicion
        genC3D.agregarEtiqueta(etiquetaContinuar)

        condicion = self.condicion.compilar(entorno)
        if condicion.getTipo() != Tipo.BOOLEAN:
            genC3D.setExcepcion(Excepcion("Semantico", "La condicion ingresada no es de tipo BOOL", self.linea, self.columna))
            return

        nuevoEntorno = Entorno(entorno)
        nuevoEntorno.etiquetaBreak = condicion.etiquetaFalse  #si se activa el break, se salta a la etiqueta falsa de la condicion
        nuevoEntorno.etiquetaContinue = etiquetaContinuar     #salta directo a la condicion

        genC3D.agregarEtiqueta(condicion.etiquetaTrue)

        for instr in self.instrucciones:
            instr.compilar(nuevoEntorno)

        genC3D.agregarGoto(etiquetaContinuar)
        genC3D.agregarEtiqueta(condicion.etiquetaFalse)
        genC3D.agregarComentario("FIN WHILE")
        genC3D.agregarEspacio()



