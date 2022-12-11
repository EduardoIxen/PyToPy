from datetime import datetime

class Excepcion:
    def __init__(self, tipo, descripcion, linea, columna):
        self.tipo = tipo
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        fecha_hora = datetime.now()
        fecha_hora_formateada = fecha_hora.strftime('%d/%m/%Y %H:%M:%S')
        self.fecha_h = fecha_hora_formateada

    def getTipo(self):
        return self.tipo

    def getDescripcion(self):
        return self.descripcion

    def getLinea(self):
        return self.linea

    def getColumna(self):
        return self.columna

    def getFechaHora(self):
        return self.fecha_h

    def __str__(self) -> str:
        return f"Error: {self.tipo} {self.descripcion} {self.linea} {self.columna} {self.fecha_h}"