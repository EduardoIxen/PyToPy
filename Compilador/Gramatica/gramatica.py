import ply.yacc as yacc

reservadas = {
    'int'       :'RINT',
    'float'     :'RFLOAT',
    'bool'      :'RBOOLEAN',
    'string'    :'RSTRING',
    'None'      :'RNULO',
    'list'      :'RLIST',
    'Struct'    :'TSTRUCT',
    'or'        :'ROR',
    'and'       :'RAND',
    'not'       :'RNOT',
    'print'     :'RPRINT'
}

tokens = [
    'PARA',                     #signos
    'PARC',
    'PUNTO',
    'MAS',                      #aritmeticas
    'MENOS',
    'MODULO',
    'DIVISION',
    'POTENCIA',
    'MULTIPLICACION',
    'MENORQUE',                 #relacionales
    'MAYORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'IGUALIGUAL',
    'DIFERENTE',
    'IGUAL',
    'DECIMAL',                  #DATOS
    'ENTERO',
    'CADENA',
    'ID'

] + list(reservadas.values())

#tokens
t_PARA              = r'\('
t_PARC              = r'\)'
t_PUNTO             = r'\.'
t_MAS               = r'\+'
t_MENOS             = r'\-'
t_MODULO            = r'\%'
t_DIVISION          = r'\/'
t_POTENCIA          = r'\*\*'
t_MULTIPLICACION    = r'\*'
t_MENORQUE          = r'\<'
t_MAYORQUE          = r'\>'
t_MENORIGUAL        = r'\<='
t_MAYORIGUAL        = r'\>='
t_IGUALIGUAL        = r'\=='
t_DIFERENTE         = r'\!='
t_IGUAL             = r'\='

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_ComentarioMulti(t):
    r'\#\=(.|\n)*\=\#'
    t.lexer.lineno += t.value.count("\n")


def t_ComentarioSimple(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Caracter invalido {t.value[0]} Fila {t.lexer.lineno} Columna {find_column(input, t)} ")

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


#Caracteres especiales en cadenas
def especiales(cadena):
    cadena = cadena.replace('\\n', '\n')
    cadena = cadena.replace('\\"', '\"')
    cadena = cadena.replace('\\t', '      ')
    cadena = cadena.replace("\\'","\'")
    cadena = cadena.replace('\\\\', '\\')
    cadena = cadena.replace('\\r', '\r')
    return cadena


# Inicio de la construccion del analizador léxico
import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','ROR'),
    ('left','RAND'),
    ('right', 'UNOT'),
    ('left','MENORQUE','MAYORQUE', 'MENORIGUAL', 'MAYORIGUAL', 'IGUALIGUAL', 'DIFERENTE'),
    ('left','MAS','MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('left', 'POTENCIA'),
    ('right','UMENOS'),
    ('left', 'PUNTO'),
)

# Creando la gramatica