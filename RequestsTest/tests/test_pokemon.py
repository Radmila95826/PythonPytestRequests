import requests
import pytest

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '17f6b81ea48328020d9e1961d851761a'
HEADER= {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '24914'


def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID}) 
    assert response.status_code == 200

def test_trainers():
    response_get = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID}) 
    assert response_get.json()["data"][0]["trainer_name"] == 'Mila'

