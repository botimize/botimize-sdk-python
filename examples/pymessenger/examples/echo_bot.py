"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot
from botimize import Botimize
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAAFlkzjPKKYBAH7DGxbn8IZC7zFWaItU3feIK3hxpHjGAqh9ebQBIViqPAcI039DesUoZApdVjPIzuBHlaAAZCJBNvN2fQ8WN2vlZBZCLHK5mR8wsfEYkMYzszINMJDRNfZCNBVq6u3TQBHJQD9qCHqgZC2bFDTLI0nTBnjdKsJ6wZDZD"
VERIFY_TOKEN = "chatbot"
bot = Bot(ACCESS_TOKEN)

botimize = Botimize("Y5IWNXBNANN1Y8WBCY3MMXBQVWV4TNY7","facebook")

@app.route("/", methods=['GET', 'POST'])
def hello():

    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        botimize.logIncoming(output)
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, message)
                        data = {
                            "access_token":ACCESS_TOKEN,
                            "message":x['message'],
                            "recipient":x['sender']
                        }
                        botimize.logOutgoing(data);
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5002, debug=True)
