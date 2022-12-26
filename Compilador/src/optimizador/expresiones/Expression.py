from src.optimizador.C3DInstruction import C3DInstruction


class Expression(C3DInstruction):
    def __init__(self, left, right, type_op, line, column):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self.type_op = type_op
        self.constant = left.constant or right.constant

    def neutral_ops(self):
        if self.type_op == '+' or self.type_op == '-':
            self.deleted = self.right.get_code() == '0' or self.left.get_code() == '0'
        elif self.type_op == '*':
            self.deleted = self.right.get_code() == '1' or self.left.get_code() == '1'
        elif self.type_op == '/':
            self.deleted = self.right.get_code() == '1'
        return self.deleted

    def get_contrary(self):
        if self.type_op == '>':
            self.type_op = '<='
        elif self.type_op == '<':
            self.type_op = '>='
        elif self.type_op == '>=':
            self.type_op = '<'
        elif self.type_op == '<=':
            self.type_op = '>'
        elif self.type_op == '==':
            self.type_op = '!='
        elif self.type_op == '!=':
            self.type_op = '=='
        else:
            self.type_op = ''

    def get_code(self):
        if self.type_op != '%':
            return f'{self.left.get_code()}{self.type_op}{self.right.get_code()}'
        else:
            return f'math.Mod({self.left.get_code()},{self.right.get_code()})'
