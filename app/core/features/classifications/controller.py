from core.features.classifications.model import Model
from core.features.classifications.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)

    def sendQuery(self):
        id = self.view.id.get()
        name = self.view.name.get()
        segment = self.view.segment.get()
        segmentid = self.view.segmentid.get()

        self.model.fillDict(id, name, segment, segmentid)

        msg.showinfo('','Condições adicionadas à consulta!')