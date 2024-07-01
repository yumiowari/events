import os

from core.controller import Controller

def main():
    if os.path.isfile('data/attraction.pkl'):
        os.remove('data/attraction.pkl')
    if os.path.isfile('data/classification.pkl'):
        os.remove('data/classification.pkl')
    if os.path.isfile('data/event.pkl'):
        os.remove('data/event.pkl')
    if os.path.isfile('data/venue.pkl'):
        os.remove('data/venue.pkl')

    controller = Controller()

main()