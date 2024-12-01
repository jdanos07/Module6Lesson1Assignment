import requests

def fetch_planet_facts():
    # body types, moons, graviy
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName')
            body_type = planet.get('bodyType')
            moons = planet.get('moons')
            gravity = planet.get('gravity')
            print(f'Planet: {name} - Body Type: {body_type}, Moons: {moons}, Gravity: {gravity}.')

fetch_planet_facts()