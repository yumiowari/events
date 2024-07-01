import tkinter as tk
from tkinter import ttk

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Attractions")
        self.root.geometry("800x600")

        self.top = tk.Frame(self.root)
        self.base = tk.Frame(self.root)

        # identificador
        self.id = tk.StringVar(value = '')

        self.idLabel = tk.Label(self.top, text = 'Identificador da atração:')
        self.idEntry = tk.Entry(self.top, textvariable = self.id)

        self.idLabel.pack()
        self.idEntry.pack()
        #

        # nome
        self.name = tk.StringVar(value = '')

        self.nameLabel = tk.Label(self.top, text = 'Nome da atração:')
        self.nameEntry = tk.Entry(self.top, textvariable = self.name)

        self.nameLabel.pack()
        self.nameEntry.pack()
        #

        # botão de confirmação
        self.confirm = tk.Button(self.base, text="Enviar", command=self.controller.sendQuery)

        self.confirm.pack()
        #

        self.top.pack(side=tk.TOP)
        self.base.pack(side=tk.BOTTOM)