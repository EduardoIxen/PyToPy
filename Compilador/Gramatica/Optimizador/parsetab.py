
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA DISTINT DIV EQUALS EQUALSEQUALS FLOAT64 FLOATLITERAL FMT FUNC GOTO GREATER GREATEREQUAL ID IF IMPORT INT INTLITERAL LECOR LEKEY LEPAR LESS LESSEQUAL MATH MINUS MOD PACKAGE PLUS POINT PRINTF RETURN RICOR RIKEY RIPAR SEMICOLON STRINGLITERAL TIMES VARstart :  PACKAGE ID SEMICOLON IMPORT LEPAR imports RIPAR SEMICOLON declarations codeListimports : imports STRINGLITERAL\n                | STRINGLITERALdeclarations : declarations declaration\n                    | declarationdeclaration :     VAR idList LECOR INTLITERAL RICOR FLOAT64 SEMICOLON\n                    |   VAR idList type SEMICOLONtype : INT\n            | FLOAT64idList :   idList COMMA ID\n                | IDcodeList : codeList code\n                | codecode : FUNC ID LEPAR RIPAR statementstatement : LEKEY instructions RIKEYinstructions : instructions instruction\n                    | instructioninstruction :  assign SEMICOLON\n                    | print SEMICOLON\n                    | if\n                    | gotoSt SEMICOLON\n                    | label\n                    | callFunc SEMICOLON\n                    | retSt SEMICOLONretSt : RETURNcallFunc : ID LEPAR RIPARlabel : ID COLONgotoSt : GOTO IDif : IF expression LEKEY GOTO ID SEMICOLON RIKEYassign : access EQUALS finalExpassign :   ID EQUALS expression\n                | ID EQUALS accessprint : FMT POINT PRINTF LEPAR STRINGLITERAL COMMA printValue RIPARprintValue :   INT LEPAR finalExp RIPAR\n                    | finalExpexpression :   finalExp PLUS finalExp\n                    | finalExp MINUS finalExp\n                    | finalExp TIMES finalExp\n                    | finalExp DIV finalExp\n                    | finalExp GREATER finalExp\n                    | finalExp LESS finalExp\n                    | finalExp GREATEREQUAL finalExp\n                    | finalExp LESSEQUAL finalExp\n                    | finalExp EQUALSEQUALS finalExp\n                    | finalExp DISTINT finalExp\n                    | MATH POINT MOD LEPAR finalExp COMMA finalExp RIPAR\n                    | finalExpfinalExp : ID\n                | INTLITERAL\n                | MINUS INTLITERAL\n                | FLOATLITERALaccess :   ID LECOR INT LEPAR finalExp RIPAR RICOR\n                | ID LECOR finalExp RICOR'
    
_lr_action_items = {'PACKAGE':([0,],[2,]),'$end':([1,15,17,21,34,53,],[0,-1,-13,-12,-14,-15,]),'ID':([2,14,18,26,35,37,38,41,43,49,50,54,55,56,57,58,59,60,61,62,64,83,84,85,86,87,88,89,90,91,92,95,98,113,115,122,123,125,],[3,20,22,31,47,47,-17,-20,-22,67,73,-16,-18,-19,-21,-23,-24,67,75,-27,67,67,67,67,67,67,67,67,67,67,67,67,112,67,67,-29,67,67,]),'SEMICOLON':([3,9,24,25,27,36,39,40,42,44,45,51,67,68,71,72,73,74,75,76,77,78,93,96,99,100,101,102,103,104,105,106,107,108,112,118,124,128,],[4,11,-9,30,-8,52,55,56,57,58,59,-25,-48,-47,-49,-51,-28,-30,-48,-31,-32,-26,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,116,-52,-33,-46,]),'IMPORT':([4,],[5,]),'LEPAR':([5,22,47,79,81,109,120,],[6,28,63,95,97,113,125,]),'STRINGLITERAL':([6,7,8,10,97,],[8,10,-3,-2,111,]),'RIPAR':([7,8,10,28,63,67,71,72,93,110,119,121,126,127,129,],[9,-3,-2,32,78,-48,-49,-51,-50,114,124,-35,128,129,-34,]),'VAR':([11,12,13,16,30,52,],[14,14,-5,-4,-7,-6,]),'FUNC':([12,13,15,16,17,21,30,34,52,53,],[18,-5,18,-4,-13,-12,-7,-14,-6,-15,]),'LECOR':([19,20,31,47,75,],[23,-11,-10,64,64,]),'COMMA':([19,20,31,67,71,72,93,111,117,],[26,-11,-10,-48,-49,-51,-50,115,123,]),'INT':([19,20,31,64,115,],[27,-11,-10,79,120,]),'FLOAT64':([19,20,31,33,],[24,-11,-10,36,]),'INTLITERAL':([23,49,60,61,64,69,83,84,85,86,87,88,89,90,91,92,95,113,115,123,125,],[29,71,71,71,71,93,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'RICOR':([29,67,71,72,80,93,114,],[33,-48,-49,-51,96,-50,118,]),'LEKEY':([32,66,67,68,71,72,93,99,100,101,102,103,104,105,106,107,108,128,],[35,82,-48,-47,-49,-51,-50,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,]),'FMT':([35,37,38,41,43,54,55,56,57,58,59,62,122,],[48,48,-17,-20,-22,-16,-18,-19,-21,-23,-24,-27,-29,]),'IF':([35,37,38,41,43,54,55,56,57,58,59,62,122,],[49,49,-17,-20,-22,-16,-18,-19,-21,-23,-24,-27,-29,]),'GOTO':([35,37,38,41,43,54,55,56,57,58,59,62,82,122,],[50,50,-17,-20,-22,-16,-18,-19,-21,-23,-24,-27,98,-29,]),'RETURN':([35,37,38,41,43,54,55,56,57,58,59,62,122,],[51,51,-17,-20,-22,-16,-18,-19,-21,-23,-24,-27,-29,]),'RIKEY':([37,38,41,43,54,55,56,57,58,59,62,116,122,],[53,-17,-20,-22,-16,-18,-19,-21,-23,-24,-27,122,-29,]),'EQUALS':([46,47,96,118,],[60,61,-53,-52,]),'COLON':([47,],[62,]),'POINT':([48,70,],[65,94,]),'MATH':([49,61,],[70,70,]),'MINUS':([49,60,61,64,67,68,71,72,75,83,84,85,86,87,88,89,90,91,92,93,95,113,115,123,125,],[69,69,69,69,-48,84,-49,-51,-48,69,69,69,69,69,69,69,69,69,69,-50,69,69,69,69,69,]),'FLOATLITERAL':([49,60,61,64,83,84,85,86,87,88,89,90,91,92,95,113,115,123,125,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'PRINTF':([65,],[81,]),'PLUS':([67,68,71,72,75,93,],[-48,83,-49,-51,-48,-50,]),'TIMES':([67,68,71,72,75,93,],[-48,85,-49,-51,-48,-50,]),'DIV':([67,68,71,72,75,93,],[-48,86,-49,-51,-48,-50,]),'GREATER':([67,68,71,72,75,93,],[-48,87,-49,-51,-48,-50,]),'LESS':([67,68,71,72,75,93,],[-48,88,-49,-51,-48,-50,]),'GREATEREQUAL':([67,68,71,72,75,93,],[-48,89,-49,-51,-48,-50,]),'LESSEQUAL':([67,68,71,72,75,93,],[-48,90,-49,-51,-48,-50,]),'EQUALSEQUALS':([67,68,71,72,75,93,],[-48,91,-49,-51,-48,-50,]),'DISTINT':([67,68,71,72,75,93,],[-48,92,-49,-51,-48,-50,]),'MOD':([94,],[109,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'imports':([6,],[7,]),'declarations':([11,],[12,]),'declaration':([11,12,],[13,16,]),'codeList':([12,],[15,]),'code':([12,15,],[17,21,]),'idList':([14,],[19,]),'type':([19,],[25,]),'statement':([32,],[34,]),'instructions':([35,],[37,]),'instruction':([35,37,],[38,54,]),'assign':([35,37,],[39,39,]),'print':([35,37,],[40,40,]),'if':([35,37,],[41,41,]),'gotoSt':([35,37,],[42,42,]),'label':([35,37,],[43,43,]),'callFunc':([35,37,],[44,44,]),'retSt':([35,37,],[45,45,]),'access':([35,37,61,],[46,46,77,]),'expression':([49,61,],[66,76,]),'finalExp':([49,60,61,64,83,84,85,86,87,88,89,90,91,92,95,113,115,123,125,],[68,74,68,80,99,100,101,102,103,104,105,106,107,108,110,117,121,126,127,]),'printValue':([115,],[119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> PACKAGE ID SEMICOLON IMPORT LEPAR imports RIPAR SEMICOLON declarations codeList','start',10,'p_start','optimizadorGramatica.py',160),
  ('imports -> imports STRINGLITERAL','imports',2,'p_imports','optimizadorGramatica.py',165),
  ('imports -> STRINGLITERAL','imports',1,'p_imports','optimizadorGramatica.py',166),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','optimizadorGramatica.py',175),
  ('declarations -> declaration','declarations',1,'p_declarations','optimizadorGramatica.py',176),
  ('declaration -> VAR idList LECOR INTLITERAL RICOR FLOAT64 SEMICOLON','declaration',7,'p_declaration','optimizadorGramatica.py',185),
  ('declaration -> VAR idList type SEMICOLON','declaration',4,'p_declaration','optimizadorGramatica.py',186),
  ('type -> INT','type',1,'p_type','optimizadorGramatica.py',194),
  ('type -> FLOAT64','type',1,'p_type','optimizadorGramatica.py',195),
  ('idList -> idList COMMA ID','idList',3,'p_idList','optimizadorGramatica.py',203),
  ('idList -> ID','idList',1,'p_idList','optimizadorGramatica.py',204),
  ('codeList -> codeList code','codeList',2,'p_codeList','optimizadorGramatica.py',212),
  ('codeList -> code','codeList',1,'p_codeList','optimizadorGramatica.py',213),
  ('code -> FUNC ID LEPAR RIPAR statement','code',5,'p_code','optimizadorGramatica.py',222),
  ('statement -> LEKEY instructions RIKEY','statement',3,'p_statement','optimizadorGramatica.py',227),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','optimizadorGramatica.py',232),
  ('instructions -> instruction','instructions',1,'p_instructions','optimizadorGramatica.py',233),
  ('instruction -> assign SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',242),
  ('instruction -> print SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',243),
  ('instruction -> if','instruction',1,'p_instruction','optimizadorGramatica.py',244),
  ('instruction -> gotoSt SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',245),
  ('instruction -> label','instruction',1,'p_instruction','optimizadorGramatica.py',246),
  ('instruction -> callFunc SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',247),
  ('instruction -> retSt SEMICOLON','instruction',2,'p_instruction','optimizadorGramatica.py',248),
  ('retSt -> RETURN','retSt',1,'p_return','optimizadorGramatica.py',253),
  ('callFunc -> ID LEPAR RIPAR','callFunc',3,'p_callFunc','optimizadorGramatica.py',258),
  ('label -> ID COLON','label',2,'p_label','optimizadorGramatica.py',263),
  ('gotoSt -> GOTO ID','gotoSt',2,'p_goto','optimizadorGramatica.py',268),
  ('if -> IF expression LEKEY GOTO ID SEMICOLON RIKEY','if',7,'p_if','optimizadorGramatica.py',273),
  ('assign -> access EQUALS finalExp','assign',3,'p_assign','optimizadorGramatica.py',278),
  ('assign -> ID EQUALS expression','assign',3,'p_assign2','optimizadorGramatica.py',283),
  ('assign -> ID EQUALS access','assign',3,'p_assign2','optimizadorGramatica.py',284),
  ('print -> FMT POINT PRINTF LEPAR STRINGLITERAL COMMA printValue RIPAR','print',8,'p_print','optimizadorGramatica.py',290),
  ('printValue -> INT LEPAR finalExp RIPAR','printValue',4,'p_printValue','optimizadorGramatica.py',295),
  ('printValue -> finalExp','printValue',1,'p_printValue','optimizadorGramatica.py',296),
  ('expression -> finalExp PLUS finalExp','expression',3,'p_expression','optimizadorGramatica.py',305),
  ('expression -> finalExp MINUS finalExp','expression',3,'p_expression','optimizadorGramatica.py',306),
  ('expression -> finalExp TIMES finalExp','expression',3,'p_expression','optimizadorGramatica.py',307),
  ('expression -> finalExp DIV finalExp','expression',3,'p_expression','optimizadorGramatica.py',308),
  ('expression -> finalExp GREATER finalExp','expression',3,'p_expression','optimizadorGramatica.py',309),
  ('expression -> finalExp LESS finalExp','expression',3,'p_expression','optimizadorGramatica.py',310),
  ('expression -> finalExp GREATEREQUAL finalExp','expression',3,'p_expression','optimizadorGramatica.py',311),
  ('expression -> finalExp LESSEQUAL finalExp','expression',3,'p_expression','optimizadorGramatica.py',312),
  ('expression -> finalExp EQUALSEQUALS finalExp','expression',3,'p_expression','optimizadorGramatica.py',313),
  ('expression -> finalExp DISTINT finalExp','expression',3,'p_expression','optimizadorGramatica.py',314),
  ('expression -> MATH POINT MOD LEPAR finalExp COMMA finalExp RIPAR','expression',8,'p_expression','optimizadorGramatica.py',315),
  ('expression -> finalExp','expression',1,'p_expression','optimizadorGramatica.py',316),
  ('finalExp -> ID','finalExp',1,'p_finalExp','optimizadorGramatica.py',326),
  ('finalExp -> INTLITERAL','finalExp',1,'p_finalExp','optimizadorGramatica.py',327),
  ('finalExp -> MINUS INTLITERAL','finalExp',2,'p_finalExp','optimizadorGramatica.py',328),
  ('finalExp -> FLOATLITERAL','finalExp',1,'p_finalExp','optimizadorGramatica.py',329),
  ('access -> ID LECOR INT LEPAR finalExp RIPAR RICOR','access',7,'p_access','optimizadorGramatica.py',337),
  ('access -> ID LECOR finalExp RICOR','access',4,'p_access','optimizadorGramatica.py',338),
]
