
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftRORleftRANDrightUNOTleftMENORQUEMAYORQUEMENORIGUALMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOleftPOTENCIArightUMENOSleftPUNTOCADENA COMA CORCHA CORCHC DECIMAL DIFERENTE DIVISION DOSPTS ENTERO ID IGUAL IGUALIGUAL LINEANUEVA LLAVEC MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MODULO MULTIPLICACION PARA PARC POTENCIA PUNTO RAND RBOOLEAN RDEF RFALSE RFLOAT RINT RLIST RNOT RNULO ROR RPRINT RSTRING RTRUE TSTRUCTinit            : ls_instrinit            : emptyempty :ls_instr   : ls_instr instrls_instr   : instrinstr    : instruccion\n                | funcion_instr LLAVEC\n    PARAMETROS   : PARAMETROS COMA PARAMETROPARAMETROS   : PARAMETROPARAMETRO    : expresionPARAMETROSTIPO : PARAMETROSTIPO COMA PARAMETROTIPOPARAMETROSTIPO : PARAMETROTIPOPARAMETROTIPO : ID DOSPTS TIPO\n                    | ID DOSPTS ID\n                    | IDinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr\n                        | declaracion_instr\n                        | llamada_instr\n    imprimir_instr     : RPRINT PARA PARAMETROS PARCdeclaracion_instr :  ID IGUAL expresiondeclaracion_instr : ID DOSPTS TIPO IGUAL expresionfuncion_instr :  RDEF ID PARA PARC DOSPTS instrucciones\n                    | RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instruccionesllamada_instr : ID PARA PARC\n                    | ID PARA PARAMETROS PARCLISTA : CORCHA PARAMETROS CORCHCACCESOLISTA : ACCESOLISTA ITEMLISTAACCESOLISTA : ITEMLISTAITEMLISTA : CORCHA expresion CORCHCTIPO : RINT\n            | RFLOAT\n            | RBOOLEAN\n            | RSTRING\n            | IDexpresion     : expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion MULTIPLICACION expresion\n                    | expresion DIVISION expresion\n                    | expresion POTENCIA expresion\n                    | expresion MODULO expresion\n                    expresion    : expresion MAYORQUE expresion\n                    | expresion MENORQUE expresion\n                    | expresion MAYORIGUAL expresion\n                    | expresion MENORIGUAL expresion\n                    | expresion IGUALIGUAL expresion\n                    | expresion DIFERENTE expresionexpresion    : expresion RAND expresion\n                    | expresion ROR expresionexpresion      : RNOT expresion %prec UNOTexpresion      : MENOS expresion %prec UMENOSexpresion      : PARA expresion PARCexpresion      : ENTEROexpresion      : DECIMALexpresion      : CADENAexpresion      : IDexpresion    : RTRUE\n                    | RFALSE\n                    | RNULOexpresion :    LISTAexpresion : ID ACCESOLISTA'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,8,9,13,14,21,22,26,27,28,29,30,31,32,40,49,50,66,67,71,73,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-3,0,-1,-2,-5,-6,-18,-19,-20,-4,-7,-57,-22,-54,-55,-56,-58,-59,-60,-61,-26,-62,-30,-52,-51,-27,-21,-29,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-23,-31,]),'RDEF':([0,2,4,5,7,8,9,13,14,21,22,26,27,28,29,30,31,32,40,49,50,66,67,71,73,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[10,10,-5,-6,-18,-19,-20,-4,-7,-57,-22,-54,-55,-56,-58,-59,-60,-61,-26,-62,-30,-52,-51,-27,-21,-29,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-23,-31,]),'RPRINT':([0,2,4,5,7,8,9,13,14,21,22,26,27,28,29,30,31,32,40,49,50,66,67,71,73,75,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,102,104,105,106,],[12,12,-5,-6,-18,-19,-20,-4,-7,-57,-22,-54,-55,-56,-58,-59,-60,-61,-26,-62,-30,-52,-51,-27,-21,12,-29,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-23,12,-17,12,-31,-16,12,]),'ID':([0,2,4,5,7,8,9,10,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,40,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,71,72,73,74,75,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,102,104,105,106,],[11,11,-5,-6,-18,-19,-20,15,-4,-7,21,34,21,21,45,-57,-22,21,21,21,-54,-55,-56,-58,-59,-60,-61,21,-26,-62,-30,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-52,-51,21,-27,21,-21,98,11,45,-29,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-23,11,-17,11,-31,-16,11,]),'LLAVEC':([6,7,8,9,21,22,26,27,28,29,30,31,32,40,49,50,66,67,71,73,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,104,105,106,],[14,-18,-19,-20,-57,-22,-54,-55,-56,-58,-59,-60,-61,-26,-62,-30,-52,-51,-27,-21,-29,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-23,-24,-17,-31,-16,-25,]),'IGUAL':([11,34,35,36,37,38,39,],[16,-36,70,-32,-33,-34,-35,]),'DOSPTS':([11,45,46,76,],[17,74,75,102,]),'PARA':([11,12,15,16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[18,19,20,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'RNOT':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'MENOS':([16,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,43,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,72,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[23,23,23,-57,53,23,23,23,-54,-55,-56,-58,-59,-60,-61,23,53,-62,-30,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-52,53,53,23,23,-29,53,-37,-38,-39,-40,-41,-42,53,53,53,53,53,53,53,53,-53,-28,53,-31,]),'ENTERO':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'DECIMAL':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'CADENA':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'RTRUE':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'RFALSE':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'RNULO':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'CORCHA':([16,18,19,21,23,24,25,33,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,78,104,],[33,33,33,51,33,33,33,33,51,-30,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-29,-31,]),'RINT':([17,74,],[36,36,]),'RFLOAT':([17,74,],[37,37,]),'RBOOLEAN':([17,74,],[38,38,]),'RSTRING':([17,74,],[39,39,]),'PARC':([18,20,21,26,27,28,29,30,31,32,36,37,38,39,41,42,43,44,45,47,48,49,50,66,67,68,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,103,104,],[40,46,-57,-54,-55,-56,-58,-59,-60,-61,-32,-33,-34,-35,71,-9,-10,73,-15,76,-12,-62,-30,-52,-51,94,-29,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-8,-14,-13,-11,-31,]),'MAS':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,52,-54,-55,-56,-58,-59,-60,-61,52,-62,-30,-52,52,52,-29,52,-37,-38,-39,-40,-41,-42,52,52,52,52,52,52,52,52,-53,-28,52,-31,]),'MULTIPLICACION':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,54,-54,-55,-56,-58,-59,-60,-61,54,-62,-30,-52,54,54,-29,54,54,54,-39,-40,-41,-42,54,54,54,54,54,54,54,54,-53,-28,54,-31,]),'DIVISION':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,55,-54,-55,-56,-58,-59,-60,-61,55,-62,-30,-52,55,55,-29,55,55,55,-39,-40,-41,-42,55,55,55,55,55,55,55,55,-53,-28,55,-31,]),'POTENCIA':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,56,-54,-55,-56,-58,-59,-60,-61,56,-62,-30,-52,56,56,-29,56,56,56,56,56,-41,56,56,56,56,56,56,56,56,56,-53,-28,56,-31,]),'MODULO':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,57,-54,-55,-56,-58,-59,-60,-61,57,-62,-30,-52,57,57,-29,57,57,57,-39,-40,-41,-42,57,57,57,57,57,57,57,57,-53,-28,57,-31,]),'MAYORQUE':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,58,-54,-55,-56,-58,-59,-60,-61,58,-62,-30,-52,58,58,-29,58,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,58,58,-53,-28,58,-31,]),'MENORQUE':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,59,-54,-55,-56,-58,-59,-60,-61,59,-62,-30,-52,59,59,-29,59,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,59,59,-53,-28,59,-31,]),'MAYORIGUAL':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,60,-54,-55,-56,-58,-59,-60,-61,60,-62,-30,-52,60,60,-29,60,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,60,60,-53,-28,60,-31,]),'MENORIGUAL':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,61,-54,-55,-56,-58,-59,-60,-61,61,-62,-30,-52,61,61,-29,61,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,61,61,-53,-28,61,-31,]),'IGUALIGUAL':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,62,-54,-55,-56,-58,-59,-60,-61,62,-62,-30,-52,62,62,-29,62,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,62,62,-53,-28,62,-31,]),'DIFERENTE':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,63,-54,-55,-56,-58,-59,-60,-61,63,-62,-30,-52,63,63,-29,63,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,63,63,-53,-28,63,-31,]),'RAND':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,64,-54,-55,-56,-58,-59,-60,-61,64,-62,-30,-52,-51,64,-29,64,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,64,-53,-28,64,-31,]),'ROR':([21,22,26,27,28,29,30,31,32,43,49,50,66,67,68,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,104,],[-57,65,-54,-55,-56,-58,-59,-60,-61,65,-62,-30,-52,-51,65,-29,65,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,65,-31,]),'COMA':([21,26,27,28,29,30,31,32,36,37,38,39,41,42,43,44,45,47,48,49,50,66,67,69,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,103,104,],[-57,-54,-55,-56,-58,-59,-60,-61,-32,-33,-34,-35,72,-9,-10,72,-15,77,-12,-62,-30,-52,-51,72,-29,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-8,-14,-13,-11,-31,]),'CORCHC':([21,26,27,28,29,30,31,32,42,43,49,50,66,67,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,104,],[-57,-54,-55,-56,-58,-59,-60,-61,-9,-10,-62,-30,-52,-51,95,-29,104,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-53,-28,-8,-31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'ls_instr':([0,],[2,]),'empty':([0,],[3,]),'instr':([0,2,],[4,13,]),'instruccion':([0,2,75,100,102,106,],[5,5,101,105,101,105,]),'funcion_instr':([0,2,],[6,6,]),'imprimir_instr':([0,2,75,100,102,106,],[7,7,7,7,7,7,]),'declaracion_instr':([0,2,75,100,102,106,],[8,8,8,8,8,8,]),'llamada_instr':([0,2,75,100,102,106,],[9,9,9,9,9,9,]),'expresion':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[22,43,43,66,67,68,43,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,43,]),'LISTA':([16,18,19,23,24,25,33,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,70,72,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'TIPO':([17,74,],[35,99,]),'PARAMETROS':([18,19,33,],[41,44,69,]),'PARAMETRO':([18,19,33,72,],[42,42,42,97,]),'PARAMETROSTIPO':([20,],[47,]),'PARAMETROTIPO':([20,77,],[48,103,]),'ACCESOLISTA':([21,],[49,]),'ITEMLISTA':([21,49,],[50,78,]),'instrucciones':([75,102,],[100,106,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> ls_instr','init',1,'p_init','gramatica.py',176),
  ('init -> empty','init',1,'p_init_empty','gramatica.py',180),
  ('empty -> <empty>','empty',0,'p_empty','gramatica.py',184),
  ('ls_instr -> ls_instr instr','ls_instr',2,'p_ls_instr','gramatica.py',188),
  ('ls_instr -> instr','ls_instr',1,'p_ls_instr2','gramatica.py',193),
  ('instr -> instruccion','instr',1,'p_instr_recib','gramatica.py',197),
  ('instr -> funcion_instr LLAVEC','instr',2,'p_instr_recib','gramatica.py',198),
  ('PARAMETROS -> PARAMETROS COMA PARAMETRO','PARAMETROS',3,'p_lista_parametros','gramatica.py',205),
  ('PARAMETROS -> PARAMETRO','PARAMETROS',1,'p_lista_parametro2','gramatica.py',210),
  ('PARAMETRO -> expresion','PARAMETRO',1,'p_parametro_v','gramatica.py',214),
  ('PARAMETROSTIPO -> PARAMETROSTIPO COMA PARAMETROTIPO','PARAMETROSTIPO',3,'p_parametros_tipo','gramatica.py',218),
  ('PARAMETROSTIPO -> PARAMETROTIPO','PARAMETROSTIPO',1,'p_parametro_tipo','gramatica.py',223),
  ('PARAMETROTIPO -> ID DOSPTS TIPO','PARAMETROTIPO',3,'p_parametro_tipo_id','gramatica.py',227),
  ('PARAMETROTIPO -> ID DOSPTS ID','PARAMETROTIPO',3,'p_parametro_tipo_id','gramatica.py',228),
  ('PARAMETROTIPO -> ID','PARAMETROTIPO',1,'p_parametro_tipo_id','gramatica.py',229),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','gramatica.py',237),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',243),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',250),
  ('instruccion -> declaracion_instr','instruccion',1,'p_instruccion','gramatica.py',251),
  ('instruccion -> llamada_instr','instruccion',1,'p_instruccion','gramatica.py',252),
  ('imprimir_instr -> RPRINT PARA PARAMETROS PARC','imprimir_instr',4,'p_imprimir','gramatica.py',258),
  ('declaracion_instr -> ID IGUAL expresion','declaracion_instr',3,'p_declaracion','gramatica.py',263),
  ('declaracion_instr -> ID DOSPTS TIPO IGUAL expresion','declaracion_instr',5,'p_declaracion2','gramatica.py',267),
  ('funcion_instr -> RDEF ID PARA PARC DOSPTS instrucciones','funcion_instr',6,'p_funciones','gramatica.py',272),
  ('funcion_instr -> RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instrucciones','funcion_instr',7,'p_funciones','gramatica.py',273),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada_instr','gramatica.py',282),
  ('llamada_instr -> ID PARA PARAMETROS PARC','llamada_instr',4,'p_llamada_instr','gramatica.py',283),
  ('LISTA -> CORCHA PARAMETROS CORCHC','LISTA',3,'p_listas','gramatica.py',291),
  ('ACCESOLISTA -> ACCESOLISTA ITEMLISTA','ACCESOLISTA',2,'p_acceso_lista','gramatica.py',296),
  ('ACCESOLISTA -> ITEMLISTA','ACCESOLISTA',1,'p_acceso_lista2','gramatica.py',301),
  ('ITEMLISTA -> CORCHA expresion CORCHC','ITEMLISTA',3,'p_item_lista','gramatica.py',305),
  ('TIPO -> RINT','TIPO',1,'p_tipo','gramatica.py',310),
  ('TIPO -> RFLOAT','TIPO',1,'p_tipo','gramatica.py',311),
  ('TIPO -> RBOOLEAN','TIPO',1,'p_tipo','gramatica.py',312),
  ('TIPO -> RSTRING','TIPO',1,'p_tipo','gramatica.py',313),
  ('TIPO -> ID','TIPO',1,'p_tipo','gramatica.py',314),
  ('expresion -> expresion MAS expresion','expresion',3,'p_aritmeticas','gramatica.py',330),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_aritmeticas','gramatica.py',331),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_aritmeticas','gramatica.py',332),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_aritmeticas','gramatica.py',333),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_aritmeticas','gramatica.py',334),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_aritmeticas','gramatica.py',335),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_relacionales','gramatica.py',352),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_relacionales','gramatica.py',353),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',354),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',355),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',356),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_relacionales','gramatica.py',357),
  ('expresion -> expresion RAND expresion','expresion',3,'p_logicas','gramatica.py',376),
  ('expresion -> expresion ROR expresion','expresion',3,'p_logicas','gramatica.py',377),
  ('expresion -> RNOT expresion','expresion',2,'p_expre_not','gramatica.py',384),
  ('expresion -> MENOS expresion','expresion',2,'p_negacion','gramatica.py',389),
  ('expresion -> PARA expresion PARC','expresion',3,'p_parentesis','gramatica.py',394),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','gramatica.py',399),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','gramatica.py',403),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',407),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',411),
  ('expresion -> RTRUE','expresion',1,'p_expresion_bool','gramatica.py',415),
  ('expresion -> RFALSE','expresion',1,'p_expresion_bool','gramatica.py',416),
  ('expresion -> RNULO','expresion',1,'p_expresion_bool','gramatica.py',417),
  ('expresion -> LISTA','expresion',1,'p_expresion_lista','gramatica.py',427),
  ('expresion -> ID ACCESOLISTA','expresion',2,'p_expresion_accesolst','gramatica.py',431),
]
