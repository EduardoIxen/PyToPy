
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftRORleftRANDrightUNOTleftMENORQUEMAYORQUEMENORIGUALMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONMODULOleftPOTENCIArightUMENOSleftPUNTOCADENA COMA CORCHA CORCHC DECIMAL DIFERENTE DIVISION DOSPTS ENTERO ID IGUAL IGUALIGUAL LINEANUEVA LLAVEC MAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MODULO MULTIPLICACION PARA PARC POTENCIA PUNTO PUNTOCOMA RAND RBOOLEAN RBREAK RCONTINUE RDEF RELIF RELSE RFALSE RFLOAT RFOR RIF RIN RINT RLIST RMUTABLE RNOT RNULO ROR RPRINT RRETURN RSTRING RSTRUCT RTRUE RWHILEinit            : ls_instrinit            : emptyempty :ls_instr   : ls_instr instrls_instr   : instrinstr    : instruccion\n                | funcion_instr LLAVEC\n    PARAMETROS   : PARAMETROS COMA PARAMETROPARAMETROS   : PARAMETROPARAMETRO    : expresionPARAMETROSTIPO : PARAMETROSTIPO COMA PARAMETROTIPOPARAMETROSTIPO : PARAMETROTIPOPARAMETROTIPO : ID DOSPTS TIPO\n                    | ID DOSPTS ID\n                    | IDinstrucciones    : instrucciones instruccioninstrucciones    : instruccioninstruccion      : imprimir_instr\n                        | declaracion_instr\n                        | llamada_instr\n                        | struct_instr\n                        | if_instr\n                        | while_instr\n                        | break_instr\n                        | continue_instr\n                        | return_instr\n                        | for_instr\n    imprimir_instr     : RPRINT PARA PARAMETROS PARCdeclaracion_instr :  ID IGUAL expresiondeclaracion_instr : ID DOSPTS TIPO IGUAL expresiondeclaracion_instr : ID ACCESOLISTA IGUAL expresiondeclaracion_instr : GETSTRUCTS IGUAL expresionfuncion_instr : RDEF ID PARA PARC DOSPTS instrucciones\n                     | RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instruccionesllamada_instr : ID PARA PARC\n                    | ID PARA PARAMETROS PARCllamada_expre : ID PARA PARC\n                     | ID PARA PARAMETROS PARCLISTA : CORCHA PARAMETROS CORCHCACCESOLISTA : ACCESOLISTA ITEMLISTAACCESOLISTA : ITEMLISTAITEMLISTA : CORCHA expresion CORCHCstruct_instr : RMUTABLE RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC\n                    | RMUTABLE RSTRUCT ID LLAVEC\n                    | RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC\n                    | RSTRUCT ID LLAVEC\n    ATRIBUTOSSTRUCT : ATRIBUTOSSTRUCT ATRIBSTRUCT PUNTOCOMAATRIBUTOSSTRUCT : ATRIBSTRUCT PUNTOCOMAATRIBSTRUCT : ID DOSPTS TIPO\n                    | ID DOSPTS ID\n                    | IDGETSTRUCTS : GETSTRUCTS PUNTO GETSTRUCTGETSTRUCTS : GETSTRUCTGETSTRUCT : IDif_instr : RIF expresion DOSPTS instrucciones LLAVECif_instr : RIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVECif_instr : RIF expresion DOSPTS instrucciones LLAVEC lista_eliflista_elif : lista_elif elif_instlista_elif : elif_instelif_inst : RELIF expresion DOSPTS instrucciones LLAVECelif_inst : RELIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVECelif_inst : RELIF expresion DOSPTS instrucciones LLAVEC lista_elifwhile_instr : RWHILE expresion DOSPTS instrucciones LLAVECbreak_instr : RBREAKcontinue_instr : RCONTINUEreturn_instr : RRETURN expresionfor_instr : RFOR ID RIN expresion DOSPTS instrucciones LLAVECTIPO : RINT\n            | RFLOAT\n            | RBOOLEAN\n            | RSTRING\n            | ID\n            | RLISTexpresion     : expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion MULTIPLICACION expresion\n                    | expresion DIVISION expresion\n                    | expresion POTENCIA expresion\n                    | expresion MODULO expresion\n                    | expresion PUNTO expresion\n                    expresion    : expresion MAYORQUE expresion\n                    | expresion MENORQUE expresion\n                    | expresion MAYORIGUAL expresion\n                    | expresion MENORIGUAL expresion\n                    | expresion IGUALIGUAL expresion\n                    | expresion DIFERENTE expresionexpresion    : expresion RAND expresion\n                    | expresion ROR expresionexpresion      : RNOT expresion %prec UNOTexpresion      : MENOS expresion %prec UMENOSexpresion      : PARA expresion PARCexpresion      : ENTEROexpresion      : DECIMALexpresion      : CADENAexpresion      : IDexpresion    : RTRUE\n                    | RFALSE\n                    | RNULOexpresion :    LISTAexpresion : ID ACCESOLISTAexpresion : llamada_expre'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,102,103,105,115,116,118,119,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,153,155,159,161,162,170,171,176,178,181,183,185,188,],[-3,0,-1,-2,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,-90,-89,-100,-31,-36,-42,-28,-44,-45,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,-30,-43,-55,-38,-63,-57,-59,-58,-67,-56,-60,-62,-61,]),'RDEF':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,102,103,105,115,116,118,119,121,123,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,153,155,159,161,162,170,171,176,178,181,183,185,188,],[17,17,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,-90,-89,-100,-31,-36,-42,-28,-44,-45,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,-30,-43,-55,-38,-63,-57,-59,-58,-67,-56,-60,-62,-61,]),'RPRINT':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[19,19,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,19,-90,-89,-100,19,-31,-36,-42,-28,-44,-45,19,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,19,19,-30,-43,-55,-16,-38,-63,19,19,19,-57,-59,19,19,19,-58,-67,19,19,-56,19,-60,-62,19,19,-61,]),'ID':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,17,22,23,24,25,26,27,28,30,31,33,34,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,59,61,62,70,71,72,78,81,83,84,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,106,108,109,114,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,149,150,152,153,155,158,159,160,161,162,163,166,167,170,171,172,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[18,18,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,32,43,51,51,-64,-65,51,60,-4,-7,51,63,51,-41,51,51,51,80,81,82,51,51,51,-92,-93,-94,-95,-96,-97,-98,-99,-101,51,-66,110,-29,51,-40,-35,-32,82,82,-46,18,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-90,-89,-100,51,18,51,51,-31,-36,51,-42,-28,82,-44,156,-45,-48,18,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,18,164,18,110,-30,-43,-47,-55,-16,-38,-63,18,18,18,-57,-59,51,18,18,18,-58,-67,18,18,-56,18,-60,-62,18,18,-61,]),'RMUTABLE':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[21,21,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,21,-90,-89,-100,21,-31,-36,-42,-28,-44,-45,21,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,21,21,-30,-43,-55,-16,-38,-63,21,21,21,-57,-59,21,21,21,-58,-67,21,21,-56,21,-60,-62,21,21,-61,]),'RSTRUCT':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,21,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[22,22,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,42,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,22,-90,-89,-100,22,-31,-36,-42,-28,-44,-45,22,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,22,22,-30,-43,-55,-16,-38,-63,22,22,22,-57,-59,22,22,22,-58,-67,22,22,-56,22,-60,-62,22,22,-61,]),'RIF':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[23,23,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,23,-90,-89,-100,23,-31,-36,-42,-28,-44,-45,23,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,23,23,-30,-43,-55,-16,-38,-63,23,23,23,-57,-59,23,23,23,-58,-67,23,23,-56,23,-60,-62,23,23,-61,]),'RWHILE':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[24,24,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,24,-90,-89,-100,24,-31,-36,-42,-28,-44,-45,24,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,24,24,-30,-43,-55,-16,-38,-63,24,24,24,-57,-59,24,24,24,-58,-67,24,24,-56,24,-60,-62,24,24,-61,]),'RBREAK':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[25,25,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,25,-90,-89,-100,25,-31,-36,-42,-28,-44,-45,25,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,25,25,-30,-43,-55,-16,-38,-63,25,25,25,-57,-59,25,25,25,-58,-67,25,25,-56,25,-60,-62,25,25,-61,]),'RCONTINUE':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[26,26,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,26,-90,-89,-100,26,-31,-36,-42,-28,-44,-45,26,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,26,26,-30,-43,-55,-16,-38,-63,26,26,26,-57,-59,26,26,26,-58,-67,26,26,-56,26,-60,-62,26,26,-61,]),'RRETURN':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[27,27,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,27,-90,-89,-100,27,-31,-36,-42,-28,-44,-45,27,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,27,27,-30,-43,-55,-16,-38,-63,27,27,27,-57,-59,27,27,27,-58,-67,27,27,-56,27,-60,-62,27,27,-61,]),'RFOR':([0,2,4,5,7,8,9,10,11,12,13,14,15,16,25,26,30,31,37,48,49,50,51,52,53,54,55,56,59,62,71,72,78,84,86,102,103,105,108,115,116,118,119,121,123,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,150,153,155,159,160,161,162,163,166,167,170,171,173,174,175,176,178,179,180,181,182,183,185,186,187,188,],[28,28,-5,-6,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-4,-7,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,-46,28,-90,-89,-100,28,-31,-36,-42,-28,-44,-45,28,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,28,28,-30,-43,-55,-16,-38,-63,28,28,28,-57,-59,28,28,28,-58,-67,28,28,-56,28,-60,-62,28,28,-61,]),'LLAVEC':([6,7,8,9,10,11,12,13,14,15,16,25,26,37,43,48,49,50,51,52,53,54,55,56,59,62,71,72,78,81,83,84,102,103,105,115,116,118,119,120,121,123,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,147,153,155,158,159,160,161,162,166,170,171,173,174,176,178,179,181,182,183,185,187,188,],[31,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-64,-65,-41,84,-92,-93,-94,-95,-96,-97,-98,-99,-101,-66,-29,-40,-35,-32,121,123,-46,-90,-89,-100,-31,-36,-42,-28,155,-44,-45,-48,159,-17,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,162,-30,-43,-47,-55,-16,-38,-63,-33,-57,-59,178,-34,-58,-67,181,-56,183,-60,-62,188,-61,]),'IGUAL':([18,20,29,35,37,63,64,65,66,67,68,69,71,79,80,118,],[33,40,-53,70,-41,-72,114,-68,-69,-70,-71,-73,-40,-52,-54,-42,]),'DOSPTS':([18,37,44,48,49,50,51,52,53,54,55,56,58,71,82,102,103,105,110,111,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,151,161,169,177,184,],[34,-41,86,-92,-93,-94,-95,-96,-97,-98,-99,-101,108,-40,122,-90,-89,-100,149,150,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,163,167,-38,175,180,186,]),'PARA':([18,19,23,24,27,32,33,36,38,39,40,45,46,47,51,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[36,39,47,47,47,61,47,47,47,47,47,47,47,47,106,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'PUNTO':([18,20,29,37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,79,80,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-54,41,-53,-41,93,-92,-93,-94,-95,-96,-97,-98,-99,-101,93,93,93,-40,93,93,93,-52,-54,93,93,93,-100,93,-42,93,93,93,93,93,93,-80,93,93,93,93,93,93,93,93,-91,-37,-39,93,93,-38,93,]),'CORCHA':([18,23,24,27,33,35,36,37,38,39,40,45,46,47,51,57,70,71,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,105,106,109,114,117,118,172,],[38,57,57,57,57,38,57,-41,57,57,57,57,57,57,38,57,57,-40,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,38,57,57,57,57,-42,57,]),'RNOT':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'MENOS':([23,24,27,33,36,37,38,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,70,71,75,76,78,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,109,114,115,117,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,172,177,],[45,45,45,45,45,-41,45,45,45,88,45,45,45,-92,-93,-94,-95,-96,-97,-98,-99,-101,45,88,88,88,45,-40,88,88,88,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-90,88,88,-100,45,45,45,88,45,-42,-74,-75,-76,-77,-78,-79,-80,88,88,88,88,88,88,88,88,-91,-37,-39,88,88,-38,45,88,]),'ENTERO':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'DECIMAL':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'CADENA':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'RTRUE':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'RFALSE':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'RNULO':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'RINT':([34,122,149,],[65,65,65,]),'RFLOAT':([34,122,149,],[66,66,66,]),'RBOOLEAN':([34,122,149,],[67,67,67,]),'RSTRING':([34,122,149,],[68,68,68,]),'RLIST':([34,122,149,],[69,69,69,]),'PARC':([36,37,48,49,50,51,52,53,54,55,56,61,65,66,67,68,69,71,73,74,75,77,102,103,104,105,106,110,112,113,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,154,161,164,165,168,],[72,-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,111,-68,-69,-70,-71,-73,-40,116,-9,-10,119,-90,-89,143,-100,144,-15,151,-12,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,161,-39,-8,-38,-14,-13,-11,]),'MAS':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,87,-92,-93,-94,-95,-96,-97,-98,-99,-101,87,87,87,-40,87,87,87,-90,87,87,-100,87,-42,-74,-75,-76,-77,-78,-79,-80,87,87,87,87,87,87,87,87,-91,-37,-39,87,87,-38,87,]),'MULTIPLICACION':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,89,-92,-93,-94,-95,-96,-97,-98,-99,-101,89,89,89,-40,89,89,89,-90,89,89,-100,89,-42,89,89,-76,-77,-78,-79,-80,89,89,89,89,89,89,89,89,-91,-37,-39,89,89,-38,89,]),'DIVISION':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,90,-92,-93,-94,-95,-96,-97,-98,-99,-101,90,90,90,-40,90,90,90,-90,90,90,-100,90,-42,90,90,-76,-77,-78,-79,-80,90,90,90,90,90,90,90,90,-91,-37,-39,90,90,-38,90,]),'POTENCIA':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,91,-92,-93,-94,-95,-96,-97,-98,-99,-101,91,91,91,-40,91,91,91,-90,91,91,-100,91,-42,91,91,91,91,-78,91,-80,91,91,91,91,91,91,91,91,-91,-37,-39,91,91,-38,91,]),'MODULO':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,92,-92,-93,-94,-95,-96,-97,-98,-99,-101,92,92,92,-40,92,92,92,-90,92,92,-100,92,-42,92,92,-76,-77,-78,-79,-80,92,92,92,92,92,92,92,92,-91,-37,-39,92,92,-38,92,]),'MAYORQUE':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,94,-92,-93,-94,-95,-96,-97,-98,-99,-101,94,94,94,-40,94,94,94,-90,94,94,-100,94,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,94,94,-91,-37,-39,94,94,-38,94,]),'MENORQUE':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,95,-92,-93,-94,-95,-96,-97,-98,-99,-101,95,95,95,-40,95,95,95,-90,95,95,-100,95,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,95,95,-91,-37,-39,95,95,-38,95,]),'MAYORIGUAL':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,96,-92,-93,-94,-95,-96,-97,-98,-99,-101,96,96,96,-40,96,96,96,-90,96,96,-100,96,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,96,96,-91,-37,-39,96,96,-38,96,]),'MENORIGUAL':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,97,-92,-93,-94,-95,-96,-97,-98,-99,-101,97,97,97,-40,97,97,97,-90,97,97,-100,97,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,97,97,-91,-37,-39,97,97,-38,97,]),'IGUALIGUAL':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,98,-92,-93,-94,-95,-96,-97,-98,-99,-101,98,98,98,-40,98,98,98,-90,98,98,-100,98,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,98,98,-91,-37,-39,98,98,-38,98,]),'DIFERENTE':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,99,-92,-93,-94,-95,-96,-97,-98,-99,-101,99,99,99,-40,99,99,99,-90,99,99,-100,99,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,99,99,-91,-37,-39,99,99,-38,99,]),'RAND':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,100,-92,-93,-94,-95,-96,-97,-98,-99,-101,100,100,100,-40,100,100,100,-90,-89,100,-100,100,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,100,-91,-37,-39,100,100,-38,100,]),'ROR':([37,44,48,49,50,51,52,53,54,55,56,58,59,62,71,75,76,78,102,103,104,105,115,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,148,153,161,177,],[-41,101,-92,-93,-94,-95,-96,-97,-98,-99,-101,101,101,101,-40,101,101,101,-90,-89,101,-100,101,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,101,101,-38,101,]),'COMA':([37,48,49,50,51,52,53,54,55,56,65,66,67,68,69,71,73,74,75,77,102,103,105,107,110,112,113,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,154,161,164,165,168,],[-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-68,-69,-70,-71,-73,-40,117,-9,-10,117,-90,-89,-100,117,-15,152,-12,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,117,-39,-8,-38,-14,-13,-11,]),'CORCHC':([37,48,49,50,51,52,53,54,55,56,71,74,75,76,102,103,105,107,118,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,146,154,161,],[-41,-92,-93,-94,-95,-96,-97,-98,-99,-101,-40,-9,-10,118,-90,-89,-100,146,-42,-74,-75,-76,-77,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,-88,-91,-37,-39,-8,-38,]),'RIN':([60,],[109,]),'PUNTOCOMA':([65,66,67,68,69,82,85,124,156,157,],[-68,-69,-70,-71,-73,-51,125,158,-50,-49,]),'RELSE':([159,183,],[169,184,]),'RELIF':([159,170,171,176,183,185,188,],[172,172,-59,-58,172,172,-61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'ls_instr':([0,],[2,]),'empty':([0,],[3,]),'instr':([0,2,],[4,30,]),'instruccion':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[5,5,127,127,160,160,127,127,160,127,160,160,127,160,127,160,127,160,]),'funcion_instr':([0,2,],[6,6,]),'imprimir_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'declaracion_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'llamada_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'struct_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'if_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'while_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'break_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'continue_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'return_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'for_instr':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'GETSTRUCTS':([0,2,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'GETSTRUCT':([0,2,41,86,108,126,147,150,163,166,167,173,174,175,179,180,182,186,187,],[29,29,79,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'ACCESOLISTA':([18,51,],[35,105,]),'ITEMLISTA':([18,35,51,105,],[37,71,37,71,]),'expresion':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[44,58,59,62,75,76,75,78,102,103,104,75,115,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,75,148,153,75,177,]),'LISTA':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'llamada_expre':([23,24,27,33,36,38,39,40,45,46,47,57,70,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,106,109,114,117,172,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'TIPO':([34,122,149,],[64,157,165,]),'PARAMETROS':([36,39,57,106,],[73,77,107,145,]),'PARAMETRO':([36,39,57,106,117,],[74,74,74,74,154,]),'ATRIBUTOSSTRUCT':([43,81,],[83,120,]),'ATRIBSTRUCT':([43,81,83,120,],[85,85,124,124,]),'PARAMETROSTIPO':([61,],[112,]),'PARAMETROTIPO':([61,152,],[113,168,]),'instrucciones':([86,108,150,163,167,175,180,186,],[126,147,166,173,174,179,182,187,]),'lista_elif':([159,183,],[170,185,]),'elif_inst':([159,170,183,185,],[171,176,171,176,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> ls_instr','init',1,'p_init','gramatica.py',198),
  ('init -> empty','init',1,'p_init_empty','gramatica.py',202),
  ('empty -> <empty>','empty',0,'p_empty','gramatica.py',206),
  ('ls_instr -> ls_instr instr','ls_instr',2,'p_ls_instr','gramatica.py',210),
  ('ls_instr -> instr','ls_instr',1,'p_ls_instr2','gramatica.py',215),
  ('instr -> instruccion','instr',1,'p_instr_recib','gramatica.py',219),
  ('instr -> funcion_instr LLAVEC','instr',2,'p_instr_recib','gramatica.py',220),
  ('PARAMETROS -> PARAMETROS COMA PARAMETRO','PARAMETROS',3,'p_lista_parametros','gramatica.py',227),
  ('PARAMETROS -> PARAMETRO','PARAMETROS',1,'p_lista_parametro2','gramatica.py',232),
  ('PARAMETRO -> expresion','PARAMETRO',1,'p_parametro_v','gramatica.py',236),
  ('PARAMETROSTIPO -> PARAMETROSTIPO COMA PARAMETROTIPO','PARAMETROSTIPO',3,'p_parametros_tipo','gramatica.py',240),
  ('PARAMETROSTIPO -> PARAMETROTIPO','PARAMETROSTIPO',1,'p_parametro_tipo','gramatica.py',245),
  ('PARAMETROTIPO -> ID DOSPTS TIPO','PARAMETROTIPO',3,'p_parametro_tipo_id','gramatica.py',249),
  ('PARAMETROTIPO -> ID DOSPTS ID','PARAMETROTIPO',3,'p_parametro_tipo_id','gramatica.py',250),
  ('PARAMETROTIPO -> ID','PARAMETROTIPO',1,'p_parametro_tipo_id','gramatica.py',251),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','gramatica.py',259),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',265),
  ('instruccion -> imprimir_instr','instruccion',1,'p_instruccion','gramatica.py',272),
  ('instruccion -> declaracion_instr','instruccion',1,'p_instruccion','gramatica.py',273),
  ('instruccion -> llamada_instr','instruccion',1,'p_instruccion','gramatica.py',274),
  ('instruccion -> struct_instr','instruccion',1,'p_instruccion','gramatica.py',275),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','gramatica.py',276),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','gramatica.py',277),
  ('instruccion -> break_instr','instruccion',1,'p_instruccion','gramatica.py',278),
  ('instruccion -> continue_instr','instruccion',1,'p_instruccion','gramatica.py',279),
  ('instruccion -> return_instr','instruccion',1,'p_instruccion','gramatica.py',280),
  ('instruccion -> for_instr','instruccion',1,'p_instruccion','gramatica.py',281),
  ('imprimir_instr -> RPRINT PARA PARAMETROS PARC','imprimir_instr',4,'p_imprimir','gramatica.py',287),
  ('declaracion_instr -> ID IGUAL expresion','declaracion_instr',3,'p_declaracion','gramatica.py',292),
  ('declaracion_instr -> ID DOSPTS TIPO IGUAL expresion','declaracion_instr',5,'p_declaracion2','gramatica.py',296),
  ('declaracion_instr -> ID ACCESOLISTA IGUAL expresion','declaracion_instr',4,'p_declaracion3','gramatica.py',301),
  ('declaracion_instr -> GETSTRUCTS IGUAL expresion','declaracion_instr',3,'p_declaracion4','gramatica.py',306),
  ('funcion_instr -> RDEF ID PARA PARC DOSPTS instrucciones','funcion_instr',6,'p_funciones','gramatica.py',311),
  ('funcion_instr -> RDEF ID PARA PARAMETROSTIPO PARC DOSPTS instrucciones','funcion_instr',7,'p_funciones','gramatica.py',312),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada_instr','gramatica.py',322),
  ('llamada_instr -> ID PARA PARAMETROS PARC','llamada_instr',4,'p_llamada_instr','gramatica.py',323),
  ('llamada_expre -> ID PARA PARC','llamada_expre',3,'p_llamada_expresion','gramatica.py',331),
  ('llamada_expre -> ID PARA PARAMETROS PARC','llamada_expre',4,'p_llamada_expresion','gramatica.py',332),
  ('LISTA -> CORCHA PARAMETROS CORCHC','LISTA',3,'p_listas','gramatica.py',340),
  ('ACCESOLISTA -> ACCESOLISTA ITEMLISTA','ACCESOLISTA',2,'p_acceso_lista','gramatica.py',345),
  ('ACCESOLISTA -> ITEMLISTA','ACCESOLISTA',1,'p_acceso_lista2','gramatica.py',350),
  ('ITEMLISTA -> CORCHA expresion CORCHC','ITEMLISTA',3,'p_item_lista','gramatica.py',354),
  ('struct_instr -> RMUTABLE RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC','struct_instr',5,'p_instr_struct','gramatica.py',359),
  ('struct_instr -> RMUTABLE RSTRUCT ID LLAVEC','struct_instr',4,'p_instr_struct','gramatica.py',360),
  ('struct_instr -> RSTRUCT ID ATRIBUTOSSTRUCT LLAVEC','struct_instr',4,'p_instr_struct','gramatica.py',361),
  ('struct_instr -> RSTRUCT ID LLAVEC','struct_instr',3,'p_instr_struct','gramatica.py',362),
  ('ATRIBUTOSSTRUCT -> ATRIBUTOSSTRUCT ATRIBSTRUCT PUNTOCOMA','ATRIBUTOSSTRUCT',3,'p_atrib_struct','gramatica.py',375),
  ('ATRIBUTOSSTRUCT -> ATRIBSTRUCT PUNTOCOMA','ATRIBUTOSSTRUCT',2,'p_atrib_struct2','gramatica.py',380),
  ('ATRIBSTRUCT -> ID DOSPTS TIPO','ATRIBSTRUCT',3,'p_atrib_item','gramatica.py',384),
  ('ATRIBSTRUCT -> ID DOSPTS ID','ATRIBSTRUCT',3,'p_atrib_item','gramatica.py',385),
  ('ATRIBSTRUCT -> ID','ATRIBSTRUCT',1,'p_atrib_item','gramatica.py',386),
  ('GETSTRUCTS -> GETSTRUCTS PUNTO GETSTRUCT','GETSTRUCTS',3,'p_get_struct','gramatica.py',393),
  ('GETSTRUCTS -> GETSTRUCT','GETSTRUCTS',1,'p_get_strct2','gramatica.py',398),
  ('GETSTRUCT -> ID','GETSTRUCT',1,'p_get_item','gramatica.py',402),
  ('if_instr -> RIF expresion DOSPTS instrucciones LLAVEC','if_instr',5,'p_if_instr','gramatica.py',407),
  ('if_instr -> RIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVEC','if_instr',9,'p_if_instr2','gramatica.py',411),
  ('if_instr -> RIF expresion DOSPTS instrucciones LLAVEC lista_elif','if_instr',6,'p_if_instr3','gramatica.py',414),
  ('lista_elif -> lista_elif elif_inst','lista_elif',2,'p_lista_elif','gramatica.py',418),
  ('lista_elif -> elif_inst','lista_elif',1,'p_lista_elif2','gramatica.py',423),
  ('elif_inst -> RELIF expresion DOSPTS instrucciones LLAVEC','elif_inst',5,'p_lista_elif_item','gramatica.py',427),
  ('elif_inst -> RELIF expresion DOSPTS instrucciones LLAVEC RELSE DOSPTS instrucciones LLAVEC','elif_inst',9,'p_lista_elif_item2','gramatica.py',431),
  ('elif_inst -> RELIF expresion DOSPTS instrucciones LLAVEC lista_elif','elif_inst',6,'p_lista_elif_item3','gramatica.py',435),
  ('while_instr -> RWHILE expresion DOSPTS instrucciones LLAVEC','while_instr',5,'p_while_instr','gramatica.py',440),
  ('break_instr -> RBREAK','break_instr',1,'p_break_instr','gramatica.py',445),
  ('continue_instr -> RCONTINUE','continue_instr',1,'p_continue_instr','gramatica.py',450),
  ('return_instr -> RRETURN expresion','return_instr',2,'p_return_instr','gramatica.py',455),
  ('for_instr -> RFOR ID RIN expresion DOSPTS instrucciones LLAVEC','for_instr',7,'p_for_instr','gramatica.py',460),
  ('TIPO -> RINT','TIPO',1,'p_tipo','gramatica.py',465),
  ('TIPO -> RFLOAT','TIPO',1,'p_tipo','gramatica.py',466),
  ('TIPO -> RBOOLEAN','TIPO',1,'p_tipo','gramatica.py',467),
  ('TIPO -> RSTRING','TIPO',1,'p_tipo','gramatica.py',468),
  ('TIPO -> ID','TIPO',1,'p_tipo','gramatica.py',469),
  ('TIPO -> RLIST','TIPO',1,'p_tipo','gramatica.py',470),
  ('expresion -> expresion MAS expresion','expresion',3,'p_aritmeticas','gramatica.py',488),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_aritmeticas','gramatica.py',489),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_aritmeticas','gramatica.py',490),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_aritmeticas','gramatica.py',491),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_aritmeticas','gramatica.py',492),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_aritmeticas','gramatica.py',493),
  ('expresion -> expresion PUNTO expresion','expresion',3,'p_aritmeticas','gramatica.py',494),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_relacionales','gramatica.py',513),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_relacionales','gramatica.py',514),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',515),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',516),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_relacionales','gramatica.py',517),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_relacionales','gramatica.py',518),
  ('expresion -> expresion RAND expresion','expresion',3,'p_logicas','gramatica.py',537),
  ('expresion -> expresion ROR expresion','expresion',3,'p_logicas','gramatica.py',538),
  ('expresion -> RNOT expresion','expresion',2,'p_expre_not','gramatica.py',545),
  ('expresion -> MENOS expresion','expresion',2,'p_negacion','gramatica.py',551),
  ('expresion -> PARA expresion PARC','expresion',3,'p_parentesis','gramatica.py',556),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','gramatica.py',561),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','gramatica.py',565),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','gramatica.py',569),
  ('expresion -> ID','expresion',1,'p_expresion_id','gramatica.py',573),
  ('expresion -> RTRUE','expresion',1,'p_expresion_bool','gramatica.py',577),
  ('expresion -> RFALSE','expresion',1,'p_expresion_bool','gramatica.py',578),
  ('expresion -> RNULO','expresion',1,'p_expresion_bool','gramatica.py',579),
  ('expresion -> LISTA','expresion',1,'p_expresion_lista','gramatica.py',589),
  ('expresion -> ID ACCESOLISTA','expresion',2,'p_expresion_accesolst','gramatica.py',593),
  ('expresion -> llamada_expre','expresion',1,'p_expresion_llamada','gramatica.py',598),
]
