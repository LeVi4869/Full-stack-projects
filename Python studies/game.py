import requests
pokemonName = input("Write the pokemon name")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemonName.lower()}"
req = requests.get(url)
pokemon = req.json()
print(f"Name: {pokemon['name']}")
print(f"Pokedex number: {pokemon['id']}")
print(f"Height: {pokemon['height']}0 cm")
print(f"Weight: {pokemon['weight']} kg")
print("Abilities: ")
index = 0
for ability in pokemon['abilities']:
    print(f"\t{index + 1}.\t", ability['ability']['name'])
    index += 1