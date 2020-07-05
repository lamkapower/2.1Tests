import requests
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
URL_DETECT = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
AUTH_TOKEN = 'OAuth AgAAAAAMJHsPAADLWwiDAXCweUwDiCWuIShzcQo'


def translate_text(tolang='ru'):
    params = {
        'key': API_KEY,
        'text': 'Hello world'
    }
    response = requests.post(URL_DETECT, params=params)
    json_response = response.json()
    lang = json_response['lang']
    translate_params = {
        'key': API_KEY,
        'text': 'Hello world',
        'lang': f'{lang}-{tolang}'
    }
    response = requests.post(URL, params=translate_params)
    json_ = response.json()
    return json_


if __name__ == '__main__':
    print(translate_text())