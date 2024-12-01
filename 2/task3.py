import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    planet_data = []

    for planet in planets:
        name = planet.get('englishName')
        aphelion = planet.get('aphelion')
        planet_data.append((name, aphelion))

    return planet_data

def largest_aphelion():
    planet_data = fetch_planet_data()

    largest = max(planet_data, key=lambda x: x[1])
    name, aphelion = largest
    print(f'{name} has the largest aphelion at {aphelion} km.')

largest_aphelion()