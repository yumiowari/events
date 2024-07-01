import tkinter as tk

from core.model import Model
from core.view import View

from core.features.attractions.controller import Controller as CtrlAttractions
from core.features.classifications.controller import Controller as CtrlClassifications
from core.features.events.controller import Controller as CtrlEvents
from core.features.venues.controller import Controller as CtrlVenues

class Controller:
    def __init__(self):
        self.root = tk.Tk()

        self.model = Model()
        self.view = View(self.root, self)

        self.root.mainloop()

    def readAttractions(self):
        self.ctrlAttractions = CtrlAttractions(self.root)

    def readClassifications(self):
        self.ctrlClassifications = CtrlClassifications(self.root)

    def readEvents(self):
        self.ctrlEvents = CtrlEvents(self.root)
        
    def readVenues(self):
        self.ctrlVenues = CtrlVenues(self.root)

    def makeAdHoc(self):
        self.model.makeAdHoc()
