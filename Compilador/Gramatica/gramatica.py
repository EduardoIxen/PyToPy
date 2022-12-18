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
    'def'       :'RDEF',
}

tokens = [
    'LINEANUEVA',
    'PARA',                     #signos
    'PARC',
    'PUNTO',
    'COMA',
    'DOSPTS',
    'LLAVEC',
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
t_LINEANUEVA        = r'\n'
t_PARA              = r'\('
t_PARC              = r'\)'
t_PUNTO             = r'\.'
t_COMA              = r'\,'
t_DOSPTS            = r'\:'
t_LLAVEC            = r'\}'
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
from src.Ast.Tipo import Tipo, TipoOperacion
from src.Instruccion.Print import Print
from src.Expresion.Aritmetica import Aritmetica
from src.Expresion.Relacional import Relacional
from src.Expresion.Logica import Logica
from src.Expresion.Unaria import Unaria
from src.Instruccion.Variables.Declaracion import Declaracion
from src.Expresion.Identificador import Identificador
from src.Instruccion.Funciones.Funcion import Funcion
from src.Instruccion.Funciones.LlamadaInstr import LlamadaInstr
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
                | funcion_instr LLAVEC
    '''
    t[0] = t[1]


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

def p_parametros_tipo(t):
    'PARAMETROSTIPO : PARAMETROSTIPO COMA PARAMETROTIPO'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametro_tipo(t):
    'PARAMETROSTIPO : PARAMETROTIPO'
    t[0] = [t[1]]

def p_parametro_tipo_id(t):
    '''PARAMETROTIPO : ID DOSPTS TIPO
                    | ID DOSPTS ID
                    | ID'''
    if len(t) == 4:
        t[0] = {"id": t[1], "tipo": t[3]}
    else:
        t[0] = {"id": t[1], "tipo": Tipo.ANY}

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
    '''instruccion      : imprimir_instr
                        | declaracion_instr
                        | llamada_instr
    '''
    t[0] = t[1]

#////////////////////////////////// IMPRIMIR //////////////////////////////////////////////
def p_imprimir(t):
    'imprimir_instr     : RPRINT PARA PARAMETROS PARC'
    t[0] = Print(t[3], t.lineno(1), find_column(t.slice[1]))

#////////////////////////////////////// DECLARACION ///////////////////////////////////////
def p_declaracion(t):
    '''declaracion_instr :  ID IGUAL expresion'''
    t[0] = Declaracion(t[1], t[3], None, t.lineno(2), find_column(t.slice[2]))

def p_declaracion2(t):
    '''declaracion_instr : ID DOSPTS TIPO IGUAL expresion'''
    t[0] = Declaracion(t[1], t[5], t[3], t.lineno(2), find_column(t.slice[2]))

#/////////////////////////////////// FUNCIONES ///////////////////////////////////////////
def p_funciones(t):
    '''funcion_instr :  RDEF ID PARA PARC DOSPTS instrucciones
                    | RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instrucciones'''

    if len(t) == 7:
        t[0] = Funcion(t[2], [], Tipo.ANY, t[6], t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = Funcion(t[2], t[4], Tipo.ANY, t[7], t.lineno(1), find_column(t.slice[1]))

#/////////////////////////////////// LLAMADA INSTR ///////////////////////////////////////
def p_llamada_instr(t):
    '''llamada_instr : ID PARA PARC
                    | ID PARA PARAMETROS PARC'''
    if len(t) == 4:
        t[0] = LlamadaInstr(t[1], [], t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = LlamadaInstr(t[1], t[3], t.lineno(1), find_column(t.slice[1]))

#//////////////////////////////////////// TIPO ///////////////////////////////////////////
def p_tipo(t):
    '''TIPO : RINT
            | RFLOAT
            | RBOOLEAN
            | RSTRING
            | ID''' #arraytype
    if t[1] == "int":
        t[0] = Tipo.INT
    elif t[1] == "float":
        t[0] = Tipo.FLOAT
    elif t[1] == "bool":
        t[0] = Tipo.BOOLEAN
    elif t[1] == "string":
        t[0] = Tipo.STRING
    elif type(t[1]) == "TypeArray":
        t[0] = t[1]
    else:
        t[0] = t[1]

#////////////////////////////// EXPRESIONES ARITMETICAS //////////////////////////////////
def p_aritmeticas(t):
    '''expresion     : expresion MAS expresion
                    | expresion MENOS expresion
                    | expresion MULTIPLICACION expresion
                    | expresion DIVISION expresion
                    | expresion POTENCIA expresion
                    | expresion MODULO expresion
                    '''
    if t[2] == '*':
        t[0] = Aritmetica(t[1], t[3], TipoOperacion.MULTIPLICACION, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == "+":
        t[0] = Aritmetica(t[1], t[3], TipoOperacion.SUMA, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(t[1], t[3], TipoOperacion.POTENCIA, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], t[3], TipoOperacion.RESTA, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(t[1], t[3], TipoOperacion.DIVISION, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(t[1], t[3], TipoOperacion.MODULO, t.lineno(2), find_column(t.slice[2]))

#////////////////////////////// EXPRESIONES RELACIONALES ///////////////////////////////////
def p_relacionales(t):
    '''expresion    : expresion MAYORQUE expresion
                    | expresion MENORQUE expresion
                    | expresion MAYORIGUAL expresion
                    | expresion MENORIGUAL expresion
                    | expresion IGUALIGUAL expresion
                    | expresion DIFERENTE expresion'''
    if t[2] == '>':
        t[0] = Relacional(t[1], t[3], TipoOperacion.MAYOR, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(t[1], t[3], TipoOperacion.MENOR, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(t[1], t[3], TipoOperacion.MAYORIGUAL, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(t[1], t[3], TipoOperacion.MENORIGUAL, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(t[1], t[3], TipoOperacion.IGUAL, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '!=':
        t[0] = Relacional(t[1], t[3], TipoOperacion.DIFERENTE, t.lineno(2), find_column(t.slice[2]))




#////////////////////////////// EXPRESIONES LOGICAS ///////////////////////////////////
def p_logicas(t):
    '''expresion    : expresion RAND expresion
                    | expresion ROR expresion'''
    if t[2] == "and":
        t[0] = Logica(t[1], t[3], TipoOperacion.AND, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == "or":
        t[0] = Logica(t[1], t[3], TipoOperacion.OR, t.lineno(2), find_column(t.slice[2]))

def p_expre_not(t):
    'expresion      : RNOT expresion %prec UNOT'
    if t[1] == 'not':
        t[0] = Logica(t[2], Primitivo(True, Tipo.BOOLEAN, t.lineno(1), find_column(t.slice[1])), TipoOperacion.NOT, t.lineno(1), find_column(t.slice[1]))

def p_negacion(t):
    'expresion      : MENOS expresion %prec UMENOS'
    t[0] = Unaria(t[2], t.lineno(1), find_column(t.slice[1]))

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
    t[0] = Identificador(t[1], Tipo.IDENTIFICADOR, t.lineno(1), find_column(t.slice[1]))

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
