class Blocks:
    def __init__(self, first_instr):
        # Primera instruccion del codigo
        self.first = first_instr
        # Bloques siguientes a este
        self.nexts = []
        self.code = []
