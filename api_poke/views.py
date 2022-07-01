from django.http import HttpResponse
from django.shortcuts import render
import requests
from .forms import PokeForm

def sort_by_key(list):
    return list['ability']['name']
def sort_by_key_pokemons(list):
    return list['name']

def form_django(request):
    form = PokeForm()
    errored=False
    parsed_req = request.GET['name'].strip().lower()  if request.GET else 'ditto'
    URL_POKEMONS = "https://pokeapi.co/api/v2/pokemon/"
    URL = "https://pokeapi.co/api/v2/pokemon/"+parsed_req
    
    response = requests.get(url = URL)
    response_pokemons = requests.get(url = URL_POKEMONS)
    if response.status_code == 404:
        errored=True
        URL = "https://pokeapi.co/api/v2/pokemon/ditto"
        response = requests.get(url = URL)

    data = response.json()['abilities']
    data_pokemons = response_pokemons.json()['results']

    sort_data = sorted(data, key=sort_by_key)
    sort_pokemons = sorted(data_pokemons, key=sort_by_key_pokemons)

    context={
        'form': form,
        'name': " não encontrado" if errored else parsed_req,
        'sort_data': sort_data,
        'pokemons': sort_pokemons
    }
    return render(request, 'poke.html',context=context)
