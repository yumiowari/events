from core.features.classifications.model import Model
from core.features.classifications.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)

    def sendQuery(self):
        pass