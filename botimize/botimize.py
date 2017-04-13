import requests

API_URL = 'https://api.botimize.io'

class Botimize:
    def __init__(self, apiKey, platform):

        self.apiKey = apiKey
        self.platform = platform
        self.apiUrl = API_URL

    def log_incoming(self, data):
        uri = self.apiUrl + '/messages'
        auth = {
            'apikey': self.apiKey
        }
        result = []

        if(self.platform == 'facebook'):
            for event in data['entry']:
                messaging = event['messaging']
                for x in messaging:
                    if x.get('message'):
                        if not x['message'].get('is_echo'):
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
                            result.append(response.json())
                    else:
                        pass

        elif(self.platform == 'line'):
            for event in data['events']:
                if event['type'] != 'message':
                    continue

                message = event['message']
                if message['type'] != 'text':
                    continue

                messageData = {
                    'sender': {
                      'id': event['source']['userId'],
                      'name': 'unknown'
                    },
                    'content': {
                      'type': message['type'],
                      'text': message['text']
                    },
                    'timestamp':event['timestamp']
                }
                options = {
                    'tag': 'unknown',
                    'platform': 'generic',
                    'direction': 'incoming',
                    'raw': messageData
                }
                response = requests.post(
                    uri,
                    params=auth,
                    json=options
                )
                result.append(response.json())
        else:
            print('Specified platform is not supported: ' + self.platform)
            return

        return result

    def log_outgoing(self, data):
        uri = self.apiUrl + '/messages'
        auth = {
            'apikey': self.apiKey
        }
        if self.platform == 'facebook':
            options = {
              'tag': 'unknown',
              'platform': self.platform,
              'direction': 'outgoing',
              'raw': data
            }
        elif self.platform == 'line':
            options = {
              'tag': 'unknown',
              'platform': 'generic',
              'direction': 'outgoing',
              'raw': data
            }
        else:
            print('Specified platform is not supported: ' + self.platform)
            return
            
        response = requests.post(
            uri,
            params=auth,
            json=options
        )
        result = response.json()
        return result