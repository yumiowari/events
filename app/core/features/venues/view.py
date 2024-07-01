import tkinter as tk

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Venues")
        self.root.geometry("800x600")

        self.top = tk.Frame(self.root)
        self.base = tk.Frame(self.root)

        # identificador
        self.id = tk.StringVar(value = '')

        self.idLabel = tk.Label(self.top, text = 'Identificador do local:')
        self.idEntry = tk.Entry(self.top, textvariable = self.id)

        self.idLabel.pack()
        self.idEntry.pack()
        #

        # nome
        self.name = tk.StringVar(value = '')

        self.nameLabel = tk.Label(self.top, text = 'Nome do local:')
        self.nameEntry = tk.Entry(self.top, textvariable = self.name)

        self.nameLabel.pack()
        self.nameEntry.pack()
        #

        # código postal
        self.postalCode = tk.StringVar(value = '')

        self.postalCodeLabel = tk.Label(self.top, text = "Código postal do local:")
        self.postalCodeEntry = tk.Entry(self.top, textvariable = self.postalCode)

        self.postalCodeLabel.pack()
        self.postalCodeEntry.pack()
        #

        # fuso horário
        self.timezone = tk.StringVar(value = '')

        self.timezoneLabel = tk.Label(self.top, text = "Fuso horário do local:")
        self.timezoneEntry = tk.Entry(self.top, textvariable = self.timezone)

        self.timezoneLabel.pack()
        self.timezoneEntry.pack()
        #

        # cidade
        self.city = tk.StringVar(value = '')

        self.cityLabel = tk.Label(self.top, text = "Cidade do local:")
        self.cityEntry = tk.Entry(self.top, textvariable = self.city)

        self.cityLabel.pack()
        self.cityEntry.pack()
        #

        # estado
        self.state = tk.StringVar(value = '')

        self.stateLabel = tk.Label(self.top, text = "Estado do local:")
        self.stateEntry = tk.Entry(self.top, textvariable = self.state)

        self.stateLabel.pack()
        self.stateEntry.pack()
        #

        # address
        self.address = tk.StringVar(value = '')

        self.addressLabel = tk.Label(self.top, text = "Endereço do local:")
        self.addressEntry = tk.Entry(self.top, textvariable = self.address)

        self.addressLabel.pack()
        self.addressEntry.pack()
        #

        # botão de confirmação
        self.confirm = tk.Button(self.base, text="Enviar", command=self.controller.sendQuery)

        self.confirm.pack()
        #

        self.top.pack(side=tk.TOP)
        self.base.pack(side=tk.BOTTOM)