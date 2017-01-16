import requests

API_URL = "https://api.botimize.io"

class Botimize:
    def __init__(self, apiKey, platform):
        self.apiKey = apiKey
        self.platform = platform
        self.apiUrl = API_URL

    def logIncoming(self, data):
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
        result = response.json()
        return result

    def logOutgoing(self, data):
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
        result = response.json()
        return result