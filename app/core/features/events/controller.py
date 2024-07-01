from core.features.events.model import Model
from core.features.events.view import View

class Controller:
    def __init__(self, root):
        self.root = root

        self.model = Model()
        self.view = View(self.root, self)

    def sendQuery(self):
        id = self.view.id.get()
        name = self.view.name.get()
        startDateSale = self.view.startDateSale.get()
        endDateSale = self.view.endDateSale.get()
        startDateEvent = self.view.startDateEvent.get()
        timezone = self.view.timezone.get()
        minPrice = self.view.minPrice.get()
        maxPrice = self.view.maxPrice.get()
        promoter = self.view.promoter.get()

        self.model.fillDict(id, name, startDateSale, endDateSale, startDateEvent, timezone, minPrice, maxPrice, promoter)