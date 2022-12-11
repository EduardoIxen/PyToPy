from enum import Enum

class Tipo(Enum):
    INT             = 0
    FLOAT           = 1
    BOOLEAN         = 2
    CHAR            = 3
    STRING          = 4
    ERROR           = 5
    NULL            = 6
    IDENTIFICADOR   = 8
    FUNCION         = 9
    RETURN          = 10
    BREAK           = 11
    CONTINUE        = 12
    NATIVA          = 13
    STRUCT          = 14
    MUTSTRUCT       = 15
    RANGE           = 16
    LIST            = 17
    ANY             = 18
    TEMP            = 19
    VECTOR          = 20

class TipoOperacion(Enum):
    AND             = 0
    OR              = 1
    NOT             = 2
    IGUAL           = 3
    MAYOR           = 4
    MENOR           = 5
    MAYORIGUAL      = 6
    MENORIGUAL      = 7
    MODULO          = 8
    DIFERENTE       = 9
    POTENCIA        = 10
    SUMA            = 11
    RESTA           = 12
    MULTIPLICACION  = 13
    DIVISION        = 14
    MENOSUNARIO     = 15
