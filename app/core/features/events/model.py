from tkinter import messagebox as msg
import pickle as pkl

class Model:
    def __init__(self):
        self.dict = {
            'id': '',
            'name': '',
            'startdatesale': '',
            'enddatesale': '',
            'startdateevent': '',
            'timezone': '',
            'minprice': '',
            'maxprice': '',
            'promoter': ''
        }

    def fillDict(self, id, name, startdatesale, enddatesale, startdateevent, timezone, minprice, maxprice, promoter):
        self.dict['id'] = id
        self.dict['name'] = name
        self.dict['startdatesale'] = startdatesale
        self.dict['enddatesale'] = enddatesale
        self.dict['startdateevent'] = startdateevent
        self.dict['timezone'] = timezone
        self.dict['minprice'] = minprice
        self.dict['maxprice'] = maxprice
        self.dict['promoter'] = promoter

        with open('data/event.pkl', 'wb') as file:
            pkl.dump(self.dict, file)

        msg.showinfo('','Condições adicionadas à consulta!')