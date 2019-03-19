'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''
import requests

for num in range(1,152):
    url = f"https://pokeapi.co/api/v2/pokemon/{num}/"
    pokemon = requests.get(url)

    name = pokemon.json()["name"]
    height = pokemon.json()['height']

    with open('catch_em_all.txt','a') as fout:
        fout.write(f"{name.capitalize()}'s height: {height} (ID:{num}) \n")

