from src.Ast.GeneradorC3D import GeneradorC3D
from src.Ast.Tipo import Tipo
from src.Abstract.Instruccion import Instruccion
from src.Abstract.Return import Return

class GetStruct(Instruccion):
    def __init__(self, izq, der , linea, columna):
        super().__init__(linea, columna)
        self.izq = izq
        self.der = der

    def compilar(self, entorno):
        nuevaInst = GeneradorC3D()
        genC3D = nuevaInst.getInstance()
        genC3D.agregarComentario("----------- INICIO ACCESO A STRUCT -----------")
        genC3D.agregarEspacio()
        izq = self.izq.compilar(entorno)        #izq es el id del struct
        if self.der is not None:
            der = self.der.getId()              #der serian los accesos o atributos

        temp = genC3D.agregarTemp()
        tipo = None
        if izq is not None:
            if (izq.getTipo() == Tipo.STRUCT or izq.getTipo() == Tipo.MUTSTRUCT):
                struct = entorno.getStruct(izq.getTipoAux())
                contador = 0
                for atrib in struct.atributos:
                    if atrib['id'] == der:
                        tipo = atrib['tipo']
                        if isinstance(tipo, str):                   #si es instancia de otro struct
                            der = entorno.getStruct(tipo)           #obtengo el struct (tipo)
                            tipo = der.getTipo()
                        if tipo == Tipo.STRUCT or tipo == Tipo.MUTSTRUCT:
                            genC3D.agregarExpresion(temp, izq.getValor(), contador, '+')
                            genC3D.getHeap(temp, temp)

                            auxReturn = Return(temp, tipo, True)
                            auxReturn.setTipoAux(der.getTipoAux())
                            auxReturn.setAtributos(der.getAtributos())
                            auxReturn.setValores(der.getValores())
                            return auxReturn
                        else:
                            genC3D.agregarComentario("LE SUMO EL NUMERO DE ATRIBUTO A LA POSICION DEL STRUCT")
                            genC3D.agregarEspacio()
                            genC3D.agregarExpresion(temp, izq.getValor(), contador, '+')
                            genC3D.getHeap(temp, temp)
                            break
                    contador += 1
        genC3D.agregarComentario("----------- FIN ACCESO A STRUCT -----------")
        genC3D.agregarEspacio()
        genC3D.agregarEspacio()
        return Return(temp, tipo, True)
