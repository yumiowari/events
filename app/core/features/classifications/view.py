import tkinter as tk
from tkinter import ttk

class View():
    def __init__(self, root, controller):
        self.root = tk.Toplevel(root)

        self.controller = controller

        self.root.title("Classifications")
        self.root.geometry("800x600")