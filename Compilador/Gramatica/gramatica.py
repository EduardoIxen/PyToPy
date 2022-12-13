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
    'print'     :'RPRINT',
    'False'     :'RFALSE',
    'True'      :'RTRUE',
}

tokens = [
    'PARA',                     #signos
    'PARC',
    'PUNTO',
    'COMA',
    'LINEANUEVA',
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
    'ID',

] + list(reservadas.values())

#tokens
t_PARA              = r'\('
t_PARC              = r'\)'
t_PUNTO             = r'\.'
t_COMA              = r'\,'
t_LINEANUEVA        = r'\n'
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
    print(f"Caracter invalido {t.value[0]} Fila {t.lexer.lineno} Columna {find_column(t)} ")

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(token):
    global input
    line_start = input.rfind('\n', 0, token.lexpos) + 1
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

# //////////////////////////////////// Creando la gramatica //////////////////////////////////////

from src.Ast.AST import AST
from src.Expresion.Primitivo import Primitivo
from src.Ast.Tipo import Tipo
from src.Instruccion.Print import Print
def p_init(t):
    'init            : ls_instr'
    t[0] = AST(t[1],0,0)

def p_init_empty(t):
    'init            : empty'
    t[0] = t[1]

def p_empty(t) :
    'empty :'
    t[0] = []

def p_ls_instr(t):
    'ls_instr   : ls_instr instr'
    t[1].append(t[2])
    t[0] = t[1]

def p_ls_instr2(t):
    'ls_instr   : instr'
    t[0] = [t[1]]

def p_instr_recib(t):
    '''instr    : instruccion
    '''
    t[0] = t[1]

#///////////////////////////////// FUNCIONES ///////////////////////////////////////////////
def p_funcion_instr(t):
    '''funcion_instr : '''

#////////////////////////////////////// PARAMETROS /////////////////////////////////////////
def p_lista_parametros(t):
    '''PARAMETROS   : PARAMETROS COMA PARAMETRO'''
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_parametro2(t):
    '''PARAMETROS   : PARAMETRO'''
    t[0] = [t[1]]

def p_parametro_v(t):
    '''PARAMETRO    : expresion'''
    t[0] = t[1]

#///////////////////////////////////////INSTRUCCIONES//////////////////////////////////////////////////
def p_instrucciones_instrucciones_instruccion(t):
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]

def p_instruccion(t):
    '''instruccion      : imprimir_instr'''
    t[0] = t[1]

#////////////////////////////////// IMPRIMIR //////////////////////////////////////////////
def p_imprimir(t):
    'imprimir_instr     : RPRINT PARA PARAMETROS PARC'
    t[0] = Print(t[3], t.lineno(1), find_column(t.slice[1]))

#////////////////////////////// EXPRESIONES ARITMETICAS ///////////////////////////////////
def p_aritmeticas(t):
    '''expresion     : expresion MAS expresion
                    | expresion MENOS expresion
                    | expresion MULTIPLICACION
                    | expresion DIVISION expresion
                    | expresion POTENCIA expresion
                    | expresion MODULO expresion
                    '''

#////////////////////////////// EXPRESIONES RELACIONALES ///////////////////////////////////
def p_relacionales(t):
    '''expresion    : expresion IGUALIGUAL expresion
                    | expresion MAYORQUE expresion
                    | expresion MENORQUE expresion
                    | expresion MAYORIGUAL expresion
                    | expresion MENORIGUAL expresion
                    | expresion DIFERENTE expresion'''


#////////////////////////////// EXPRESIONES LOGICAS ///////////////////////////////////
def p_logicas(t):
    '''expresion    : expresion RAND expresion
                    | expresion ROR expresion'''

def p_expre_not(t):
    'expresion      : RNOT expresion %prec UNOT'

def p_negacion(t):
    'expresion      : MENOS expresion %prec UMENOS'

#////////////////////////////// EXPRESION DE AGRUPACION /////////////////////////////
def p_parentesis(t):
    'expresion      : PARA expresion PARC'
    t[0] = t[2]

#/////////////////////////////// EXPRESIONES PRIMITIVOS ////////////////////////////
def p_expresion_entero(t):
    'expresion      : ENTERO'
    t[0] = Primitivo(t[1], Tipo.INT, t.lineno(1), find_column(t.slice[1]))

def p_expresion_decimal(t):
    'expresion      : DECIMAL'
    t[0] = Primitivo(t[1], Tipo.FLOAT, t.lineno(1), find_column(t.slice[1]))

def p_expresion_cadena(t):
    'expresion      : CADENA'
    t[0] = Primitivo(t[1], Tipo.STRING, t.lineno(1), find_column(t.slice[1]))

def p_expresion_id(t):
    'expresion      : ID'
    t[0] = Primitivo(t[1], Tipo.IDENTIFICADOR, t.lineno(1), find_column(t.slice[1]))

def p_expresion_bool(t):
    '''expresion    : RTRUE
                    | RFALSE
                    | RNULO'''
    if str(t[1]) == "True":
        t[0] = Primitivo(True, Tipo.BOOLEAN, t.lineno(1), find_column(t.slice[1]))
    elif str(t[1]) == "False":
        t[0] = Primitivo(False, Tipo.BOOLEAN, t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = t[0] = Primitivo(None, Tipo.NULL, t.lineno(1), find_column(t.slice[1]))

#//////////////////////////////////////// ERRORES /////////////////////////////////////////////
def p_error(t):
    print("Error sintactico en '%s'" % t.value)

parser = yacc.yacc()
input = ""

def parse(entrada):
    global input
    global lexer
    global parser
    input = entrada
    lexer = lex.lex()
    parser = yacc.yacc()
    return parser.parse(entrada)
