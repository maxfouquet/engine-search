import os
import json

from project import app
from flask import jsonify
from googleapiclient.discovery import build

my_api_key = "AIzaSyBPOGk4Z5D1WxwcFWnNlCioi0Bb_HVxtos"
my_cse_id = "d283338c4566b52ec"

def filter():
    data = []

    filename = os.path.join(app.static_folder, 'data', 'types.json')
    with open(filename) as json_file:
        load = json.load(json_file)

    type = [x for x in load["types"] if x["type"] == "health"]
    for site in type[0]["sites"]:
        data.append("site: " + site)

    return ' OR '.join(data)

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    print(search_term + " " + filter())
    response = service.cse().list(q=search_term + " " + filter(), cx=cse_id, **kwargs).execute()
    return response['items']

@app.route('/<terms>')
def api(terms):
    results = google_search(terms, my_api_key, my_cse_id, num=100)

    return jsonify(results)
