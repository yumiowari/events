from core.features.attractions.model import Model
from core.features.attractions.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)