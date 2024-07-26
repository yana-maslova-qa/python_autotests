import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "e92893068665c0d430150080047babb5"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}


body_criaute = {
    "name": "generate",
    "photo_id": -1
}

body_update = {
    "pokemon_id": "41979",
    "name": "Cтас",
    "photo_id": "222"
}

body_add_pokeball = {
    "pokemon_id": "41979"
}

body_battle = {
    "attacking_pokemon": "34330",
    "defending_pokemon": "41969"
}

#Создание
'''response_criaute = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_criaute)
print(response_criaute.text)

message = response_criaute.json()['message']
print(message)'''

#Изменение
'''response_update = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_update)
print(response_update.text)

message = response_update.json()['message']
print(message)'''

#Ловля покемона
'''response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)'''

#Проведение битвы
response_battle = requests.post(url=f'{URL}/battle', headers=HEADER, json=body_battle)
print(response_battle.text)

message = response_battle.json()['message']
print(message) 





