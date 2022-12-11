from Tipo import Tipo

class TablaTipo:
    def __init__(self):
        self.tipos = [
            [Tipo.INT,   Tipo.FLOAT, Tipo.INT,      Tipo.CHAR,  Tipo.ERROR],
            [Tipo.FLOAT, Tipo.FLOAT, Tipo.ERROR,    Tipo.ERROR, Tipo.ERROR],
            [Tipo.INT,   Tipo.FLOAT, Tipo.BOOLEAN,  Tipo.ERROR, Tipo.ERROR],
            [Tipo.CHAR,  Tipo.ERROR, Tipo.CHAR,     Tipo.CHAR,  Tipo.ERROR],
            [Tipo.ERROR, Tipo.ERROR, Tipo.ERROR,    Tipo.ERROR, Tipo.ERROR]
        ]


    def obtenerTipo(self, izq, der):
        return self.tipos[izq.value][der.value]

'''
            [1 , 2 , 1 , 4 , 5]
            [2 , 2 , 5 , 5 , 5]
            [1 , 2 , 3 , 5 , 5]
            [4 , 5 , 4 , 4 , 5]
            [5 , 5 , 5 , 5 , 5]

[1][1]
[1][2]

int 1
float 2
bool 3
char 4
error 5
'''