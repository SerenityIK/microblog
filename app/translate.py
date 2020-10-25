import requests
from flask_babel import _
from app import current_app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    region = 'global'
    # set endpoint url
    endpoint = 'https://api.cognitive.microsofttranslator.com/'
    path = 'translate?api-version=3.0'
    params = '&from={}&to={}'.format(source_language, dest_language)
    constructed_url = endpoint + path + params
    # set headers
    headers = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json'
        }
    # set body
    body = [{
        'text': text
    }]
    # make request to ms translator api
    response = requests.post(constructed_url, headers=headers, json=body)
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    translation = response.json()
    return translation[0]['translations'][0]['text']
