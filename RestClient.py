import requests

URL = 'http://localhost:5276/api/KajakTurs/'

def GetAll():
    response = requests.get(URL)
    data = response.json()
    return data, response

def Add(kajakTur):
    response = requests.post(URL, json = kajakTur)
    data = response.json()
    return data, response

