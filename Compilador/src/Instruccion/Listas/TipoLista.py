from src.Abstract.Expresion import Expresion
from src.Abstract.Return import Return


class TipoLista(Expresion):
    def __init__(self, valor, tipo, linea, columna):
        super().__init__(linea, columna)
        self.valor = valor
        self.tipo = tipo

    def compilar(self, entorno):
        return Return("", self.tipo, False)
