
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftRORleftRANDrightUNOTleftMENORQUEMAYORQUEMENORIGUALMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOleftPOTENCIArightUMENOSleftPUNTOCADENA COMA CORCHA CORCHC DECIMAL DIFERENTE DIVISION DOSPTS ENTERO ID IGUAL IGUALIGUAL LINEANUEVA LLAVEC MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MODULO MULTIPLICACION PARA PARC POTENCIA PUNTO RAND RBOOLEAN RDEF RFALSE RFLOAT RINT RLIST RNOT RNULO ROR RPRINT RSTRING RTRUE TSTRUCTinit            : ls_instrinit            : emptyempty :ls_instr   : ls_instr instrls_instr   : instrinstr    : instruccion\n                | funcion_instr LLAVEC\n    PARAMETROS   : PARAMETROS COMA PARAMETROPARAMETROS   : PARAMETROPARAMETRO    : expresionPARAMETROSTIPO : PARAMETROSTIPO COMA PARAMETROTIPOPARAMETROSTIPO : PARAMETROTIPOPARAMETROTIPO : ID DOSPTS TIPO\n                    | ID DOSPTS ID\n                    | IDinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr\n                        | declaracion_instr\n                        | llamada_instr\n    imprimir_instr     : RPRINT PARA PARAMETROS PARCdeclaracion_instr :  ID IGUAL expresiondeclaracion_instr : ID DOSPTS TIPO IGUAL expresiondeclaracion_instr : ID ACCESOLISTA IGUAL expresionfuncion_instr :  RDEF ID PARA PARC DOSPTS instrucciones\n                    | RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instruccionesllamada_instr : ID PARA PARC\n                    | ID PARA PARAMETROS PARCLISTA : CORCHA PARAMETROS CORCHCACCESOLISTA : ACCESOLISTA ITEMLISTAACCESOLISTA : ITEMLISTAITEMLISTA : CORCHA expresion CORCHCTIPO : RINT\n            | RFLOAT\n            | RBOOLEAN\n            | RSTRING\n            | IDexpresion     : expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion MULTIPLICACION expresion\n                    | expresion DIVISION expresion\n                    | expresion POTENCIA expresion\n                    | expresion MODULO expresion\n                    expresion    : expresion MAYORQUE expresion\n                    | expresion MENORQUE expresion\n                    | expresion MAYORIGUAL expresion\n                    | expresion MENORIGUAL expresion\n                    | expresion IGUALIGUAL expresion\n                    | expresion DIFERENTE expresionexpresion    : expresion RAND expresion\n                    | expresion ROR expresionexpresion      : RNOT expresion %prec UNOTexpresion      : MENOS expresion %prec UMENOSexpresion      : PARA expresion PARCexpresion      : ENTEROexpresion      : DECIMALexpresion      : CADENAexpresion      : IDexpresion    : RTRUE\n                    | RFALSE\n                    | RNULOexpresion :    LISTAexpresion : ID ACCESOLISTA'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,8,9,13,14,20,24,25,29,30,31,32,33,34,35,44,45,55,70,71,75,76,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-3,0,-1,-2,-5,-6,-18,-19,-20,-4,-7,-31,-58,-22,-55,-56,-57,-59,-60,-61,-62,-30,-27,-63,-53,-52,-24,-28,-32,-21,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-23,]),'RDEF':([0,2,4,5,7,8,9,13,14,20,24,25,29,30,31,32,33,34,35,44,45,55,70,71,75,76,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[10,10,-5,-6,-18,-19,-20,-4,-7,-31,-58,-22,-55,-56,-57,-59,-60,-61,-62,-30,-27,-63,-53,-52,-24,-28,-32,-21,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-23,]),'RPRINT':([0,2,4,5,7,8,9,13,14,20,24,25,29,30,31,32,33,34,35,44,45,55,70,71,75,76,78,79,81,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,104,105,106,108,109,],[12,12,-5,-6,-18,-19,-20,-4,-7,-31,-58,-22,-55,-56,-57,-59,-60,-61,-62,-30,-27,-63,-53,-52,-24,-28,-32,-21,12,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-23,12,-17,12,-16,12,]),'ID':([0,2,4,5,7,8,9,10,13,14,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,43,44,45,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,74,75,76,77,78,79,80,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,104,105,106,108,109,],[11,11,-5,-6,-18,-19,-20,15,-4,-7,24,37,24,-31,24,24,51,-58,-22,24,24,24,-55,-56,-57,-59,-60,-61,-62,24,24,-30,-27,-63,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-53,-52,24,-24,-28,24,-32,-21,102,11,51,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-23,11,-17,11,-16,11,]),'LLAVEC':([6,7,8,9,20,24,25,29,30,31,32,33,34,35,44,45,55,70,71,75,76,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,104,105,108,109,],[14,-18,-19,-20,-31,-58,-22,-55,-56,-57,-59,-60,-61,-62,-30,-27,-63,-53,-52,-24,-28,-32,-21,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-23,-25,-17,-16,-26,]),'IGUAL':([11,18,20,37,38,39,40,41,42,44,78,],[16,43,-31,-37,74,-33,-34,-35,-36,-30,-32,]),'DOSPTS':([11,51,52,82,],[17,80,81,106,]),'PARA':([11,12,15,16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[19,22,23,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'CORCHA':([11,16,18,19,20,21,22,24,26,27,28,36,43,44,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,78,],[21,36,21,36,-31,36,36,21,36,36,36,36,36,-30,21,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-32,]),'RNOT':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'MENOS':([16,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,43,44,48,49,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,74,75,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[26,26,-31,26,26,-58,57,26,26,26,-55,-56,-57,-59,-60,-61,-62,26,26,-30,57,57,-63,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-53,57,57,26,57,26,-32,-38,-39,-40,-41,-42,-43,57,57,57,57,57,57,57,57,-54,-29,57,]),'ENTERO':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'DECIMAL':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'CADENA':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'RTRUE':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'RFALSE':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'RNULO':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'RINT':([17,80,],[39,39,]),'RFLOAT':([17,80,],[40,40,]),'RBOOLEAN':([17,80,],[41,41,]),'RSTRING':([17,80,],[42,42,]),'PARC':([19,20,23,24,29,30,31,32,33,34,35,39,40,41,42,44,46,47,48,50,51,53,54,55,70,71,72,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,107,],[45,-31,52,-58,-55,-56,-57,-59,-60,-61,-62,-33,-34,-35,-36,-30,76,-9,-10,79,-15,82,-12,-63,-53,-52,98,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-8,-14,-13,-11,]),'MAS':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,56,-55,-56,-57,-59,-60,-61,-62,-30,56,56,-63,-53,56,56,56,-32,-38,-39,-40,-41,-42,-43,56,56,56,56,56,56,56,56,-54,-29,56,]),'MULTIPLICACION':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,58,-55,-56,-57,-59,-60,-61,-62,-30,58,58,-63,-53,58,58,58,-32,58,58,-40,-41,-42,-43,58,58,58,58,58,58,58,58,-54,-29,58,]),'DIVISION':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,59,-55,-56,-57,-59,-60,-61,-62,-30,59,59,-63,-53,59,59,59,-32,59,59,-40,-41,-42,-43,59,59,59,59,59,59,59,59,-54,-29,59,]),'POTENCIA':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,60,-55,-56,-57,-59,-60,-61,-62,-30,60,60,-63,-53,60,60,60,-32,60,60,60,60,-42,60,60,60,60,60,60,60,60,60,-54,-29,60,]),'MODULO':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,61,-55,-56,-57,-59,-60,-61,-62,-30,61,61,-63,-53,61,61,61,-32,61,61,-40,-41,-42,-43,61,61,61,61,61,61,61,61,-54,-29,61,]),'MAYORQUE':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,62,-55,-56,-57,-59,-60,-61,-62,-30,62,62,-63,-53,62,62,62,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,62,62,-54,-29,62,]),'MENORQUE':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,63,-55,-56,-57,-59,-60,-61,-62,-30,63,63,-63,-53,63,63,63,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,63,63,-54,-29,63,]),'MAYORIGUAL':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,64,-55,-56,-57,-59,-60,-61,-62,-30,64,64,-63,-53,64,64,64,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,64,64,-54,-29,64,]),'MENORIGUAL':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,65,-55,-56,-57,-59,-60,-61,-62,-30,65,65,-63,-53,65,65,65,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,65,65,-54,-29,65,]),'IGUALIGUAL':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,66,-55,-56,-57,-59,-60,-61,-62,-30,66,66,-63,-53,66,66,66,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,66,66,-54,-29,66,]),'DIFERENTE':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,67,-55,-56,-57,-59,-60,-61,-62,-30,67,67,-63,-53,67,67,67,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,67,67,-54,-29,67,]),'RAND':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,68,-55,-56,-57,-59,-60,-61,-62,-30,68,68,-63,-53,-52,68,68,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,68,-54,-29,68,]),'ROR':([20,24,25,29,30,31,32,33,34,35,44,48,49,55,70,71,72,75,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-31,-58,69,-55,-56,-57,-59,-60,-61,-62,-30,69,69,-63,-53,-52,69,69,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,69,]),'COMA':([20,24,29,30,31,32,33,34,35,39,40,41,42,44,46,47,48,50,51,53,54,55,70,71,73,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,101,102,103,107,],[-31,-58,-55,-56,-57,-59,-60,-61,-62,-33,-34,-35,-36,-30,77,-9,-10,77,-15,83,-12,-63,-53,-52,77,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-8,-14,-13,-11,]),'CORCHC':([20,24,29,30,31,32,33,34,35,44,47,48,49,55,70,71,73,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,101,],[-31,-58,-55,-56,-57,-59,-60,-61,-62,-30,-9,-10,78,-63,-53,-52,99,-32,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-54,-29,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'ls_instr':([0,],[2,]),'empty':([0,],[3,]),'instr':([0,2,],[4,13,]),'instruccion':([0,2,81,104,106,109,],[5,5,105,108,105,108,]),'funcion_instr':([0,2,],[6,6,]),'imprimir_instr':([0,2,81,104,106,109,],[7,7,7,7,7,7,]),'declaracion_instr':([0,2,81,104,106,109,],[8,8,8,8,8,8,]),'llamada_instr':([0,2,81,104,106,109,],[9,9,9,9,9,9,]),'ACCESOLISTA':([11,24,],[18,55,]),'ITEMLISTA':([11,18,24,55,],[20,44,20,44,]),'expresion':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[25,48,49,48,70,71,72,48,75,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,48,]),'LISTA':([16,19,21,22,26,27,28,36,43,56,57,58,59,60,61,62,63,64,65,66,67,68,69,74,77,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TIPO':([17,80,],[38,103,]),'PARAMETROS':([19,22,36,],[46,50,73,]),'PARAMETRO':([19,22,36,77,],[47,47,47,101,]),'PARAMETROSTIPO':([23,],[53,]),'PARAMETROTIPO':([23,83,],[54,107,]),'instrucciones':([81,106,],[104,109,]),}

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
  ('declaracion_instr -> ID ACCESOLISTA IGUAL expresion','declaracion_instr',4,'p_declaracion3','gramatica.py',271),
  ('funcion_instr -> RDEF ID PARA PARC DOSPTS instrucciones','funcion_instr',6,'p_funciones','gramatica.py',276),
  ('funcion_instr -> RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instrucciones','funcion_instr',7,'p_funciones','gramatica.py',277),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada_instr','gramatica.py',286),
  ('llamada_instr -> ID PARA PARAMETROS PARC','llamada_instr',4,'p_llamada_instr','gramatica.py',287),
  ('LISTA -> CORCHA PARAMETROS CORCHC','LISTA',3,'p_listas','gramatica.py',295),
  ('ACCESOLISTA -> ACCESOLISTA ITEMLISTA','ACCESOLISTA',2,'p_acceso_lista','gramatica.py',300),
  ('ACCESOLISTA -> ITEMLISTA','ACCESOLISTA',1,'p_acceso_lista2','gramatica.py',305),
  ('ITEMLISTA -> CORCHA expresion CORCHC','ITEMLISTA',3,'p_item_lista','gramatica.py',309),
  ('TIPO -> RINT','TIPO',1,'p_tipo','gramatica.py',314),
  ('TIPO -> RFLOAT','TIPO',1,'p_tipo','gramatica.py',315),
  ('TIPO -> RBOOLEAN','TIPO',1,'p_tipo','gramatica.py',316),
  ('TIPO -> RSTRING','TIPO',1,'p_tipo','gramatica.py',317),
  ('TIPO -> ID','TIPO',1,'p_tipo','gramatica.py',318),
  ('expresion -> expresion MAS expresion','expresion',3,'p_aritmeticas','gramatica.py',334),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_aritmeticas','gramatica.py',335),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_aritmeticas','gramatica.py',336),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_aritmeticas','gramatica.py',337),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_aritmeticas','gramatica.py',338),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_aritmeticas','gramatica.py',339),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_relacionales','gramatica.py',356),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_relacionales','gramatica.py',357),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',358),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',359),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',360),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_relacionales','gramatica.py',361),
  ('expresion -> expresion RAND expresion','expresion',3,'p_logicas','gramatica.py',380),
  ('expresion -> expresion ROR expresion','expresion',3,'p_logicas','gramatica.py',381),
  ('expresion -> RNOT expresion','expresion',2,'p_expre_not','gramatica.py',388),
  ('expresion -> MENOS expresion','expresion',2,'p_negacion','gramatica.py',393),
  ('expresion -> PARA expresion PARC','expresion',3,'p_parentesis','gramatica.py',398),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','gramatica.py',403),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','gramatica.py',407),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',411),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',415),
  ('expresion -> RTRUE','expresion',1,'p_expresion_bool','gramatica.py',419),
  ('expresion -> RFALSE','expresion',1,'p_expresion_bool','gramatica.py',420),
  ('expresion -> RNULO','expresion',1,'p_expresion_bool','gramatica.py',421),
  ('expresion -> LISTA','expresion',1,'p_expresion_lista','gramatica.py',431),
  ('expresion -> ID ACCESOLISTA','expresion',2,'p_expresion_accesolst','gramatica.py',435),
]
