import requests, bs4, pandas, time
import Immobiliare, Tuttocasa


def start():
    global city, title, price, par

    title, price, par = [], [], []
    seek = input('Enter the name of the website to scrape: ').lower()

    while seek not in ['immobiliare', 'tuttocasa']:
        print('\n\nYour choice is unavailable.')
        seek = input('\nPlease enter the name of another website: ')

    city = input('Enter the city: ')

    if seek == 'immobiliare':
        Immobiliare(city)

    elif seek == 'tuttocasa':
        Tuttocasa(city)

title, price, par = [], [], []
city = ''

start()
