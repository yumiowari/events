from core.features.venues.model import Model
from core.features.venues.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)

    def sendQuery(self):
        id = self.view.id.get()
        name = self.view.name.get()
        postalCode = self.view.postalCode.get()
        timezone = self.view.timezone.get()
        city = self.view.city.get()
        state = self.view.state.get()
        address = self.view.address.get()

        self.model.fillDict(id, name, postalCode, timezone, city, state, address)

        msg.showinfo('','Condições adicionadas à consulta!')