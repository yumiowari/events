from tkinter import messagebox as msg
import pickle as pkl

class Model:
    def __init__(self):
        self.dict = {
            'id': '',
            'name': '',
            'startDateSale': '',
            'endDateSale': '',
            'startDateEvent': '',
            'timezone': '',
            'minPrice': '',
            'maxPrice': '',
            'promoter': ''
        }

    def fillDict(self, id, name, startDateSale, endDateSale, startDateEvent, timezone, minPrice, maxPrice, promoter):
        self.dict['id'] = id
        self.dict['name'] = name
        self.dict['startDateSale'] = startDateSale
        self.dict['endDateSale'] = endDateSale
        self.dict['startDateEvent'] = startDateEvent
        self.dict['timezone'] = timezone
        self.dict['minPrice'] = minPrice
        self.dict['maxPrice'] = maxPrice
        self.dict['promoter'] = promoter

        with open('data/event.pkl', 'wb') as file:
            pkl.dump(self.dict, file)

        msg.showinfo('','Condições adicionadas à consulta!')