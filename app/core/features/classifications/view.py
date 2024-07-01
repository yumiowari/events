import tkinter as tk

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Classifications")
        self.root.geometry("800x600")

        self.top = tk.Frame(self.root)
        self.base = tk.Frame(self.root)

        # identificador
        self.id = tk.StringVar(value = '')

        self.idLabel = tk.Label(self.top, text = 'Identificador da classificação:')
        self.idEntry = tk.Entry(self.top, textvariable = self.id)

        self.idLabel.pack()
        self.idEntry.pack()
        #

        # nome
        self.name = tk.StringVar(value = '')

        self.nameLabel = tk.Label(self.top, text = 'Nome da classificação:')
        self.nameEntry = tk.Entry(self.top, textvariable = self.name)

        self.nameLabel.pack()
        self.nameEntry.pack()
        #

        # nome do segmento
        self.segment = tk.StringVar(value = '')

        self.segmentLabel = tk.Label(self.top, text = "Nome do segmento da classificação:")
        self.segmentEntry = tk.Entry(self.top, textvariable = self.segment)

        self.segmentLabel.pack()
        self.segmentEntry.pack()
        #

        # identificador do segmento
        self.segmentid = tk.StringVar(value = '')

        self.segmentidLabel = tk.Label(self.top, text = "Identificador do segmento da classificação:")
        self.segmentidEntry = tk.Entry(self.top, textvariable = self.segmentid)

        self.segmentidLabel.pack()
        self.segmentidEntry.pack()
        #

        # botão de confirmação
        self.confirm = tk.Button(self.base, text="Enviar", command=self.controller.sendQuery)

        self.confirm.pack()
        #

        self.top.pack(side=tk.TOP)
        self.base.pack(side=tk.BOTTOM)