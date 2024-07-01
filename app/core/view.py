import tkinter as tk

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Ad-Hoc")
        self.root.geometry("400x300")

        self.menubar = tk.Menu(self.root)

        self.ordermenu = tk.Menu(self.menubar, tearoff=0)
        self.ordermenu.add_command(label="Attractions", command=self.controller.readAttractions)
        self.ordermenu.add_command(label="Classifications", command=self.controller.readClassifications)
        self.ordermenu.add_command(label="Events", command=self.controller.readEvents)
        self.ordermenu.add_command(label="Venues", command=self.controller.readVenues)
        self.menubar.add_cascade(label="Consultar", menu=self.ordermenu)

        self.root.config(menu=self.menubar)

        # botão de confirmação
        self.confirm = tk.Button(self.root, text="Enviar", command=self.controller.makeAdHoc)

        self.confirm.pack(side = tk.BOTTOM)
        #