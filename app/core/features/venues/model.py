from tkinter import messagebox as msg
import pickle as pkl

class Model:
    def __init__(self):
        self.dict = {
            'id': '',
            'name': '',
            'postalcode': '',
            'timezone': '',
            'city': '',
            'state': '',
            'address': ''
        }

    def fillDict(self, id, name, postalcode, timezone, city, state, address):
        self.dict['id'] = id
        self.dict['name'] = name
        self.dict['postalcode'] = postalcode
        self.dict['timezone'] = timezone
        self.dict['city'] = city
        self.dict['state'] = state
        self.dict['address'] = address

        with open('data/venue.pkl', 'wb') as file:
            pkl.dump(self.dict, file)

        msg.showinfo('','Condições adicionadas à consulta!')