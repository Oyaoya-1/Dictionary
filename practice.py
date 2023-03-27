import requests

api_key = '6c206b54-39e3-42b6-a379-5e3ae77a3a81'
word = 'carrot'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)
definitions = res.json()
for definition in definitions:
    print (definition)