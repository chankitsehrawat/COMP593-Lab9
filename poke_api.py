# Description: This file contains the function get_pokemon_info() which makes a request to the PokeAPI to get information about a Pokémon.
import requests

# Function to get information about a Pokémon
# This function makes a request to the PokeAPI to get information about a Pokémon.
def get_pokemon_info(pokemon_name):
    """Gets information about a Pokémon from the PokeAPI"""
    pokemon_name = str(pokemon_name).strip().lower()
    
    if not pokemon_name:
        return None
    
    try:
        # Make API request
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract required information
            pokemon_info = {
                'name': data['name'].capitalize(),
                'height': data['height'],
                'weight': data['weight'],
                'types': data['types'],
                'stats': data['stats']
            }
            return pokemon_info
        else:
            return None
            
    except (requests.exceptions.RequestException, KeyError):
        return None