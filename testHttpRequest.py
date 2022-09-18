import requests
import json

r = requests.get('https://evilinsult.com/generate_insult.php?lang=es&type=json')

jsonRespuesta = json.loads(r.text)
print(jsonRespuesta)
print(jsonRespuesta["insult"])

