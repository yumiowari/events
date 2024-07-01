import pickle as pkl

class Model:
    def __init__(self):
        self.dict = {
            'id': '',
            'name': '',
            'segment': '',
            'segmentid': ''
        }

    def fillDict(self, id, name, segment, segmentid):
        self.dict['id'] = id
        self.dict['name'] = name
        self.dict['segment'] = segment
        self.dict['segmentid'] = segmentid

        with open('data/classification.pkl', 'wb') as file:
            pkl.dump(self.dict, file)