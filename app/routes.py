from app import app
from flask import render_template, request
from .forms import PokeSearchForm
import requests

@app.route('/', methods=['GET', 'POST'])
def searchPokemon():
    form = PokeSearchForm()
    poke_dict = {}
    if request.method == 'POST':
        if form.validate():
            poke_name = form.name.data
            print(poke_name)
            url = f'https://pokeapi.co/api/v2/pokemon/{poke_name.lower()}'
            responce = requests.get(url)
            if responce.ok:
                data = responce.json()
                poke_dict = {
                    'name': data['name'],
                    'ability': data['abilities'][0]['ability']['name'],
                    'hp': data['stats'][0]['base_stat'],
                    'attack': data['stats'][1]['base_stat'],
                    'defense': data['stats'][2]['base_stat'],
                    'img_url': data['sprites']['front_default']
                }
                print(poke_dict)
            else:
                print('Failed to access API')
    return render_template('searchPokemon.html', form=form, poke_dict=poke_dict)

