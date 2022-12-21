from src.Abstract.Instruccion import Instruccion
from src.Ast.Tipo import Tipo

class Struct(Instruccion):
    def __init__(self, id, atributos, linea, columna, mutable = False):
        super().__init__(linea, columna)
        self.id = id
        self.atributos = atributos
        self.mutable = mutable

    def compilar(self, entorno):
        if self.mutable:
            entorno.setStruct(self.id, self, Tipo.MUTSTRUCT)
        else:
            entorno.setStruct(self.id, self, Tipo.STRUCT)