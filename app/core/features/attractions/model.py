from tkinter import messagebox as msg
import pickle as pkl

class Model:
    def __init__(self):
        self.dict = {
            'id': '',
            'name': ''
        }

    def fillDict(self, id, name):
        self.dict['id'] = id
        self.dict['name'] = name

        with open('data/attraction.pkl', 'wb') as file:
            pkl.dump(self.dict, file)

        msg.showinfo('','Condições adicionadas à consulta!')