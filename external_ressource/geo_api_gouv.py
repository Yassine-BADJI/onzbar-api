import requests


def get_long_and_latitude(encoded_loc):
    response = requests.get(
        url=f'https://api-adresse.data.gouv.fr/search/?q={encoded_loc}&type=street&autocomplete=1',
        headers={'Content-Type': 'application/json'}
    )
    data = response.json()
    longitude = data['features'][0]['geometry']['coordinates'][0]
    latitude = data['features'][0]['geometry']['coordinates'][1]
    return {'longitude': longitude, 'latitude': latitude}


