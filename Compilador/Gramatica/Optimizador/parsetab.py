
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA DISTINT DIV EQUALS EQUALSEQUALS FLOAT64 FLOATLITERAL FMT FUNC GOTO GREATER GREATEREQUAL ID IF IMPORT INT INTLITERAL LECOR LEKEY LEPAR LESS LESSEQUAL MINUS PACKAGE PLUS POINT PRINTF RETURN RICOR RIKEY RIPAR SEMICOLON STRINGLITERAL TIMES VAR\n    start : PACKAGE ID fin_inst IMPORT LEPAR package_list RIPAR fin_inst declarations codeList\n    declarations : declarations declaration\n    | declaration\n    package_list        : package_list STRINGLITERAL\n                        | STRINGLITERAL\n    \n    fin_inst            : SEMICOLON\n                        |\n    declaration :     VAR idList LECOR INTLITERAL RICOR FLOAT64 SEMICOLON\n    |   VAR idList type SEMICOLONtype : INT\n    | FLOAT64idList :   idList COMMA ID\n    | IDcodeList : codeList code\n    | codecode : FUNC ID LEPAR RIPAR statementstatement : LEKEY instructions RIKEYinstructions : instructions instruction\n    | instructioninstruction :  assign SEMICOLON\n    | print SEMICOLON\n    | if\n    | gotoSt SEMICOLON\n    | label\n    | callFunc SEMICOLON\n    | retSt SEMICOLONretSt : RETURNcallFunc : ID LEPAR RIPARlabel : ID COLONgotoSt : GOTO IDif : IF expression LEKEY GOTO ID SEMICOLON RIKEYassign : access EQUALS finalExpassign :   ID EQUALS expression\n    | ID EQUALS accessprint : FMT POINT PRINTF LEPAR STRINGLITERAL COMMA printValue RIPARprintValue :   INT LEPAR finalExp RIPAR\n    | finalExpexpression :   finalExp PLUS finalExp\n    | finalExp MINUS finalExp\n    | finalExp TIMES finalExp\n    | finalExp DIV finalExp\n    | finalExp GREATER finalExp\n    | finalExp LESS finalExp\n    | finalExp GREATEREQUAL finalExp\n    | finalExp LESSEQUAL finalExp\n    | finalExp EQUALSEQUALS finalExp\n    | finalExp DISTINT finalExp\n    | finalExpfinalExp : ID\n    | INTLITERAL\n    | MINUS INTLITERAL\n    | FLOATLITERALaccess :   ID LECOR INT LEPAR finalExp RIPAR RICOR\n    | ID LECOR finalExp RICOR'
    
_lr_action_items = {'PACKAGE':([0,],[2,]),'$end':([1,16,18,22,35,54,],[0,-1,-15,-14,-16,-17,]),'ID':([2,15,19,27,36,38,39,42,44,50,51,55,56,57,58,59,60,61,62,63,65,83,84,85,86,87,88,89,90,91,92,94,97,112,118,120,],[3,21,23,32,48,48,-19,-22,-24,68,73,-18,-20,-21,-23,-25,-26,68,75,-29,68,68,68,68,68,68,68,68,68,68,68,68,110,68,-31,68,]),'SEMICOLON':([3,10,25,26,28,37,40,41,43,45,46,52,68,69,71,72,73,74,75,76,77,78,93,95,98,99,100,101,102,103,104,105,106,107,110,114,119,],[5,5,-11,31,-10,53,56,57,58,59,60,-27,-49,-48,-50,-52,-30,-32,-49,-33,-34,-28,-51,-54,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,113,-53,-35,]),'IMPORT':([3,4,5,],[-7,6,-6,]),'VAR':([5,10,12,13,14,17,31,53,],[-6,-7,15,15,-3,-2,-9,-8,]),'LEPAR':([6,23,48,79,81,116,],[7,29,64,94,96,120,]),'STRINGLITERAL':([7,8,9,11,96,],[9,11,-5,-4,109,]),'RIPAR':([8,9,11,29,64,68,71,72,93,108,115,117,121,122,],[10,-5,-4,33,78,-49,-50,-52,-51,111,119,-37,122,-36,]),'FUNC':([13,14,16,17,18,22,31,35,53,54,],[19,-3,19,-2,-15,-14,-9,-16,-8,-17,]),'LECOR':([20,21,32,48,75,],[24,-13,-12,65,65,]),'COMMA':([20,21,32,109,],[27,-13,-12,112,]),'INT':([20,21,32,65,112,],[28,-13,-12,79,116,]),'FLOAT64':([20,21,32,34,],[25,-13,-12,37,]),'INTLITERAL':([24,50,61,62,65,70,83,84,85,86,87,88,89,90,91,92,94,112,120,],[30,71,71,71,71,93,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'RICOR':([30,68,71,72,80,93,111,],[34,-49,-50,-52,95,-51,114,]),'LEKEY':([33,67,68,69,71,72,93,98,99,100,101,102,103,104,105,106,107,],[36,82,-49,-48,-50,-52,-51,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,]),'FMT':([36,38,39,42,44,55,56,57,58,59,60,63,118,],[49,49,-19,-22,-24,-18,-20,-21,-23,-25,-26,-29,-31,]),'IF':([36,38,39,42,44,55,56,57,58,59,60,63,118,],[50,50,-19,-22,-24,-18,-20,-21,-23,-25,-26,-29,-31,]),'GOTO':([36,38,39,42,44,55,56,57,58,59,60,63,82,118,],[51,51,-19,-22,-24,-18,-20,-21,-23,-25,-26,-29,97,-31,]),'RETURN':([36,38,39,42,44,55,56,57,58,59,60,63,118,],[52,52,-19,-22,-24,-18,-20,-21,-23,-25,-26,-29,-31,]),'RIKEY':([38,39,42,44,55,56,57,58,59,60,63,113,118,],[54,-19,-22,-24,-18,-20,-21,-23,-25,-26,-29,118,-31,]),'EQUALS':([47,48,95,114,],[61,62,-54,-53,]),'COLON':([48,],[63,]),'POINT':([49,],[66,]),'MINUS':([50,61,62,65,68,69,71,72,75,83,84,85,86,87,88,89,90,91,92,93,94,112,120,],[70,70,70,70,-49,84,-50,-52,-49,70,70,70,70,70,70,70,70,70,70,-51,70,70,70,]),'FLOATLITERAL':([50,61,62,65,83,84,85,86,87,88,89,90,91,92,94,112,120,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'PRINTF':([66,],[81,]),'PLUS':([68,69,71,72,75,93,],[-49,83,-50,-52,-49,-51,]),'TIMES':([68,69,71,72,75,93,],[-49,85,-50,-52,-49,-51,]),'DIV':([68,69,71,72,75,93,],[-49,86,-50,-52,-49,-51,]),'GREATER':([68,69,71,72,75,93,],[-49,87,-50,-52,-49,-51,]),'LESS':([68,69,71,72,75,93,],[-49,88,-50,-52,-49,-51,]),'GREATEREQUAL':([68,69,71,72,75,93,],[-49,89,-50,-52,-49,-51,]),'LESSEQUAL':([68,69,71,72,75,93,],[-49,90,-50,-52,-49,-51,]),'EQUALSEQUALS':([68,69,71,72,75,93,],[-49,91,-50,-52,-49,-51,]),'DISTINT':([68,69,71,72,75,93,],[-49,92,-50,-52,-49,-51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'fin_inst':([3,10,],[4,12,]),'package_list':([7,],[8,]),'declarations':([12,],[13,]),'declaration':([12,13,],[14,17,]),'codeList':([13,],[16,]),'code':([13,16,],[18,22,]),'idList':([15,],[20,]),'type':([20,],[26,]),'statement':([33,],[35,]),'instructions':([36,],[38,]),'instruction':([36,38,],[39,55,]),'assign':([36,38,],[40,40,]),'print':([36,38,],[41,41,]),'if':([36,38,],[42,42,]),'gotoSt':([36,38,],[43,43,]),'label':([36,38,],[44,44,]),'callFunc':([36,38,],[45,45,]),'retSt':([36,38,],[46,46,]),'access':([36,38,62,],[47,47,77,]),'expression':([50,62,],[67,76,]),'finalExp':([50,61,62,65,83,84,85,86,87,88,89,90,91,92,94,112,120,],[69,74,69,80,98,99,100,101,102,103,104,105,106,107,108,117,121,]),'printValue':([112,],[115,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> PACKAGE ID fin_inst IMPORT LEPAR package_list RIPAR fin_inst declarations codeList','start',10,'p_start','optimizadorGramatica.py',152),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','optimizadorGramatica.py',158),
  ('declarations -> declaration','declarations',1,'p_declarations','optimizadorGramatica.py',159),
  ('package_list -> package_list STRINGLITERAL','package_list',2,'p_packages','optimizadorGramatica.py',169),
  ('package_list -> STRINGLITERAL','package_list',1,'p_packages','optimizadorGramatica.py',170),
  ('fin_inst -> SEMICOLON','fin_inst',1,'p_fin_inst','optimizadorGramatica.py',181),
  ('fin_inst -> <empty>','fin_inst',0,'p_fin_inst','optimizadorGramatica.py',182),
  ('declaration -> VAR idList LECOR INTLITERAL RICOR FLOAT64 SEMICOLON','declaration',7,'p_declaration','optimizadorGramatica.py',189),
  ('declaration -> VAR idList type SEMICOLON','declaration',4,'p_declaration','optimizadorGramatica.py',190),
  ('type -> INT','type',1,'p_type','optimizadorGramatica.py',198),
  ('type -> FLOAT64','type',1,'p_type','optimizadorGramatica.py',199),
  ('idList -> idList COMMA ID','idList',3,'p_idList','optimizadorGramatica.py',207),
  ('idList -> ID','idList',1,'p_idList','optimizadorGramatica.py',208),
  ('codeList -> codeList code','codeList',2,'p_codeList','optimizadorGramatica.py',216),
  ('codeList -> code','codeList',1,'p_codeList','optimizadorGramatica.py',217),
  ('code -> FUNC ID LEPAR RIPAR statement','code',5,'p_code','optimizadorGramatica.py',226),
  ('statement -> LEKEY instructions RIKEY','statement',3,'p_statement','optimizadorGramatica.py',231),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','optimizadorGramatica.py',236),
  ('instructions -> instruction','instructions',1,'p_instructions','optimizadorGramatica.py',237),
  ('instruction -> assign SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',246),
  ('instruction -> print SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',247),
  ('instruction -> if','instruction',1,'p_instruction','optimizadorGramatica.py',248),
  ('instruction -> gotoSt SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',249),
  ('instruction -> label','instruction',1,'p_instruction','optimizadorGramatica.py',250),
  ('instruction -> callFunc SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',251),
  ('instruction -> retSt SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',252),
  ('retSt -> RETURN','retSt',1,'p_return','optimizadorGramatica.py',257),
  ('callFunc -> ID LEPAR RIPAR','callFunc',3,'p_callFunc','optimizadorGramatica.py',262),
  ('label -> ID COLON','label',2,'p_label','optimizadorGramatica.py',267),
  ('gotoSt -> GOTO ID','gotoSt',2,'p_goto','optimizadorGramatica.py',272),
  ('if -> IF expression LEKEY GOTO ID SEMICOLON RIKEY','if',7,'p_if','optimizadorGramatica.py',277),
  ('assign -> access EQUALS finalExp','assign',3,'p_assign','optimizadorGramatica.py',282),
  ('assign -> ID EQUALS expression','assign',3,'p_assign2','optimizadorGramatica.py',287),
  ('assign -> ID EQUALS access','assign',3,'p_assign2','optimizadorGramatica.py',288),
  ('print -> FMT POINT PRINTF LEPAR STRINGLITERAL COMMA printValue RIPAR','print',8,'p_print','optimizadorGramatica.py',294),
  ('printValue -> INT LEPAR finalExp RIPAR','printValue',4,'p_printValue','optimizadorGramatica.py',299),
  ('printValue -> finalExp','printValue',1,'p_printValue','optimizadorGramatica.py',300),
  ('expression -> finalExp PLUS finalExp','expression',3,'p_expression','optimizadorGramatica.py',309),
  ('expression -> finalExp MINUS finalExp','expression',3,'p_expression','optimizadorGramatica.py',310),
  ('expression -> finalExp TIMES finalExp','expression',3,'p_expression','optimizadorGramatica.py',311),
  ('expression -> finalExp DIV finalExp','expression',3,'p_expression','optimizadorGramatica.py',312),
  ('expression -> finalExp GREATER finalExp','expression',3,'p_expression','optimizadorGramatica.py',313),
  ('expression -> finalExp LESS finalExp','expression',3,'p_expression','optimizadorGramatica.py',314),
  ('expression -> finalExp GREATEREQUAL finalExp','expression',3,'p_expression','optimizadorGramatica.py',315),
  ('expression -> finalExp LESSEQUAL finalExp','expression',3,'p_expression','optimizadorGramatica.py',316),
  ('expression -> finalExp EQUALSEQUALS finalExp','expression',3,'p_expression','optimizadorGramatica.py',317),
  ('expression -> finalExp DISTINT finalExp','expression',3,'p_expression','optimizadorGramatica.py',318),
  ('expression -> finalExp','expression',1,'p_expression','optimizadorGramatica.py',319),
  ('finalExp -> ID','finalExp',1,'p_finalExp','optimizadorGramatica.py',327),
  ('finalExp -> INTLITERAL','finalExp',1,'p_finalExp','optimizadorGramatica.py',328),
  ('finalExp -> MINUS INTLITERAL','finalExp',2,'p_finalExp','optimizadorGramatica.py',329),
  ('finalExp -> FLOATLITERAL','finalExp',1,'p_finalExp','optimizadorGramatica.py',330),
  ('access -> ID LECOR INT LEPAR finalExp RIPAR RICOR','access',7,'p_access','optimizadorGramatica.py',338),
  ('access -> ID LECOR finalExp RICOR','access',4,'p_access','optimizadorGramatica.py',339),
]
