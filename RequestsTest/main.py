import requests

URL= 'https://api.pokemonbattle.ru/v2'
TOKEN= '17f6b81ea48328020d9e1961d851761a'
HEADER= {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_registration= {
    "trainer_token": TOKEN,
    "email": "ahmetdinovaradmila@gmail.com",
    "password": "Iloveqa6"
}
body_confirmation= {
    "trainer_token": TOKEN
}

body_update= {
    "pokemon_id": "182406",
    "name": "Мишка",
    'photo_id': 1
}

body_catch= {
    "pokemon_id": "182668"
}

response_create=requests.post(url = f'{URL}/pokemons', headers = HEADER, json= body_create)
print(response_create.text)


response=requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json= body_registration)
print(response.text)
 
response_confirmation=requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json= body_confirmation)
print(response_confirmation.text)

response_update=requests.put(url = f'{URL}/pokemons', headers = HEADER, json= body_update)
print(response_update.text)

response_catch=requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json= body_catch)
print(response_catch.text)