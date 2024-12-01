import requests

selected_pokemon = ['pikachu', 'bulbasaur', 'squirtle']
weight_list = []

def fetch_pokemon_weight():
    
    for pokemon in selected_pokemon:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}')
    
        if response.status_code == 200:
            data = response.json()

            weight = data.get('weight')
            weight_list.append(weight)
        else:
            print('A selected Pokemon either does not exist, or is misspelled.')
    
    print(weight_list)

    
def avg_weight_calc():
    import statistics as stat
    average_weight = stat.mean(weight_list)
    print(f'The average weight of {selected_pokemon} is {average_weight} decagrams.')

fetch_pokemon_weight()
avg_weight_calc()