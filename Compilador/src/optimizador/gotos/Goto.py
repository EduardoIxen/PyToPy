from src.optimizador.C3DInstruction import C3DInstruction


class Goto(C3DInstruction):
    def __init__(self, label, line, column):
        super().__init__(line, column)
        self.label = label

    def get_code(self):
        if self.deleted:
            return ''
        return f'goto {self.label}'
