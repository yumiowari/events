# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import StaleDataError
import uuid
from DAO import *
from mapeamento import *

import json
import requests
from datetime import datetime

class AcessDB:
    # Função de inserção no banco
    def insert(obj):
        try:
            session = DAO.getSession()
            DAO.insert(session, obj)
            session.commit()
            session.close()
            return 1
        except Exception as e:
            print(e)
            session.close()
            return 0

    # Funções para buscar um registro do banco
    def selectClassification(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            clas = DAOClassifications.select(session, id)
            session.commit()
            return clas
        except:
            return 0

    def selectVenue(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            clas = DAOVenues.select(session, id)
            session.commit()
            return clas
        except:
            return 0

    def selectEvent(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            clas = DAOEvents.select(session, id)
            session.commit()
            return clas
        except:
            return 0
        
    def selectAttraction(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOAttractions.select(session, id)
            session.commit()
            return org
        except:
            return 0
    
    def selectEventAttraction(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOEventAttraction.select(session, id)
            session.commit()
            return org
        except:
            return 0
    
    def selectVenueAlias(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOVenueAlias.select(session, id)
            session.commit()
            return org
        except:
            return 0
        
    def selectMarket(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOMarket.select(session, id)
            session.commit()
            return org
        except:
            return 0
        
    def selectVenueImage(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOVenueImage.select(session, id)
            session.commit()
            return org
        except:
            return 0
        
    def selectEventImage(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOEventImage.select(session, id)
            session.commit()
            return org
        except:
            return 0
        
    def selectAttractionImage(id):
        try:
            session = DAO.getSession()
            session.expire_on_commit = False
            org = DAOAttractionImage.select(session, id)
            session.commit()
            return org
        except:
            return 0
    
class API:
    def __init__(self):
        self.manipulateDB = AcessDB


    def getClassifications(self):
        try:
            print('Fazendo a carga das classificações no banco...')
            response = requests.get("https://app.ticketmaster.com/discovery/v2/classifications.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page=0")
            classification_json = response.json()
            
            if len(classification_json) == 0:
                raise Exception('Json vazio')
            
            for clas in classification_json["_embedded"]["classifications"]:
                if 'segment' in clas:
                    segment_id = clas['segment']['id']
                    segment_nome = clas['segment']['name']

                    for genres in clas['segment']["_embedded"]['genres']:
                        
                        clasObject = Classification(id=genres['id'],
                                                name=genres['name'],
                                                segmentid=str(segment_id),
                                                segmentname=str(segment_nome)
                                            )
                        
                         #Verifica se o objeto já existe no banco
                        check = self.manipulateDB.selectClassification(clasObject.id)
                        id = str(clasObject.id)
                        #Se não existir, insere no banco
                        if not check:
                            self.manipulateDB.insert(clasObject)
                            print('Classification inserida no banco. ID: ' + id)
                        else:
                            print('Classification já existe no banco. ID: ' + id)
                    
                elif 'type' in clas:
                    segment_id = clas['type']['id']
                    segment_nome = clas['type']['name']

                    for types in clas['type']["_embedded"]['subtypes']:
                        
                        clasObject = Classification(id=types['id'],
                                                name=types['name'],
                                                segmentid=str(segment_id),
                                                segmentname=str(segment_nome)
                                            )
                        
                         #Verifica se o objeto já existe no banco
                        check = self.manipulateDB.selectClassification(clasObject.id)
                        id = str(clasObject.id)
                        #Se não existir, insere no banco
                        if not check:
                            self.manipulateDB.insert(clasObject)
                            print('Classificacao inserida no banco. ID: ' + id)
                        else:
                            print('Classificacao já existe no banco. ID: ' + id)
                    
               
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)
        
    def getVenues(self):
        try:
            print('Fazendo a carga das Venues no banco...')
            for page in range(0,10):
                url = f"https://app.ticketmaster.com/discovery/v2/venues.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page={page}&size=200"
                response = requests.get(url)
                venues_json = response.json()
            
                if len(venues_json) == 0:
                    raise Exception('Json vazio')

                
                for ven in venues_json["_embedded"]["venues"]:
                    

                    #Garantindo que os atributos não estão vazios
                    ven_url = ven['url'] if 'url' in ven else None
                    ven_address = ven['address']['line1'] if 'address' in ven and len(ven['address']) > 0 and 'line1' in ven['address'] else None

                    venObject = Venue(id=ven['id'],
                                            name=ven['name'],
                                            url=ven_url,
                                            postalcode=ven['postalCode'],
                                            timezone=ven['timezone'],
                                            city=ven['city']['name'],
                                            state=ven['state']['name'],
                                            country=ven['country']['name'],
                                            address=ven_address,
                                        )
                    
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectVenue(venObject.id)
                    id = str(venObject.id)
                    #Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(venObject)
                        print('Venue inserido no banco. ID: ' + id)
                    else:
                        print('Venue já existe no banco. ID: ' + id)

                    #Preencher tabela auxiliar de alias Venue
                    if 'aliases' in ven and len(ven['aliases']) > 0:
                        for alias in ven['aliases']:
                            ven_aliases = alias
                            aliasObject = VenueAlia(alias=ven_aliases,
                                                    venueid=ven['id'],
                                            )
                            #Verifica se o objeto já existe no banco
                            check = self.manipulateDB.selectVenueAlias(aliasObject.alias)
                            id = str(aliasObject.alias)
                            #Se não existir, insere no banco
                            if not check:
                                self.manipulateDB.insert(aliasObject)
                                print('Venue alias inserido no banco. ID: ' + id)
                            else:
                                print('Venue alias já existe no banco. ID: ' + id)

                    #Preencher tabela auxiliar de imagem Venue
                    if 'images' in ven and len(ven['images']) > 0:
                        for image in ven['images']:
                            ven_images = image['url']
                            imagesObject = VenueImage(image=ven_images,
                                                    venueid=ven['id'],
                                            )
                            #Verifica se o objeto já existe no banco
                            check = self.manipulateDB.selectVenueImage(imagesObject.image)
                            id = str(imagesObject.image)
                            #Se não existir, insere no banco
                            if not check:
                                self.manipulateDB.insert(imagesObject)
                                print('Venue image inserido no banco. ID: ' + id)
                            else:
                                print('Venue image já existe no banco. ID: ' + id)

                    # Preencher tabela de market
                    if 'markets' in ven and len(ven['markets']) > 0:
                        for market in ven['markets']:
                            ven_market = market['name']
                            marketObject = Market(id=ven_market+'/'+ven['id'],
                                                    market=ven_market,
                                                    venueid=ven['id'],
                                            )
                           
                            #Verifica se o objeto já existe no banco
                            check = self.manipulateDB.selectMarket(marketObject.id)
                            id = str(marketObject.id)
                            #Se não existir, insere no banco
                            if not check:
                                self.manipulateDB.insert(marketObject)
                                print('Venue market inserido no banco. ID: ' + id)
                            else:
                                print('Venue market já existe no banco. ID: ' + id)
                            
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)
        
    def getEvents(self):
        try:
            print('Fazendo a carga dos Events no banco...')
            for page in range(0,10):
                url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page={page}&size=200"
                response = requests.get(url)
                events_json = response.json()
                
                if len(events_json) == 0:
                    raise Exception('Json vazio')

                for event in events_json["_embedded"]["events"]:

                    # Preencher venue
                    for ven in event["_embedded"]["venues"]:

                        #Garantindo que os atributos não estão vazios
                        ven_url = ven['url'] if 'url' in ven else None
                        ven_address = ven['address']['line1'] if 'address' in ven and len(ven['address']) > 0 and 'line1' in ven['address'] else None
                        ven_state = ven['state']['name'] if 'state' in ven and len(ven['state']) > 0 and 'namw' in ven['state'] else None
                        ven_postal = ven['postalCode'] if 'postalCode' in ven else None

                        venObject = Venue(id=ven['id'],
                                                name=ven['name'],
                                                url=ven_url,
                                                postalcode=ven_postal,
                                                timezone=ven['timezone'],
                                                city=ven['city']['name'],
                                                state=ven_state,
                                                country=ven['country']['name'],
                                                address=ven_address,
                                            )
                        
                        #Verifica se o objeto já existe no banco
                        check = self.manipulateDB.selectVenue(venObject.id)
                        id = str(venObject.id)
                        #Se não existir, insere no banco
                        if not check:
                            self.manipulateDB.insert(venObject)
                            print('Venue inserido no banco. ID: ' + id)
                        else:
                            print('Venue já existe no banco. ID: ' + id)

                        #Preencher tabela auxiliar de alias Venue
                        if 'aliases' in ven and len(ven['aliases']) > 0:
                            for alias in ven['aliases']:
                                ven_aliases = alias
                                aliasObject = VenueAlia(alias=ven_aliases,
                                                        venueid=ven['id'],
                                                )
                                #Verifica se o objeto já existe no banco
                                check = self.manipulateDB.selectVenueAlias(aliasObject.alias)
                                id = str(aliasObject.alias)
                                #Se não existir, insere no banco
                                if not check:
                                    self.manipulateDB.insert(aliasObject)
                                    print('Venue alias inserido no banco. ID: ' + id)
                                else:
                                    print('Venue alias já existe no banco. ID: ' + id)

                        #Preencher tabela auxiliar de imagem Venue
                        if 'images' in ven and len(ven['images']) > 0:
                            for image in ven['images']:
                                ven_images = image['url']
                                imagesObject = VenueImage(image=ven_images,
                                                        venueid=ven['id'],
                                                )
                                #Verifica se o objeto já existe no banco
                                check = self.manipulateDB.selectVenueImage(imagesObject.image)
                                id = str(imagesObject.image)
                                #Se não existir, insere no banco
                                if not check:
                                    self.manipulateDB.insert(imagesObject)
                                    print('Venue image inserido no banco. ID: ' + id)
                                else:
                                    print('Venue image já existe no banco. ID: ' + id)

                        # Preencher tabela de market
                        if 'markets' in ven and len(ven['markets']) > 0:
                            for market in ven['markets']:
                                ven_market = market['name']
                                marketObject = Market(id=ven_market+'/'+ven['id'],
                                                        market=ven_market,
                                                        venueid=ven['id'],
                                                )
                            
                                #Verifica se o objeto já existe no banco
                                check = self.manipulateDB.selectMarket(marketObject.id)
                                id = str(marketObject.id)
                                #Se não existir, insere no banco
                                if not check:
                                    self.manipulateDB.insert(marketObject)
                                    print('Venue market inserido no banco. ID: ' + id)
                                else:
                                    print('Venue market já existe no banco. ID: ' + id)
                                        
                    # Preencher attraction
                    for attr in event["_embedded"]["attractions"]:
                        print(f'ID do ERRO ATTR: '+attr['id'])
                        attr_url = attr['url'] if 'url' in attr else None

                        try:
                            if ('classifications' in attr and 
                                len(attr['classifications']) > 0 and 
                                'genre' in attr['classifications'][0] and 
                                'id' in attr['classifications'][0]['genre']):
                                attr_genre = attr['classifications'][0]['genre']['id']
                            else:
                                attr_genre = None

                            if attr_genre == 'Undefined':
                                if ('type' in attr['classifications'][0] and 
                                    'id' in attr['classifications'][0]['type']):
                                    attr_genre = attr['classifications'][0]['type']['id']
                                else:
                                    attr_genre = None
                        except KeyError as e:
                            print(f"KeyError: {e}")
                            attr_genre = None


                        attrObject = Attraction(id=attr['id'],
                                            name=attr['name'],
                                            url=attr_url,
                                            classificationsid=attr_genre,
                                        )
                    
                        #Verifica se o objeto já existe no banco
                        check = self.manipulateDB.selectAttraction(attrObject.id)
                        id = str(attrObject.id)
                        #Se não existir, insere no banco
                        if not check:
                            self.manipulateDB.insert(attrObject)
                            print('Attraction inserido no banco. ID: ' + id)
                        else:
                            print('Attraction já existe no banco. ID: ' + id)

                        # Preencher tabela de market
                        if 'images' in attr and len(attr['images']) > 0:
                            for image in attr['images']:
                                ven_image = image['url']
                                imagesObject = AttractionImage(image=ven_image,
                                                        attractionid=attr['id'],
                                                )
                            
                                #Verifica se o objeto já existe no banco
                                check = self.manipulateDB.selectAttractionImage(imagesObject.image)
                                id = str(imagesObject.image)
                                #Se não existir, insere no banco
                                if not check:
                                    self.manipulateDB.insert(imagesObject)
                                    print('Attraction image inserido no banco. ID: ' + id)
                                else:
                                    print('Attraction image já existe no banco. ID: ' + id)
        
                    event_url = event['url'] if 'url' in event else None
                    event_startDate = event['sales']['public']['startDateTime'] if 'startDateTime' in event['sales']['public'] else None
                    event_endDate = event['sales']['public']['endDateTime'] if 'endDateTime' in event['sales']['public'] else None
                    event_timezone = event['dates']['timezone'] if 'timezone' in event['dates'] else None
                    event_promoter = event['promoter']['name'] if 'promoter' in event else None
                    event_min = event['priceRanges'][0].get('min') if 'priceRanges' in event and len(event['priceRanges']) > 0 and 'min' in event['priceRanges'][0] else None
                    event_max = event['priceRanges'][0].get('max') if 'priceRanges' in event and len(event['priceRanges']) > 0 and 'max' in event['priceRanges'][0] else None
                    event_dateTime = event['dates']['start']['dateTime'] if 'dates' in event and 'start' in event['dates'] and 'dateTime' in event['dates']['start'] else None
                    
                    print(f'ID do ERRO evento: '+event['id'])
                    
                    try:
                        if ('classifications' in event and 
                            len(event['classifications']) > 0 and 
                            'genre' in event['classifications'][0] and 
                            'id' in event['classifications'][0]['genre']):
                            event_genre = event['classifications'][0]['genre']['id']
                        else:
                            event_genre = None

                        if event_genre == 'Undefined':
                            if ('type' in event['classifications'][0] and 
                                'id' in event['classifications'][0]['type']):
                                event_genre = event['classifications'][0]['type']['id']
                            else:
                                event_genre = None
                    except KeyError as e:
                        print(f"KeyError: {e}")
                        event_genre = None

                    eventObject = Event(id=event['id'],
                                            name=event['name'],
                                            url=event_url,
                                            startdatesale=event_startDate,
                                            enddatesale=event_endDate,
                                            startdateevent=event_dateTime,
                                            timezone=event_timezone,
                                            minprice=event_min,
                                            maxprice=event_max,
                                            promoter=event_promoter,
                                            venueid=event['_embedded']['venues'][0]['id'],
                                            classificationsid=event_genre,
                                        )

                    
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectEvent(eventObject.id)
                    id = str(eventObject.id)
                    #Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(eventObject)
                        print('Event inserido no banco. ID: ' + id)
                    else:
                        print('Event já existe no banco. ID: ' + id)

                     # Preencher tabela de image event
                    if 'images' in event and len(event['images']) > 0:
                        for image in event['images']:
                            ven_image = image['url']
                            imagesObject = EventImage(image=ven_image,
                                                    eventid=event['id'],
                                            )
                           
                            #Verifica se o objeto já existe no banco
                            check = self.manipulateDB.selectEventImage(imagesObject.image)
                            id = str(imagesObject.image)
                            #Se não existir, insere no banco
                            if not check:
                                self.manipulateDB.insert(imagesObject)
                                print('Attraction image inserido no banco. ID: ' + id)
                            else:
                                print('Attraction image já existe no banco. ID: ' + id)

                    #Preencher tabela auxiliar de event_attraction
                    for event_attr in event["_embedded"]["attractions"]:

                        event_attrObject = EventAttraction(id=event['id']+'/'+event_attr['id'],
                                                eventid=event['id'],
                                                attractionid=event_attr['id']
                                            )
                        
                        #Verifica se o objeto já existe no banco
                        check = self.manipulateDB.selectEventAttraction(event_attrObject.id)
                        id = str(event_attrObject.id)
                        #Se não existir, insere no banco
                        if not check:
                            self.manipulateDB.insert(event_attrObject)
                            print('Event Attractin inserido no banco. ID: ' + id)
                        else:
                            print('Event Attractin já existe no banco. ID: ' + id)
            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)
        
    def getAttractions(self):
        try:
            print('Fazendo a carga dos Attractions no banco...')
            for page in range(0,10):
                url = f"https://app.ticketmaster.com/discovery/v2/attractions.json?apikey=HvPlPVQ2sP3kTGbG19RGHGl9sQFvUNZX&page={page}&size=200"
                response = requests.get(url)
                attractions_json = response.json()
                
                if len(attractions_json) == 0:
                    raise Exception('Json vazio')

                for attr in attractions_json["_embedded"]["attractions"]:

                    attr_url = attr['url'] if 'url' in attr else None

                    attrObject = Attraction(id=attr['id'],
                                            name=attr['name'],
                                            url=attr_url,
                                            classificationsid=attr['classifications'][0]['genre']['id'],
                                        )
                    
                    #Verifica se o objeto já existe no banco
                    check = self.manipulateDB.selectAttraction(attrObject.id)
                    id = str(attrObject.id)
                    #Se não existir, insere no banco
                    if not check:
                        self.manipulateDB.insert(attrObject)
                        print('Attraction inserido no banco. ID: ' + id)
                    else:
                        print('Attraction já existe no banco. ID: ' + id)

                    # Preencher tabela de market
                    if 'images' in attr and len(attr['images']) > 0:
                        for image in attr['images']:
                            ven_image = image['url']
                            imagesObject = AttractionImage(image=ven_image,
                                                    attractionid=attr['id'],
                                            )
                           
                            #Verifica se o objeto já existe no banco
                            check = self.manipulateDB.selectAttractionImage(imagesObject.image)
                            id = str(imagesObject.image)
                            #Se não existir, insere no banco
                            if not check:
                                self.manipulateDB.insert(imagesObject)
                                print('Attraction image inserido no banco. ID: ' + id)
                            else:
                                print('Attraction image já existe no banco. ID: ' + id)

            return 1

        except Exception as e:
            return '\nERRO: ' + repr(e)