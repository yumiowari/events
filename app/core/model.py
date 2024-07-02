from tkinter import messagebox as msg
import pickle as pkl
import os

from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Float, ForeignKey, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from core.mapeamento import *

class Model:
    def __init__(self):
        self.attractionDict = {
            'id': '',
            'name': ''
        }

        self.classificationDict = {
            'id': '',
            'name': '',
            'segment': '',
            'segmentid': ''
        }

        self.eventDict = {
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

        self.venueDict = {
            'id': '',
            'name': '',
            'postalcode': '',
            'timezone': '',
            'city': '',
            'state': '',
            'country': '',
            'address': ''
        }

        # conexão com o banco de dados
        self.engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/ticketmaster")
        self.base = declarative_base
        self.session = sessionmaker(bind = self.engine)
        #

    def makeAdHoc(self):
        attractionDict = self.attractionDict
        classificationDict = self.classificationDict
        eventDict = self.eventDict
        venueDict = self.venueDict

        if os.path.isfile('data/attraction.pkl'):
            with open('data/attraction.pkl', 'rb') as file:
                attractionDict = dict(pkl.load(file))

        if os.path.isfile('data/classification.pkl'):  
            with open('data/classification.pkl', 'rb') as file:
                classificationDict = dict(pkl.load(file))

        if os.path.isfile('data/event.pkl'):  
            with open('data/event.pkl', 'rb') as file:
                eventDict = dict(pkl.load(file))

        if os.path.isfile('data/venue.pkl'):  
            with open('data/venue.pkl', 'rb') as file:
                venueDict = dict(pkl.load(file))

        # faz a consulta dinâmica
        session = self.session()

        ## preenche as condições
        conditions = []
        relations = []
        globalFlag = False # infere se já iniciou a query

        ### attractions
        localFlag = False # infere se a tabela já foi concatenada

        if attractionDict['id'] != '':
            conditions.append(Attraction.id == attractionDict['id'])
            localFlag = True
        if attractionDict['name'] != '':
            conditions.append(Attraction.name == attractionDict['name'])
            localFlag = True

        if localFlag == True:
            query = session.query(Attraction)
            globalFlag = True

            relations.append(self.attractionDict)
        ###

        ### classifications
        localFlag = False

        if classificationDict['id'] != '':
            conditions.append(Classification.id == classificationDict['id'])
            localFlag = True
        if classificationDict['name'] != '':
            conditions.append(Classification.name == classificationDict['name'])
            localFlag = True
        if classificationDict['segment'] != '':
            conditions.append(Classification.segmentname == classificationDict['segment'])
            localFlag = True
        if classificationDict['segmentid'] != '':
            conditions.append(Classification.segmentid == classificationDict['segmentid'])
            localFlag = True

        if localFlag == True:
            if globalFlag == False:
                query = session.query(Classification)
                globalFlag = True
            else:
                query = query.join(Classification)

            relations.append(self.classificationDict)
        ###

        ### events
        localFlag = False

        if eventDict['id'] != '':
            conditions.append(Event.id == eventDict['id'])
            localFlag = True
        if eventDict['name'] != '':
            conditions.append(Event.name == eventDict['name'])
            localFlag = True
        if eventDict['startdatesale'] != '':
            conditions.append(Event.startdatesale == eventDict['startdatesale'])
            localFlag = True
        if eventDict['enddatesale'] != '':
            conditions.append(Event.enddatesale == eventDict['enddatesale'])
            localFlag = True
        if eventDict['startdateevent'] != '':
            conditions.append(Event.startdateevent == eventDict['startdateevent'])
            localFlag = True
        if eventDict['timezone'] != '':
            conditions.append(Event.timezone == eventDict['timezone'])
            localFlag = True
        if eventDict['minprice'] != '':
            conditions.append(Event.minprice == eventDict['minprice'])
            localFlag = True
        if eventDict['maxprice'] != '':
            conditions.append(Event.maxprice == eventDict['maxprice'])
            localFlag = True
        if eventDict['promoter'] != '':
            conditions.append(Event.promoter == eventDict['promoter'])
            localFlag = True

        if localFlag == True:
            if globalFlag == False:
                query = session.query(Event)
                globalFlag = True
            else:
                query = query.join(Event)

            relations.append(self.eventDict)
        ###

        ### venues
        localFlag = False

        if venueDict['id'] != '':
            conditions.append(Venue.id == venueDict['id'])
            localFlag = True
        if venueDict['name'] != '':
            conditions.append(Venue.name == venueDict['name'])
            localFlag = True
        if venueDict['postalcode'] != '':
            conditions.append(Venue.postalcode == venueDict['postalcode'])
            localFlag = True
        if venueDict['timezone'] != '':
            conditions.append(Venue.timezone == venueDict['timezone'])
            localFlag = True
        if venueDict['city'] != '':
            conditions.append(Venue.city == venueDict['city'])
            localFlag = True
        if venueDict['state'] != '':
            conditions.append(Venue.state == venueDict['state'])
            localFlag = True
        if venueDict['address'] != '':
            conditions.append(Venue.address == venueDict['address'])
            localFlag = True

        if localFlag == True:
            if globalFlag == False:
                query = session.query(Venue)
                globalFlag = True
            else:
                query = query.join(Venue)

            relations.append(self.venueDict)
        ###

        if globalFlag == True:
            if conditions:
                query = query.filter(and_(*conditions))

            results = query.all()

            self.showResults(results, relations)

            msg.showinfo('','Consulta realizada com sucesso.')
        else:
            msg.showerror('','Nenhuma condição foi informada.')

        session.close()
        ##

        #

    def showResults(self, results, relations):
        if not results:
            print("Nenhuma tupla foi encontrada.")
            return

        for result in results:
            print("Resultado:")
            for relation in relations:
                for key, value in relation.items():
                    print(f"{key}: {getattr(result, key, 'N/A')}")
                print()
            print("-------------------------")