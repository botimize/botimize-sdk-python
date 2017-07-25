from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from botimize import Botimize

app = Flask(__name__)
channelAccessToken = 'th5/8waCLbr6r+Q+78hpzi2EI1EhSTuHIAN3w+LIOVg2QDYYYV1bQB7tfVnGSXb/8rDIe9zIz58GyoLJGMirKODWIu19Ly2H8m58iXwPgd5sarjQiZPQ/Ia4eIgvRhr4/77nbp+ozIFVPfwlUIukiwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channelAccessToken)
handler = WebhookHandler('942c406c1f319abccd36ecdf4b51495a')
botimize = Botimize('13CIVSYVFO85N1EI116G6J3O3E93IXZY',"line",'https://3e220120.ngrok.io')

@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    event = request.get_json()
    print(event)
    botimize.log_incoming(event)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    outgoing_log = {
        'replyToken': event.reply_token,
        'messages': [{
            'type': event.message.type,
            'text': event.message.text,
        }],
        'channelAccessToken': channelAccessToken
    }
    print(outgoing_log)
    botimize.log_outgoing(outgoing_log)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()