
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftRORleftRANDrightUNOTleftMENORQUEMAYORQUEMENORIGUALMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOleftPOTENCIArightUMENOSleftPUNTOCADENA COMA DECIMAL DIFERENTE DIVISION ENTERO ID IGUAL IGUALIGUAL LINEANUEVA MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MODULO MULTIPLICACION PARA PARC POTENCIA PUNTO RAND RBOOLEAN RFALSE RFLOAT RINT RLIST RNOT RNULO ROR RPRINT RSTRING RTRUE TSTRUCTinit            : ls_instrinit            : emptyempty :ls_instr   : ls_instr instrls_instr   : instrinstr    : instruccion\n    funcion_instr : PARAMETROS   : PARAMETROS COMA PARAMETROPARAMETROS   : PARAMETROPARAMETRO    : expresioninstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr\n    imprimir_instr     : RPRINT PARA PARAMETROS PARCexpresion     : expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion MULTIPLICACION expresion\n                    | expresion DIVISION expresion\n                    | expresion POTENCIA expresion\n                    | expresion MODULO expresion\n                    expresion    : expresion IGUALIGUAL expresion\n                    | expresion MAYORQUE expresion\n                    | expresion MENORQUE expresion\n                    | expresion MAYORIGUAL expresion\n                    | expresion MENORIGUAL expresion\n                    | expresion DIFERENTE expresionexpresion    : expresion RAND expresion\n                    | expresion ROR expresionexpresion      : RNOT expresion %prec UNOTexpresion      : MENOS expresion %prec UMENOSexpresion      : PARA expresion PARCexpresion      : ENTEROexpresion      : DECIMALexpresion      : CADENAexpresion      : IDexpresion    : RTRUE\n                    | RFALSE\n                    | RNULO'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,24,],[-3,0,-1,-2,-5,-6,-13,-4,-14,]),'RPRINT':([0,2,4,5,6,8,24,],[7,7,-5,-6,-13,-4,-14,]),'PARA':([7,9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'RNOT':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'MENOS':([9,10,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[14,14,27,14,14,-32,-33,-34,-35,-36,-37,-38,27,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-30,27,-31,-15,-16,-17,-18,-19,-20,27,27,27,27,27,27,27,27,]),'ENTERO':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'DECIMAL':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'CADENA':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'ID':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'RTRUE':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'RFALSE':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'RNULO':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'PARC':([11,12,13,16,17,18,19,20,21,22,23,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[24,-9,-10,-32,-33,-34,-35,-36,-37,-38,42,-30,-29,-31,-8,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'COMA':([11,12,13,16,17,18,19,20,21,22,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[25,-9,-10,-32,-33,-34,-35,-36,-37,-38,-30,-29,-31,-8,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),'MAS':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[26,-32,-33,-34,-35,-36,-37,-38,26,-30,26,-31,-15,-16,-17,-18,-19,-20,26,26,26,26,26,26,26,26,]),'MULTIPLICACION':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[28,-32,-33,-34,-35,-36,-37,-38,28,-30,28,-31,28,28,-17,-18,-19,-20,28,28,28,28,28,28,28,28,]),'DIVISION':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[29,-32,-33,-34,-35,-36,-37,-38,29,-30,29,-31,29,29,-17,-18,-19,-20,29,29,29,29,29,29,29,29,]),'POTENCIA':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[30,-32,-33,-34,-35,-36,-37,-38,30,-30,30,-31,30,30,30,30,-19,30,30,30,30,30,30,30,30,30,]),'MODULO':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[31,-32,-33,-34,-35,-36,-37,-38,31,-30,31,-31,31,31,-17,-18,-19,-20,31,31,31,31,31,31,31,31,]),'IGUALIGUAL':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[32,-32,-33,-34,-35,-36,-37,-38,32,-30,32,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,32,32,]),'MAYORQUE':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[33,-32,-33,-34,-35,-36,-37,-38,33,-30,33,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,33,33,]),'MENORQUE':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[34,-32,-33,-34,-35,-36,-37,-38,34,-30,34,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,34,34,]),'MAYORIGUAL':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[35,-32,-33,-34,-35,-36,-37,-38,35,-30,35,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,35,35,]),'MENORIGUAL':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[36,-32,-33,-34,-35,-36,-37,-38,36,-30,36,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,36,36,]),'DIFERENTE':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[37,-32,-33,-34,-35,-36,-37,-38,37,-30,37,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,37,37,]),'RAND':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[38,-32,-33,-34,-35,-36,-37,-38,38,-30,-29,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,38,]),'ROR':([13,16,17,18,19,20,21,22,23,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[39,-32,-33,-34,-35,-36,-37,-38,39,-30,-29,-31,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'ls_instr':([0,],[2,]),'empty':([0,],[3,]),'instr':([0,2,],[4,8,]),'instruccion':([0,2,],[5,5,]),'imprimir_instr':([0,2,],[6,6,]),'PARAMETROS':([9,],[11,]),'PARAMETRO':([9,25,],[12,43,]),'expresion':([9,10,14,15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,],[13,23,40,41,13,44,45,46,47,48,49,50,51,52,53,54,55,56,57,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> ls_instr','init',1,'p_init','gramatica.py',158),
  ('init -> empty','init',1,'p_init_empty','gramatica.py',162),
  ('empty -> <empty>','empty',0,'p_empty','gramatica.py',166),
  ('ls_instr -> ls_instr instr','ls_instr',2,'p_ls_instr','gramatica.py',170),
  ('ls_instr -> instr','ls_instr',1,'p_ls_instr2','gramatica.py',175),
  ('instr -> instruccion','instr',1,'p_instr_recib','gramatica.py',179),
  ('funcion_instr -> <empty>','funcion_instr',0,'p_funcion_instr','gramatica.py',185),
  ('PARAMETROS -> PARAMETROS COMA PARAMETRO','PARAMETROS',3,'p_lista_parametros','gramatica.py',189),
  ('PARAMETROS -> PARAMETRO','PARAMETROS',1,'p_lista_parametro2','gramatica.py',194),
  ('PARAMETRO -> expresion','PARAMETRO',1,'p_parametro_v','gramatica.py',198),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','gramatica.py',203),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',209),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',217),
  ('imprimir_instr -> RPRINT PARA PARAMETROS PARC','imprimir_instr',4,'p_imprimir','gramatica.py',223),
  ('expresion -> expresion MAS expresion','expresion',3,'p_aritmeticas','gramatica.py',228),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_aritmeticas','gramatica.py',229),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_aritmeticas','gramatica.py',230),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_aritmeticas','gramatica.py',231),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_aritmeticas','gramatica.py',232),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_aritmeticas','gramatica.py',233),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',240),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_relacionales','gramatica.py',241),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_relacionales','gramatica.py',242),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',243),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',244),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_relacionales','gramatica.py',245),
  ('expresion -> expresion RAND expresion','expresion',3,'p_logicas','gramatica.py',250),
  ('expresion -> expresion ROR expresion','expresion',3,'p_logicas','gramatica.py',251),
  ('expresion -> RNOT expresion','expresion',2,'p_expre_not','gramatica.py',254),
  ('expresion -> MENOS expresion','expresion',2,'p_negacion','gramatica.py',257),
  ('expresion -> PARA expresion PARC','expresion',3,'p_parentesis','gramatica.py',261),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','gramatica.py',266),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','gramatica.py',270),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',274),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',278),
  ('expresion -> RTRUE','expresion',1,'p_expresion_bool','gramatica.py',282),
  ('expresion -> RFALSE','expresion',1,'p_expresion_bool','gramatica.py',283),
  ('expresion -> RNULO','expresion',1,'p_expresion_bool','gramatica.py',284),
]
