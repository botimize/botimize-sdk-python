import requests

class Botimize:
    def __init__(self, apiKey, platform, api_url = 'https://api.botimize.io'):

        self.apiKey = apiKey
        self.platform = platform
        if(platform != 'facebook' and platform != 'line' and 
            platform != 'telegram' and platform != 'generic'):
            print('unsupported platform:' + platform)

        self.apiUrl = api_url

    def log_incoming(self, data):
        uri = self.apiUrl + '/messages'
        auth = {
            'apikey': self.apiKey
        }
        options = {
            'tag': 'unknown',
            'platform': self.platform,
            'direction': 'incoming',
            'raw': data
        }
        response = requests.post(
            uri,
            params=auth,
            json=options
        )
        return response.json()

    def log_outgoing(self, data):
        uri = self.apiUrl + '/messages'
        auth = {
            'apikey': self.apiKey
        }
        options = {
          'tag': 'unknown',
          'platform': self.platform,
          'direction': 'outgoing',
          'raw': data
        }
       
        response = requests.post(
            uri,
            params=auth,
            json=options
        )
        return response.json()