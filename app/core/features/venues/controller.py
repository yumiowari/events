from core.features.venues.model import Model
from core.features.venues.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)

    def sendQuery(self):
        pass