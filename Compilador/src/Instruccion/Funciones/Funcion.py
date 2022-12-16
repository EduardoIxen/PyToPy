from src.Abstract.Instruccion import Instruccion
from src.Ast.GeneradorC3D import GeneradorC3D
from src.Excepcion.Excepcion import Excepcion
from src.Ast.Entorno import Entorno

class Funcion(Instruccion):
    def __init__(self, id, parametros, tipo, instrucciones, linea, columna):
        Instruccion.__init__(self, linea, columna)
        self.id = id
        self.tipo = tipo
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.yaCompilado = True

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        if self.yaCompilado:
            self.yaCompilado = False
            if self.validarParametros():
                genC3D.setExcepcion(Excepcion("Semantico", f"Parametro duplicado en {self.id}", self.linea, self.columna))
                return
            if not entorno.agregarFuncion(self.id, self):
                genC3D.setExcepcion(Excepcion("Semantico", f"La funcion ingresada ya existe {self.id}", self.linea, self.columna))
                return
        nuevoEntorno = Entorno(entorno) #crea un nuevo entorno para la funcion y le agregaa un nombre
        nuevoEntorno.setNombre('funcion')
        simbFuncion = entorno.getFuncion(self.id)
        etiquReturn = genC3D.nuevaEtiqueta()
        almacenamientoTemp = genC3D.getAlmacenamientoTemporal()
        nuevoEntorno.setEntornoFuncion(simbFuncion, etiquReturn)

        for param in self.parametros:
            tipo = param['tipo']
            if isinstance(tipo, str):
                #agregar c3d para structs
                pass
            nuevoEntorno.setVariable(param['id'], param['tipo'], False)
        genC3D.limpiarAlmacenamTemp()
        genC3D.agregarInicioFunc(self.id)
        for instr in self.instrucciones:
            instr.compilar(nuevoEntorno)

        genC3D.agregarGoto(etiquReturn)
        genC3D.agregarEtiqueta(etiquReturn)
        genC3D.agregarFinFunc()
        genC3D.setAlmacenamientTemp(almacenamientoTemp)

    def validarParametros(self):
        parametros = []
        for param in self.parametros:
            if isinstance(param, str):
                if param in parametros:
                    return True
                parametros.append(param)
            else:
                if param['id'] in parametros:
                    return True
                parametros.append(param['id'])
        return False
