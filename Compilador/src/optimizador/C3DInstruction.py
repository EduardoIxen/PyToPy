from abc import ABC, abstractmethod


class C3DInstruction(ABC):
    def __init__(self, line, column):
        self.line = line
        self.column = column
        self.have_int = False
        self.deleted = False
        self.is_leader = False

    @abstractmethod
    def get_code(self):
        pass
