import tkinter as tk
from tkinter import ttk

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Events")
        self.root.geometry("800x600")

        self.top = tk.Frame(self.root)
        self.base = tk.Frame(self.root)

        # identificador
        self.id = tk.StringVar(value = '')

        self.idLabel = tk.Label(self.top, text = 'Identificador do evento:')
        self.idEntry = tk.Entry(self.top, textvariable = self.id)

        self.idLabel.pack()
        self.idEntry.pack()
        #

        # nome
        self.name = tk.StringVar(value = '')

        self.nameLabel = tk.Label(self.top, text = 'Nome do evento:')
        self.nameEntry = tk.Entry(self.top, textvariable = self.name)

        self.nameLabel.pack()
        self.nameEntry.pack()
        #

        # inicio da bilheteria
        self.startDateSale = tk.StringVar(value = '')

        self.startDateSaleLabel = tk.Label(self.top, text = "Data de início da bilheteria do evento:")
        self.startDateSaleEntry = tk.Entry(self.top, textvariable = self.startDateSale)

        self.startDateSaleLabel.pack()
        self.startDateSaleEntry.pack()
        #

        # fim da bilheteria
        self.endDateSale = tk.StringVar(value = '')

        self.endDateSaleLabel = tk.Label(self.top, text = "Data de fim da bilheteria do evento:")
        self.endDateSaleEntry = tk.Entry(self.top, textvariable = self.endDateSale)

        self.endDateSaleLabel.pack()
        self.endDateSaleEntry.pack()
        #

        # inicio do evento
        self.startDateEvent = tk.StringVar(value = '')

        self.startDateEventLabel = tk.Label(self.top, text = "Data de início do evento:")
        self.startDateEventEntry = tk.Entry(self.top, textvariable = self.startDateEvent)

        self.startDateEventLabel.pack()
        self.startDateEventEntry.pack()
        #

        # fuso horário
        self.timezone = tk.StringVar(value = '')

        self.timezoneLabel = tk.Label(self.top, text = "Fuso horário do local:")
        self.timezoneEntry = tk.Entry(self.top, textvariable = self.timezone)

        self.timezoneLabel.pack()
        self.timezoneEntry.pack()
        #

        # preço mínimo
        self.minPrice = tk.StringVar(value = '')

        self.minPriceLabel = tk.Label(self.top, text = "Preço mínimo do evento:")
        self.minPriceEntry = tk.Entry(self.top, textvariable = self.minPrice)

        self.minPriceLabel.pack()
        self.minPriceEntry.pack()
        #

        # preço máximo
        self.maxPrice = tk.StringVar(value = '')

        self.maxPriceLabel = tk.Label(self.top, text = "Preço máximo do evento:")
        self.maxPriceEntry = tk.Entry(self.top, textvariable = self.maxPrice)

        self.maxPriceLabel.pack()
        self.maxPriceEntry.pack()
        #

        # promotor
        self.promoter = tk.StringVar(value = '')

        self.promoterLabel = tk.Label(self.top, text = "Promotor do evento:")
        self.promoterEntry = tk.Entry(self.top, textvariable = self.promoter)

        self.promoterLabel.pack()
        self.promoterEntry.pack()
        #

        # botão de confirmação
        self.confirm = tk.Button(self.base, text="Enviar", command=self.controller.sendQuery)

        self.confirm.pack()
        #

        self.top.pack(side=tk.TOP)
        self.base.pack(side=tk.BOTTOM)