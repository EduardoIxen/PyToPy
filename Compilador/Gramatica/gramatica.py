import ply.yacc as yacc

reservadas = {
    'int'       :'RINT',
    'float'     :'RFLOAT',
    'bool'      :'RBOOLEAN',
    'string'    :'RSTRING',
    'None'      :'RNULO',
    'list'      :'RLIST',
    'struct'    :'RSTRUCT',
    'mutable'   :'RMUTABLE',
    'or'        :'ROR',
    'and'       :'RAND',
    'not'       :'RNOT',
    'print'     :'RPRINT',
    'False'     :'RFALSE',
    'True'      :'RTRUE',
    'def'       :'RDEF',
    'if'        :'RIF',
    'else'      :'RELSE',
    'elif'      :'RELIF',
    'while'     :'RWHILE',
    'break'     :'RBREAK',
    'continue'  :'RCONTINUE',
    'return'    :'RRETURN',
    'for'       :'RFOR',
    'in'        :'RIN',
    'range'     :'RRANGE',
    'upper'     :'RUPPER',
    'lower'     :'RLOWER',
}

tokens = [
    'LINEANUEVA',
    'PARA',                     #signos
    'PARC',
    'PUNTO',
    'COMA',
    'DOSPTS',
    'LLAVEC',
    'CORCHA',
    'CORCHC',
    'PUNTOCOMA',
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
t_CORCHA            = r'\['
t_CORCHC            = r'\]'
t_PUNTOCOMA         = r'\;'
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
    ('left', 'IGUALIGUAL', 'DIFERENTE'),
    ('left','MENORQUE','MAYORQUE', 'MENORIGUAL', 'MAYORIGUAL'),
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
from src.Expresion.LlamadaExpre import LlamadaExpre
from src.Instruccion.Listas.Lista import Lista
from src.Instruccion.Listas.AccesoLista import AccesoLista
from src.Instruccion.Listas.TipoLista import TipoLista
from src.Instruccion.Struct.Struct import Struct
from src.Instruccion.Struct.GetStruct import GetStruct
from src.Instruccion.Condicional.IfInstr import IfInstr
from src.Instruccion.loop.WhileInstr import WhileInstr
from src.Instruccion.loop.BreakInstr import BreakInstr
from src.Instruccion.loop.ContinueInstr import ContinueInstr
from src.Instruccion.Funciones.ReturnInstr import ReturnInstr
from src.Instruccion.loop.ForInstr import ForInstr
from src.Instruccion.loop.RangeInstr import RangeInstr
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
    '''instruccion      : imprimir_instr finins
                        | declaracion_instr finins
                        | llamada_instr finins
                        | struct_instr
                        | if_instr
                        | while_instr
                        | break_instr finins
                        | continue_instr finins
                        | return_instr finins
                        | for_instr
    '''
    t[0] = t[1]

def p_finins(t) :
    '''finins       : PUNTOCOMA
                    |'''
    t[0] = None


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
    #provar con x = {valor, tipo}

def p_declaracion3(t):
    'declaracion_instr : ID ACCESOLISTA IGUAL expresion'
    t[0] = Declaracion(t[1], t[4], None, t.lineno(3), find_column(t.slice[3]))
    #probar con valor = [t[1], t[2]]

def p_declaracion4(t):
    '''declaracion_instr : GETSTRUCTS IGUAL expresion'''
    t[0] = Declaracion(t[1], t[3], None, t.lineno(2), find_column(t.slice[2]))

#/////////////////////////////////// FUNCIONES ///////////////////////////////////////////
def p_funciones(t):
    '''funcion_instr : RDEF ID PARA PARC DOSPTS instrucciones
                     | RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instrucciones'''
    #probar con tipo de retorno cuando tenga el return

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

def p_llamada_instr_upper(t):
    'llamada_instr : expresion PUNTO RUPPER PARA PARC'
    t[0] = LlamadaInstr('upper', [t[1]], t.lineno(2), find_column(t.slice[2]))

def p_llamada_instr_lower(t):
    'llamada_instr : expresion PUNTO RLOWER PARA PARC'
    t[0] = LlamadaInstr('lower', [t[1]], t.lineno(2), find_column(t.slice[2]))

def p_llamada_int_instr(t):
    'llamada_instr : RINT PARA expresion PARC'
    t[0] = LlamadaInstr("int", [t[3]], t.lineno(1), find_column(t.slice[1]))

def p_llamada_float_instr(t):
    'llamada_instr : RFLOAT PARA expresion PARC'
    t[0] = LlamadaInstr("float", [t[3]], t.lineno(1), find_column(t.slice[1]))

#///////////////////////////////// LLAMADA EXPRESION ////////////////////////////////////
def p_llamada_expresion(t):
    '''llamada_expre : ID PARA PARC
                     | ID PARA PARAMETROS PARC'''
    if len(t) == 4:
        t[0] = LlamadaExpre(t[1], [], t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = LlamadaExpre(t[1], t[3], t.lineno(1), find_column(t.slice[1]))

def p_llamada_upper(t):
    'llamada_expre : expresion PUNTO RUPPER PARA PARC'
    t[0] = LlamadaExpre('upper', [t[1]], t.lineno(2), find_column(t.slice[2]))

def p_llamada_lower(t):
    'llamada_expre : expresion PUNTO RLOWER PARA PARC'
    t[0] = LlamadaExpre('lower', [t[1]], t.lineno(2), find_column(t.slice[2]))

def p_llamada_int(t):
    'llamada_expre : RINT PARA expresion PARC'
    t[0] = LlamadaExpre("int", [t[3]], t.lineno(1), find_column(t.slice[1]))

def p_llamada_float(t):
    'llamada_expre : RFLOAT PARA expresion PARC'
    t[0] = LlamadaExpre("float", [t[3]], t.lineno(1), find_column(t.slice[1]))

#///////////////////////////////////// LISTAS ////////////////////////////////////////////
def p_listas(t):
    '''LISTA : CORCHA PARAMETROS CORCHC'''
    t[0] = Lista(t[2], t.lineno(1), find_column(t.slice[1]))

#////////////////////////////////// ACCESO A LISTAS //////////////////////////////////////
def p_acceso_lista(t):
    'ACCESOLISTA : ACCESOLISTA ITEMLISTA'
    t[1].append(t[2])
    t[0] = t[1]

def p_acceso_lista2(t):
    'ACCESOLISTA : ITEMLISTA'
    t[0] = [t[1]]

def p_item_lista(t):
    'ITEMLISTA : CORCHA expresion CORCHC'
    t[0] = t[2]

#///////////////////////////////////// TIPO LISTA ////////////////////////////////////////
def p_tipo_lista(t):
    'tipo_lista : RLIST PARA TIPO PARC'
    t[0] = TipoLista(t[3], Tipo.LIST, t.lineno(1), find_column(t.slice[1]))

#/////////////////////////////////////// STRUCTS /////////////////////////////////////////
def p_instr_struct(t):
    '''struct_instr : RMUTABLE RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC
                    | RMUTABLE RSTRUCT ID LLAVEC
                    | RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC
                    | RSTRUCT ID LLAVEC
    '''
    if len(t) == 6:
        t[0] = Struct(t[3], t[4], t.lineno(1), find_column(t.slice[1]), True)
    elif len(t) == 5:
        if t[1] == "mutable":
            t[0] = Struct(t[3], [], t.lineno(1), find_column(t.slice[1]), True)
        else:
            t[0] = Struct(t[2], t[3], t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = Struct(t[2], [], t.lineno(1), find_column(t.slice[1]))

def p_atrib_struct(t):
    'ATRIBUTOSSTRUCT : ATRIBUTOSSTRUCT ATRIBSTRUCT PUNTOCOMA'
    t[1].append(t[2])
    t[0] = t[1]

def p_atrib_struct2(t):
    'ATRIBUTOSSTRUCT : ATRIBSTRUCT PUNTOCOMA'
    t[0] = [t[1]]

def p_atrib_item(t):
    '''ATRIBSTRUCT : ID DOSPTS TIPO
                    | ID DOSPTS ID
                    | ID'''
    if (len(t) == 2):
        t[0] = {"id": t[1], "tipo": Tipo.ANY}
    else:
        t[0] = {"id": t[1], "tipo": t[3]}

def p_get_struct(t):
    '''GETSTRUCTS : GETSTRUCTS PUNTO GETSTRUCT'''
    t[1].append(t[3])
    t[0] = t[1]

def p_get_strct2(t):
    '''GETSTRUCTS : GETSTRUCT'''
    t[0] = [t[1]]

def p_get_item(t):
    'GETSTRUCT : ID'
    t[0] = t[1]

#////////////////////////////////////////// IF ///////////////////////////////////////////
def p_if_instr(t):
    '''if_instr : RIF expresion DOSPTS instrucciones LLAVEC'''
    t[0] = IfInstr(t[2], t[4], None, None, t.lineno(1), find_column(t.slice[1]))

def p_if_instr2(t):
    'if_instr : RIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVEC'
    t[0] = IfInstr(t[2], t[4], t[8], None, t.lineno(1), find_column(t.slice[1]))
def p_if_instr3(t):
    'if_instr : RIF expresion DOSPTS instrucciones LLAVEC lista_elif'
    t[0] = IfInstr(t[2], t[4], None, t[6], t.lineno(1), find_column(t.slice[1]))

def p_lista_elif(t):
    '''lista_elif : lista_elif elif_inst'''
    t[1].append(t[2])
    t[0] = t[1]

def p_lista_elif2(t):
    'lista_elif : elif_inst'
    t[0] = [t[1]]

def p_lista_elif_item(t):
    'elif_inst : RELIF expresion DOSPTS instrucciones LLAVEC'
    t[0] = IfInstr(t[2], t[4], None, None, t.lineno(1), find_column(t.slice[1]))

def p_lista_elif_item2(t):
    '''elif_inst : RELIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVEC'''
    t[0] = IfInstr(t[2], t[4], t[8], None, t.lineno(1), find_column(t.slice[1]))

def p_lista_elif_item3(t):
    'elif_inst : RELIF expresion DOSPTS instrucciones LLAVEC lista_elif'
    t[0] = IfInstr(t[2], t[4], None, t[6], t.lineno(1), find_column(t.slice[1]))

#/////////////////////////////////////// WHILE ///////////////////////////////////////////
def p_while_instr(t):
    'while_instr : RWHILE expresion DOSPTS instrucciones LLAVEC'
    t[0] = WhileInstr(t[2], t[4], t.lineno(1), find_column(t.slice[1]))

#///////////////////////////////////////// BREAK ////////////////////////////////////////
def p_break_instr(t):
    'break_instr : RBREAK'
    t[0] = BreakInstr(t.lineno(1), find_column(t.slice[1]))

#////////////////////////////////////// CONTINUE ///////////////////////////////////////
def p_continue_instr(t):
    'continue_instr : RCONTINUE'
    t[0] = ContinueInstr(t.lineno(1), find_column(t.slice[1]))

#///////////////////////////////////// RETURN ///////////////////////////////////////////
def p_return_instr(t):
    'return_instr : RRETURN expresion'
    t[0] = ReturnInstr(t[2], t.lineno(1), find_column(t.slice[1]))

#//////////////////////////////////////// FOR ////////////////////////////////////////////
def p_for_instr(t):
    '''for_instr : RFOR ID RIN expresion DOSPTS instrucciones LLAVEC'''
    t[0] = ForInstr(t[2], t[4], t[6], t.lineno(1), find_column(t.slice[1]))

def p_for_range_instr(t):
    'for_instr : RFOR ID RIN range_instr DOSPTS instrucciones LLAVEC'
    t[0] = ForInstr(t[2], t[4], t[6], t.lineno(1), find_column(t.slice[1]))

def p_range(t):
    'range_instr : RRANGE PARA expresion PARC'
    t[0] = RangeInstr(Primitivo(1, Tipo.INT, t.lineno(1), find_column(t.slice[1])), t[3], t.lineno(1), find_column(t.slice[1]))

#//////////////////////////////////////// TIPO ///////////////////////////////////////////
def p_tipo(t):
    '''TIPO : RINT
            | RFLOAT
            | RBOOLEAN
            | RSTRING
            | ID
            | tipo_lista
            '''
    if t[1] == "int":
        t[0] = Tipo.INT
    elif t[1] == "float":
        t[0] = Tipo.FLOAT
    elif t[1] == "bool":
        t[0] = Tipo.BOOLEAN
    elif t[1] == "string":
        t[0] = Tipo.STRING
    elif type(t[1]) == TipoLista:  #probar si funciona
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
                    | expresion PUNTO expresion
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
    elif t[2] == '.':
        t[0] = GetStruct(t[1], t[3], t.lineno(2), find_column(t.slice[2]))

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
        #probar dejar der como None

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

#///////////////////////////////// EXPRESION LISTA ////////////////////////////////////////////
def p_expresion_lista(t):
    'expresion :    LISTA'
    t[0] = t[1]

def p_expresion_accesolst(t):
    'expresion : ID ACCESOLISTA'
    t[0] = AccesoLista(t[1], t[2], t.lineno(1), find_column(t.slice[1]))

#//////////////////////////////////// EXPRESION LLAMADA ///////////////////////////////////////
def p_expresion_llamada(t):
    'expresion : llamada_expre'
    t[0] = t[1]

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
