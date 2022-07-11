import requests
from datetime import datetime
import hashlib
import os

characters = []

def getParams():
    ts = datetime.timestamp(datetime.now())
    private_key = os.getenv('PRIVATE_KEY')
    public_key = os.getenv('PUBLIC_KEY')
    print("here")
    print(os.environ)
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
    print(request)
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
