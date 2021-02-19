import requests


def create_qr_code(bar_id):
    requests.get(
        url=f'https://api.qrserver.com/v1/create-qr-code/?data=onzbar_{bar_id}',
        headers={'Content-Type': 'application/json'}
    )
