
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftRORleftRANDrightUNOTleftMENORQUEMAYORQUEMENORIGUALMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOleftPOTENCIArightUMENOSleftPUNTOCADENA COMA CORCHA CORCHC DECIMAL DIFERENTE DIVISION DOSPTS ENTERO ID IGUAL IGUALIGUAL LINEANUEVA LLAVEC MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MODULO MULTIPLICACION PARA PARC POTENCIA PUNTO PUNTOCOMA RAND RBOOLEAN RBREAK RDEF RELIF RELSE RFALSE RFLOAT RIF RINT RLIST RMUTABLE RNOT RNULO ROR RPRINT RSTRING RSTRUCT RTRUE RWHILEinit            : ls_instrinit            : emptyempty :ls_instr   : ls_instr instrls_instr   : instrinstr    : instruccion\n                | funcion_instr LLAVEC\n    PARAMETROS   : PARAMETROS COMA PARAMETROPARAMETROS   : PARAMETROPARAMETRO    : expresionPARAMETROSTIPO : PARAMETROSTIPO COMA PARAMETROTIPOPARAMETROSTIPO : PARAMETROTIPOPARAMETROTIPO : ID DOSPTS TIPO\n                    | ID DOSPTS ID\n                    | IDinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr\n                        | declaracion_instr\n                        | llamada_instr\n                        | struct_instr\n                        | if_instr\n                        | while_instr\n                        | break_instr\n    imprimir_instr     : RPRINT PARA PARAMETROS PARCdeclaracion_instr :  ID IGUAL expresiondeclaracion_instr : ID DOSPTS TIPO IGUAL expresiondeclaracion_instr : ID ACCESOLISTA IGUAL expresiondeclaracion_instr : GETSTRUCTS IGUAL expresionfuncion_instr : RDEF ID PARA PARC DOSPTS instrucciones\n                     | RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instruccionesllamada_instr : ID PARA PARC\n                    | ID PARA PARAMETROS PARCllamada_expre : ID PARA PARC\n                     | ID PARA PARAMETROS PARCLISTA : CORCHA PARAMETROS CORCHCACCESOLISTA : ACCESOLISTA ITEMLISTAACCESOLISTA : ITEMLISTAITEMLISTA : CORCHA expresion CORCHCstruct_instr : RMUTABLE RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC\n                    | RMUTABLE RSTRUCT ID LLAVEC\n                    | RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC\n                    | RSTRUCT ID LLAVEC\n    ATRIBUTOSSTRUCT : ATRIBUTOSSTRUCT ATRIBSTRUCT PUNTOCOMAATRIBUTOSSTRUCT : ATRIBSTRUCT PUNTOCOMAATRIBSTRUCT : ID DOSPTS TIPO\n                    | ID DOSPTS ID\n                    | IDGETSTRUCTS : GETSTRUCTS PUNTO GETSTRUCTGETSTRUCTS : GETSTRUCTGETSTRUCT : IDif_instr : RIF expresion DOSPTS instrucciones LLAVECif_instr : RIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVECif_instr : RIF expresion DOSPTS instrucciones LLAVEC lista_eliflista_elif : lista_elif elif_instlista_elif : elif_instelif_inst : RELIF expresion DOSPTS instrucciones LLAVECelif_inst : RELIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVECelif_inst : RELIF expresion DOSPTS instrucciones LLAVEC lista_elifwhile_instr : RWHILE expresion DOSPTS instrucciones LLAVECbreak_instr : RBREAKTIPO : RINT\n            | RFLOAT\n            | RBOOLEAN\n            | RSTRING\n            | ID\n            | RLISTexpresion     : expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion MULTIPLICACION expresion\n                    | expresion DIVISION expresion\n                    | expresion POTENCIA expresion\n                    | expresion MODULO expresion\n                    | expresion PUNTO expresion\n                    expresion    : expresion MAYORQUE expresion\n                    | expresion MENORQUE expresion\n                    | expresion MAYORIGUAL expresion\n                    | expresion MENORIGUAL expresion\n                    | expresion IGUALIGUAL expresion\n                    | expresion DIFERENTE expresionexpresion    : expresion RAND expresion\n                    | expresion ROR expresionexpresion      : RNOT expresion %prec UNOTexpresion      : MENOS expresion %prec UMENOSexpresion      : PARA expresion PARCexpresion      : ENTEROexpresion      : DECIMALexpresion      : CADENAexpresion      : IDexpresion    : RTRUE\n                    | RFALSE\n                    | RNULOexpresion :    LISTAexpresion : ID ACCESOLISTAexpresion : llamada_expre'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,8,9,10,11,12,13,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,94,95,97,106,107,109,110,112,114,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,145,149,151,152,159,160,164,168,170,172,175,],[-3,0,-1,-2,-5,-6,-18,-19,-20,-21,-22,-23,-24,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,-84,-83,-94,-28,-33,-39,-25,-41,-42,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,-27,-40,-52,-35,-60,-54,-56,-55,-53,-57,-59,-58,]),'RDEF':([0,2,4,5,7,8,9,10,11,12,13,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,94,95,97,106,107,109,110,112,114,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,145,149,151,152,159,160,164,168,170,172,175,],[14,14,-5,-6,-18,-19,-20,-21,-22,-23,-24,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,-84,-83,-94,-28,-33,-39,-25,-41,-42,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,-27,-40,-52,-35,-60,-54,-56,-55,-53,-57,-59,-58,]),'RPRINT':([0,2,4,5,7,8,9,10,11,12,13,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,78,94,95,97,100,106,107,109,110,112,114,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,140,143,145,149,150,151,152,155,156,159,160,162,163,164,166,167,168,169,170,172,173,174,175,],[16,16,-5,-6,-18,-19,-20,-21,-22,-23,-24,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,16,-84,-83,-94,16,-28,-33,-39,-25,-41,-42,16,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,16,16,-27,-40,-52,-16,-35,-60,16,16,-54,-56,16,16,-55,16,16,-53,16,-57,-59,16,16,-58,]),'ID':([0,2,4,5,7,8,9,10,11,12,13,14,19,20,21,22,24,25,27,28,30,31,32,33,34,35,36,37,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,62,63,64,70,73,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,100,105,106,107,108,109,110,111,112,113,114,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,139,140,142,143,145,148,149,150,151,152,155,156,159,160,161,162,163,164,166,167,168,169,170,172,173,174,175,],[15,15,-5,-6,-18,-19,-20,-21,-22,-23,-24,26,37,45,45,-61,-4,-7,45,55,45,-38,45,45,45,72,73,74,45,45,45,-86,-87,-88,-89,-90,-91,-92,-93,-95,45,101,-26,45,-37,-32,-29,74,74,-43,15,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-84,-83,-94,45,15,45,-28,-33,45,-39,-25,74,-41,146,-42,-45,15,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,15,153,15,101,-27,-40,-44,-52,-16,-35,-60,15,15,-54,-56,45,15,15,-55,15,15,-53,15,-57,-59,15,15,-58,]),'RMUTABLE':([0,2,4,5,7,8,9,10,11,12,13,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,78,94,95,97,100,106,107,109,110,112,114,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,140,143,145,149,150,151,152,155,156,159,160,162,163,164,166,167,168,169,170,172,173,174,175,],[18,18,-5,-6,-18,-19,-20,-21,-22,-23,-24,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,18,-84,-83,-94,18,-28,-33,-39,-25,-41,-42,18,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,18,18,-27,-40,-52,-16,-35,-60,18,18,-54,-56,18,18,-55,18,18,-53,18,-57,-59,18,18,-58,]),'RSTRUCT':([0,2,4,5,7,8,9,10,11,12,13,18,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,78,94,95,97,100,106,107,109,110,112,114,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,140,143,145,149,150,151,152,155,156,159,160,162,163,164,166,167,168,169,170,172,173,174,175,],[19,19,-5,-6,-18,-19,-20,-21,-22,-23,-24,36,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,19,-84,-83,-94,19,-28,-33,-39,-25,-41,-42,19,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,19,19,-27,-40,-52,-16,-35,-60,19,19,-54,-56,19,19,-55,19,19,-53,19,-57,-59,19,19,-58,]),'RIF':([0,2,4,5,7,8,9,10,11,12,13,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,78,94,95,97,100,106,107,109,110,112,114,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,140,143,145,149,150,151,152,155,156,159,160,162,163,164,166,167,168,169,170,172,173,174,175,],[20,20,-5,-6,-18,-19,-20,-21,-22,-23,-24,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,20,-84,-83,-94,20,-28,-33,-39,-25,-41,-42,20,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,20,20,-27,-40,-52,-16,-35,-60,20,20,-54,-56,20,20,-55,20,20,-53,20,-57,-59,20,20,-58,]),'RWHILE':([0,2,4,5,7,8,9,10,11,12,13,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,78,94,95,97,100,106,107,109,110,112,114,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,140,143,145,149,150,151,152,155,156,159,160,162,163,164,166,167,168,169,170,172,173,174,175,],[21,21,-5,-6,-18,-19,-20,-21,-22,-23,-24,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,21,-84,-83,-94,21,-28,-33,-39,-25,-41,-42,21,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,21,21,-27,-40,-52,-16,-35,-60,21,21,-54,-56,21,21,-55,21,21,-53,21,-57,-59,21,21,-58,]),'RBREAK':([0,2,4,5,7,8,9,10,11,12,13,22,24,25,31,42,43,44,45,46,47,48,49,50,54,63,64,70,76,78,94,95,97,100,106,107,109,110,112,114,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,140,143,145,149,150,151,152,155,156,159,160,162,163,164,166,167,168,169,170,172,173,174,175,],[22,22,-5,-6,-18,-19,-20,-21,-22,-23,-24,-61,-4,-7,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,-43,22,-84,-83,-94,22,-28,-33,-39,-25,-41,-42,22,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,22,22,-27,-40,-52,-16,-35,-60,22,22,-54,-56,22,22,-55,22,22,-53,22,-57,-59,22,22,-58,]),'LLAVEC':([6,7,8,9,10,11,12,13,22,31,37,42,43,44,45,46,47,48,49,50,54,63,64,70,73,75,76,94,95,97,106,107,109,110,111,112,114,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,138,143,145,148,149,150,151,152,155,159,160,162,164,166,168,169,170,172,174,175,],[25,-18,-19,-20,-21,-22,-23,-24,-61,-38,76,-86,-87,-88,-89,-90,-91,-92,-93,-95,-26,-37,-32,-29,112,114,-43,-84,-83,-94,-28,-33,-39,-25,145,-41,-42,-45,149,-17,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,152,-27,-40,-44,-52,-16,-35,-60,-30,-54,-56,-31,-55,168,-53,170,-57,-59,175,-58,]),'IGUAL':([15,17,23,29,31,55,56,57,58,59,60,61,63,71,72,109,],[27,34,-50,62,-38,-66,105,-62,-63,-64,-65,-67,-37,-49,-51,-39,]),'DOSPTS':([15,31,38,42,43,44,45,46,47,48,49,50,52,63,74,94,95,97,101,102,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,141,151,158,165,171,],[28,-38,78,-86,-87,-88,-89,-90,-91,-92,-93,-95,100,-37,113,-84,-83,-94,139,140,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,156,-35,163,167,173,]),'PARA':([15,16,20,21,26,27,30,32,33,34,39,40,41,45,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[30,33,41,41,53,41,41,41,41,41,41,41,41,98,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'PUNTO':([15,17,23,31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,71,72,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-51,35,-50,-38,85,-86,-87,-88,-89,-90,-91,-92,-93,-95,85,85,-37,85,85,85,-49,-51,85,85,85,-94,85,-39,85,85,85,85,85,85,-74,85,85,85,85,85,85,85,85,-85,-34,-36,85,-35,85,]),'CORCHA':([15,20,21,27,29,30,31,32,33,34,39,40,41,45,51,62,63,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,97,98,105,108,109,161,],[32,51,51,51,32,51,-38,51,51,51,51,51,51,32,51,51,-37,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,32,51,51,51,-39,51,]),'RNOT':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'MENOS':([20,21,27,30,31,32,33,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,54,62,63,67,68,70,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,106,108,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,161,165,],[39,39,39,39,-38,39,39,39,80,39,39,39,-86,-87,-88,-89,-90,-91,-92,-93,-95,39,80,80,39,-37,80,80,80,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-84,80,80,-94,39,39,80,39,-39,-68,-69,-70,-71,-72,-73,-74,80,80,80,80,80,80,80,80,-85,-34,-36,80,-35,39,80,]),'ENTERO':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'DECIMAL':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'CADENA':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'RTRUE':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'RFALSE':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'RNULO':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'RINT':([28,113,139,],[57,57,57,]),'RFLOAT':([28,113,139,],[58,58,58,]),'RBOOLEAN':([28,113,139,],[59,59,59,]),'RSTRING':([28,113,139,],[60,60,60,]),'RLIST':([28,113,139,],[61,61,61,]),'PARC':([30,31,42,43,44,45,46,47,48,49,50,53,57,58,59,60,61,63,65,66,67,69,94,95,96,97,98,101,103,104,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,144,151,153,154,157,],[64,-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,102,-62,-63,-64,-65,-67,-37,107,-9,-10,110,-84,-83,134,-94,135,-15,141,-12,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,151,-36,-8,-35,-14,-13,-11,]),'MAS':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,79,-86,-87,-88,-89,-90,-91,-92,-93,-95,79,79,-37,79,79,79,-84,79,79,-94,79,-39,-68,-69,-70,-71,-72,-73,-74,79,79,79,79,79,79,79,79,-85,-34,-36,79,-35,79,]),'MULTIPLICACION':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,81,-86,-87,-88,-89,-90,-91,-92,-93,-95,81,81,-37,81,81,81,-84,81,81,-94,81,-39,81,81,-70,-71,-72,-73,-74,81,81,81,81,81,81,81,81,-85,-34,-36,81,-35,81,]),'DIVISION':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,82,-86,-87,-88,-89,-90,-91,-92,-93,-95,82,82,-37,82,82,82,-84,82,82,-94,82,-39,82,82,-70,-71,-72,-73,-74,82,82,82,82,82,82,82,82,-85,-34,-36,82,-35,82,]),'POTENCIA':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,83,-86,-87,-88,-89,-90,-91,-92,-93,-95,83,83,-37,83,83,83,-84,83,83,-94,83,-39,83,83,83,83,-72,83,-74,83,83,83,83,83,83,83,83,-85,-34,-36,83,-35,83,]),'MODULO':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,84,-86,-87,-88,-89,-90,-91,-92,-93,-95,84,84,-37,84,84,84,-84,84,84,-94,84,-39,84,84,-70,-71,-72,-73,-74,84,84,84,84,84,84,84,84,-85,-34,-36,84,-35,84,]),'MAYORQUE':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,86,-86,-87,-88,-89,-90,-91,-92,-93,-95,86,86,-37,86,86,86,-84,86,86,-94,86,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,86,86,-85,-34,-36,86,-35,86,]),'MENORQUE':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,87,-86,-87,-88,-89,-90,-91,-92,-93,-95,87,87,-37,87,87,87,-84,87,87,-94,87,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,87,87,-85,-34,-36,87,-35,87,]),'MAYORIGUAL':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,88,-86,-87,-88,-89,-90,-91,-92,-93,-95,88,88,-37,88,88,88,-84,88,88,-94,88,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,88,88,-85,-34,-36,88,-35,88,]),'MENORIGUAL':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,89,-86,-87,-88,-89,-90,-91,-92,-93,-95,89,89,-37,89,89,89,-84,89,89,-94,89,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,89,89,-85,-34,-36,89,-35,89,]),'IGUALIGUAL':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,90,-86,-87,-88,-89,-90,-91,-92,-93,-95,90,90,-37,90,90,90,-84,90,90,-94,90,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,90,90,-85,-34,-36,90,-35,90,]),'DIFERENTE':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,91,-86,-87,-88,-89,-90,-91,-92,-93,-95,91,91,-37,91,91,91,-84,91,91,-94,91,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,91,91,-85,-34,-36,91,-35,91,]),'RAND':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,92,-86,-87,-88,-89,-90,-91,-92,-93,-95,92,92,-37,92,92,92,-84,-83,92,-94,92,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,92,-85,-34,-36,92,-35,92,]),'ROR':([31,38,42,43,44,45,46,47,48,49,50,52,54,63,67,68,70,94,95,96,97,106,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,143,151,165,],[-38,93,-86,-87,-88,-89,-90,-91,-92,-93,-95,93,93,-37,93,93,93,-84,-83,93,-94,93,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,93,-35,93,]),'COMA':([31,42,43,44,45,46,47,48,49,50,57,58,59,60,61,63,65,66,67,69,94,95,97,99,101,103,104,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,144,151,153,154,157,],[-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-62,-63,-64,-65,-67,-37,108,-9,-10,108,-84,-83,-94,108,-15,142,-12,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,108,-36,-8,-35,-14,-13,-11,]),'CORCHC':([31,42,43,44,45,46,47,48,49,50,63,66,67,68,94,95,97,99,109,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,137,144,151,],[-38,-86,-87,-88,-89,-90,-91,-92,-93,-95,-37,-9,-10,109,-84,-83,-94,137,-39,-68,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,-82,-85,-34,-36,-8,-35,]),'PUNTOCOMA':([57,58,59,60,61,74,77,115,146,147,],[-62,-63,-64,-65,-67,-48,116,148,-47,-46,]),'RELSE':([149,170,],[158,171,]),'RELIF':([149,159,160,164,170,172,175,],[161,161,-56,-55,161,161,-58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'ls_instr':([0,],[2,]),'empty':([0,],[3,]),'instr':([0,2,],[4,24,]),'instruccion':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[5,5,118,118,150,150,118,150,118,150,118,150,118,150,118,150,]),'funcion_instr':([0,2,],[6,6,]),'imprimir_instr':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'declaracion_instr':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'llamada_instr':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'struct_instr':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'if_instr':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'while_instr':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'break_instr':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'GETSTRUCTS':([0,2,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'GETSTRUCT':([0,2,35,78,100,117,138,140,155,156,162,163,166,167,169,173,174,],[23,23,71,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'ACCESOLISTA':([15,45,],[29,97,]),'ITEMLISTA':([15,29,45,97,],[31,63,31,63,]),'expresion':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[38,52,54,67,68,67,70,94,95,96,67,106,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,67,143,67,165,]),'LISTA':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'llamada_expre':([20,21,27,30,32,33,34,39,40,41,51,62,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,98,105,108,161,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'TIPO':([28,113,139,],[56,147,154,]),'PARAMETROS':([30,33,51,98,],[65,69,99,136,]),'PARAMETRO':([30,33,51,98,108,],[66,66,66,66,144,]),'ATRIBUTOSSTRUCT':([37,73,],[75,111,]),'ATRIBSTRUCT':([37,73,75,111,],[77,77,115,115,]),'PARAMETROSTIPO':([53,],[103,]),'PARAMETROTIPO':([53,142,],[104,157,]),'instrucciones':([78,100,140,156,163,167,173,],[117,138,155,162,166,169,174,]),'lista_elif':([149,170,],[159,172,]),'elif_inst':([149,159,170,172,],[160,164,160,164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> ls_instr','init',1,'p_init','gramatica.py',191),
  ('init -> empty','init',1,'p_init_empty','gramatica.py',195),
  ('empty -> <empty>','empty',0,'p_empty','gramatica.py',199),
  ('ls_instr -> ls_instr instr','ls_instr',2,'p_ls_instr','gramatica.py',203),
  ('ls_instr -> instr','ls_instr',1,'p_ls_instr2','gramatica.py',208),
  ('instr -> instruccion','instr',1,'p_instr_recib','gramatica.py',212),
  ('instr -> funcion_instr LLAVEC','instr',2,'p_instr_recib','gramatica.py',213),
  ('PARAMETROS -> PARAMETROS COMA PARAMETRO','PARAMETROS',3,'p_lista_parametros','gramatica.py',220),
  ('PARAMETROS -> PARAMETRO','PARAMETROS',1,'p_lista_parametro2','gramatica.py',225),
  ('PARAMETRO -> expresion','PARAMETRO',1,'p_parametro_v','gramatica.py',229),
  ('PARAMETROSTIPO -> PARAMETROSTIPO COMA PARAMETROTIPO','PARAMETROSTIPO',3,'p_parametros_tipo','gramatica.py',233),
  ('PARAMETROSTIPO -> PARAMETROTIPO','PARAMETROSTIPO',1,'p_parametro_tipo','gramatica.py',238),
  ('PARAMETROTIPO -> ID DOSPTS TIPO','PARAMETROTIPO',3,'p_parametro_tipo_id','gramatica.py',242),
  ('PARAMETROTIPO -> ID DOSPTS ID','PARAMETROTIPO',3,'p_parametro_tipo_id','gramatica.py',243),
  ('PARAMETROTIPO -> ID','PARAMETROTIPO',1,'p_parametro_tipo_id','gramatica.py',244),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','gramatica.py',252),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',258),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',265),
  ('instruccion -> declaracion_instr','instruccion',1,'p_instruccion','gramatica.py',266),
  ('instruccion -> llamada_instr','instruccion',1,'p_instruccion','gramatica.py',267),
  ('instruccion -> struct_instr','instruccion',1,'p_instruccion','gramatica.py',268),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','gramatica.py',269),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','gramatica.py',270),
  ('instruccion -> break_instr','instruccion',1,'p_instruccion','gramatica.py',271),
  ('imprimir_instr -> RPRINT PARA PARAMETROS PARC','imprimir_instr',4,'p_imprimir','gramatica.py',277),
  ('declaracion_instr -> ID IGUAL expresion','declaracion_instr',3,'p_declaracion','gramatica.py',282),
  ('declaracion_instr -> ID DOSPTS TIPO IGUAL expresion','declaracion_instr',5,'p_declaracion2','gramatica.py',286),
  ('declaracion_instr -> ID ACCESOLISTA IGUAL expresion','declaracion_instr',4,'p_declaracion3','gramatica.py',291),
  ('declaracion_instr -> GETSTRUCTS IGUAL expresion','declaracion_instr',3,'p_declaracion4','gramatica.py',296),
  ('funcion_instr -> RDEF ID PARA PARC DOSPTS instrucciones','funcion_instr',6,'p_funciones','gramatica.py',301),
  ('funcion_instr -> RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instrucciones','funcion_instr',7,'p_funciones','gramatica.py',302),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada_instr','gramatica.py',312),
  ('llamada_instr -> ID PARA PARAMETROS PARC','llamada_instr',4,'p_llamada_instr','gramatica.py',313),
  ('llamada_expre -> ID PARA PARC','llamada_expre',3,'p_llamada_expresion','gramatica.py',321),
  ('llamada_expre -> ID PARA PARAMETROS PARC','llamada_expre',4,'p_llamada_expresion','gramatica.py',322),
  ('LISTA -> CORCHA PARAMETROS CORCHC','LISTA',3,'p_listas','gramatica.py',330),
  ('ACCESOLISTA -> ACCESOLISTA ITEMLISTA','ACCESOLISTA',2,'p_acceso_lista','gramatica.py',335),
  ('ACCESOLISTA -> ITEMLISTA','ACCESOLISTA',1,'p_acceso_lista2','gramatica.py',340),
  ('ITEMLISTA -> CORCHA expresion CORCHC','ITEMLISTA',3,'p_item_lista','gramatica.py',344),
  ('struct_instr -> RMUTABLE RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC','struct_instr',5,'p_instr_struct','gramatica.py',349),
  ('struct_instr -> RMUTABLE RSTRUCT ID LLAVEC','struct_instr',4,'p_instr_struct','gramatica.py',350),
  ('struct_instr -> RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC','struct_instr',4,'p_instr_struct','gramatica.py',351),
  ('struct_instr -> RSTRUCT ID LLAVEC','struct_instr',3,'p_instr_struct','gramatica.py',352),
  ('ATRIBUTOSSTRUCT -> ATRIBUTOSSTRUCT ATRIBSTRUCT PUNTOCOMA','ATRIBUTOSSTRUCT',3,'p_atrib_struct','gramatica.py',365),
  ('ATRIBUTOSSTRUCT -> ATRIBSTRUCT PUNTOCOMA','ATRIBUTOSSTRUCT',2,'p_atrib_struct2','gramatica.py',370),
  ('ATRIBSTRUCT -> ID DOSPTS TIPO','ATRIBSTRUCT',3,'p_atrib_item','gramatica.py',374),
  ('ATRIBSTRUCT -> ID DOSPTS ID','ATRIBSTRUCT',3,'p_atrib_item','gramatica.py',375),
  ('ATRIBSTRUCT -> ID','ATRIBSTRUCT',1,'p_atrib_item','gramatica.py',376),
  ('GETSTRUCTS -> GETSTRUCTS PUNTO GETSTRUCT','GETSTRUCTS',3,'p_get_struct','gramatica.py',383),
  ('GETSTRUCTS -> GETSTRUCT','GETSTRUCTS',1,'p_get_strct2','gramatica.py',388),
  ('GETSTRUCT -> ID','GETSTRUCT',1,'p_get_item','gramatica.py',392),
  ('if_instr -> RIF expresion DOSPTS instrucciones LLAVEC','if_instr',5,'p_if_instr','gramatica.py',397),
  ('if_instr -> RIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVEC','if_instr',9,'p_if_instr2','gramatica.py',401),
  ('if_instr -> RIF expresion DOSPTS instrucciones LLAVEC lista_elif','if_instr',6,'p_if_instr3','gramatica.py',404),
  ('lista_elif -> lista_elif elif_inst','lista_elif',2,'p_lista_elif','gramatica.py',408),
  ('lista_elif -> elif_inst','lista_elif',1,'p_lista_elif2','gramatica.py',413),
  ('elif_inst -> RELIF expresion DOSPTS instrucciones LLAVEC','elif_inst',5,'p_lista_elif_item','gramatica.py',417),
  ('elif_inst -> RELIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVEC','elif_inst',9,'p_lista_elif_item2','gramatica.py',421),
  ('elif_inst -> RELIF expresion DOSPTS instrucciones LLAVEC lista_elif','elif_inst',6,'p_lista_elif_item3','gramatica.py',425),
  ('while_instr -> RWHILE expresion DOSPTS instrucciones LLAVEC','while_instr',5,'p_while_instr','gramatica.py',430),
  ('break_instr -> RBREAK','break_instr',1,'p_break_instr','gramatica.py',435),
  ('TIPO -> RINT','TIPO',1,'p_tipo','gramatica.py',440),
  ('TIPO -> RFLOAT','TIPO',1,'p_tipo','gramatica.py',441),
  ('TIPO -> RBOOLEAN','TIPO',1,'p_tipo','gramatica.py',442),
  ('TIPO -> RSTRING','TIPO',1,'p_tipo','gramatica.py',443),
  ('TIPO -> ID','TIPO',1,'p_tipo','gramatica.py',444),
  ('TIPO -> RLIST','TIPO',1,'p_tipo','gramatica.py',445),
  ('expresion -> expresion MAS expresion','expresion',3,'p_aritmeticas','gramatica.py',463),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_aritmeticas','gramatica.py',464),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_aritmeticas','gramatica.py',465),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_aritmeticas','gramatica.py',466),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_aritmeticas','gramatica.py',467),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_aritmeticas','gramatica.py',468),
  ('expresion -> expresion PUNTO expresion','expresion',3,'p_aritmeticas','gramatica.py',469),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_relacionales','gramatica.py',488),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_relacionales','gramatica.py',489),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',490),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',491),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',492),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_relacionales','gramatica.py',493),
  ('expresion -> expresion RAND expresion','expresion',3,'p_logicas','gramatica.py',512),
  ('expresion -> expresion ROR expresion','expresion',3,'p_logicas','gramatica.py',513),
  ('expresion -> RNOT expresion','expresion',2,'p_expre_not','gramatica.py',520),
  ('expresion -> MENOS expresion','expresion',2,'p_negacion','gramatica.py',526),
  ('expresion -> PARA expresion PARC','expresion',3,'p_parentesis','gramatica.py',531),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','gramatica.py',536),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','gramatica.py',540),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',544),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',548),
  ('expresion -> RTRUE','expresion',1,'p_expresion_bool','gramatica.py',552),
  ('expresion -> RFALSE','expresion',1,'p_expresion_bool','gramatica.py',553),
  ('expresion -> RNULO','expresion',1,'p_expresion_bool','gramatica.py',554),
  ('expresion -> LISTA','expresion',1,'p_expresion_lista','gramatica.py',564),
  ('expresion -> ID ACCESOLISTA','expresion',2,'p_expresion_accesolst','gramatica.py',568),
  ('expresion -> llamada_expre','expresion',1,'p_expresion_llamada','gramatica.py',573),
]
