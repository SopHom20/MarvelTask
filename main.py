import requests
from datetime import datetime
import hashlib

characters = []

def getParams():
    ts = datetime.timestamp(datetime.now())
    private_key = 'dd9f636bb9927e657228de86f6fc0047cac8dae3'
    public_key = '1c3a6525dc80c14c7fadb474d1bd11c5'
    hashkey = hashlib.md5()
    hashkey.update(f'{ts}{private_key}{public_key}'.encode())
    hashed = hashkey.hexdigest()

    parameters = {'apikey': public_key, 'ts': ts, 'hash': hashed}

    return parameters

def getCharacter(character):
    parameters = getParams()
    parameters['nameStartsWith'] = character
    return (requests.get('https://gateway.marvel.com/v1/public/characters?', params=parameters)).json()


def getDetails(request):
    characters.clear()
    if request['data']['count'] > 0:
        for char in request['data']['results']:
            character = {'name': char['name']}
            description = char['description']
            if len(description) > 0:
                character['description'] = char['description']
            else:
                character['description'] = "No description provided"
            character['comicnumber'] = str(char['comics']['available'])
            character['thumbnail'] = char['thumbnail']['path']
            characters.append(character)


def getResults():
    return characters

#character = input("Enter a Marvel character: ")
#print()
#getDetails(getCharacter(character))
