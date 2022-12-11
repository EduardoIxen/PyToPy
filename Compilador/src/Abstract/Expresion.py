from abc import ABC, abstractmethod

class Expresion(ABC):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna
        self.etiquetaTrue = ''
        self.etiquetaFalse = ''

    @abstractmethod
    def compilar(self, entorno):
        pass
