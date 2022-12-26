from src.optimizador.C3DInstruction import C3DInstruction


class IF(C3DInstruction):
    def __init__(self, condition, label, line, column):
        super().__init__(line, column)
        self.condition = condition
        self.label = label

    def get_code(self):
        return f'if ({self.condition.get_code()}) {{goto {self.label};}}'
