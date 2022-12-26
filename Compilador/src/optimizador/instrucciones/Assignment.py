from src.optimizador.expresiones.Literal import Literal
from src.optimizador.C3DInstruction import C3DInstruction
from src.optimizador.expresiones.Access import Access

class Assignment(C3DInstruction):
    def __init__(self, place, exp, line, column):
        super().__init__(line, column)
        self.place = place
        self.exp = exp

    def self_assignment(self):
        if type(self.exp) is Literal or type(self.exp) is Access:
            aux = self.place.get_code() == self.exp.get_code()
        else:
            aux = self.place.get_code() == self.exp.right.get_code(
            ) or self.place.get_code() == self.exp.left.get_code()
        return aux

    def get_code(self):
        if self.deleted:
            return ''
        return f'{self.place.get_code()} = {self.exp.get_code()}'
