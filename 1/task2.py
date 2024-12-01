import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')

data = response.json()

name = data.get('name')
abilities = [ability['ability']['name']  for ability in data.get('abilities')]

print(f'{name.capitalize()}:')
for ability in abilities:
    print(f'    {ability.capitalize()}')