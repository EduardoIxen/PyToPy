from src.optimizador.instrucciones.Label import Label
from src.optimizador.Blocks import Blocks
from src.optimizador.instrucciones.Assignment import Assignment
from src.optimizador.gotos.Goto import Goto
from src.optimizador.gotos.IF import IF


class Optimizador():
    reglas = []

    def __init__(self, packages, temps, code):
        self.packages = packages
        self.temps = temps
        self.code = code
        self.blocks = []

    def get_code(self):
        ret = f'package main;\n\nimport(\n\t"{self.packages}"\n);\n'
        for temp in self.temps:
            ret = ret + f'var {temp}\n'
        ret = ret + '\n'

        for func in self.code:
            ret = ret + func.get_code()+'\n\n'
        return ret

    def Mirilla(self):
        for func in self.code:
            tamano = 20
            while tamano <= len(func.instr):
                flag_opt = False
                for i in range(10):
                    aux = 0
                    while (tamano+aux) <= len(func.instr):
                        flag_opt = flag_opt or self.Regla3(
                            func.instr[0+aux:tamano+aux])
                        flag_opt = flag_opt or self.Regla6(
                            func.instr[0+aux:tamano+aux])
                        aux = aux+1

    def Bloques(self):
        self.blocks = []
        self.GenerarBloques()

    def GenerarBloques(self):
        self.GenerarLideres()
        self.CrearBloques()
        self.ConnectBloques()

    def GenerarLideres(self):
        #Por cada funcion
        print("Lideres")
        for func in self.code:
            #la primera instruccion de tres direcciones en el codigo intermedio es líder
            func.instr[0].is_leader = True

            #cualquier instruccion que siga despues de un salgo condicional o incondicional es lider
            flag = False
            for instr in func.instr:
                if flag:
                    instr.is_leader = True
                    flag = False
                if type(instr) is Goto or type(instr) is IF:
                    flag = True

    def CrearBloques(self):
        #Por cada funcion
        print("Creacion de bloques")
        for func in self.code:
            #Bloques de la funcion actual
            blocks = []
            block = None
            for instr in func.instr:
                if instr.is_leader:
                    #Si hay un bloque creado. Agregarlo al arreglo de bloques
                    if block is not None:
                        blocks.append(block)
                    block = Blocks(instr)
                block.code.append(instr)
            #EOF
            blocks.append(block)
            #Guardar los bloques de la funcion
            self.blocks.append(blocks)

    def ConnectBloques(self):
        #Por cada arreglo de bloques en una funcion
        print("Conexion de bloques")
        for func in self.blocks:
            prev_block = None
            #Por cada bloque en la funcion. Se unen en cascada
            for block in func:
                if prev_block is None:
                    prev_block = block
                    continue
                prev_block.nexts.append(block)
                prev_block = block
            #Revisar los saltos entre bloques
            for block in func:
                #Obtener la ultima instruccion
                last_ins = block.code[len(block.code)-1]
                if type(last_ins) is Goto or type(last_ins) is IF:
                    label = last_ins.label
                    #Revisar todos los bloques
                    for check in func:
                        if type(check.first) is Label and check.first.id == label:
                            block.nexts.append(check)
                            break

    def Regla1(self, arreglo):
        print("Regla 1")
        ret = False
        for i in range(len(arreglo)):
            actual = arreglo[i]

        return ret

    def Regla2(self, arreglo):
        print("Regla 2")
        ret = False
        return ret

    def Regla3(self, arreglo):
        ret = False
        for i in range(len(arreglo)):
            actual = arreglo[i]
            if type(actual) is IF and not actual.deleted:
                if i+1 < len(arreglo):
                    next_inst = arreglo[i+1]
                else:
                    return ret
                if type(next_inst) is Goto and not next_inst.deleted and i+2 < len(arreglo):
                    actual.condition.get_contrary()
                    actual.label = next_inst.label
                    next_inst.deleted = True
                    arreglo[i+2].deleted = True
                    ret = True
                    print("Regla 3")
        return ret

    def Regla4(self, arreglo):
        print("Regla 4")
        ret = False
        return ret

    def Regla5(self, arreglo):
        print("Regla 5")
        ret = False
        return ret

    def Regla6(self, arreglo):
        ret = False
        for i in range(len(arreglo)):
            actual = arreglo[i]
            if type(actual) is Assignment and not actual.deleted:
                if(actual.self_assigment()):
                    actual_opt = actual.exp.neutral_ops()
                    if actual_opt:
                        ret = True
                        actual.deleted = True
                        print("Regla 6")
        return ret

    def Regla7(self, arreglo):
        print("Regla 7")
        ret = False
        return ret

    def Regla8(self, arreglo):
        print("Regla 8")
        ret = False
        return ret
