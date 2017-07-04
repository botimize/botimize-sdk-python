# [botimize](http://botimize.io) - Analytics built to optimize your bots


## Table of contents

- [Setup](#setup)
- [Usage](#usage)
- [Initialization](#initialization)
- [Log incoming messages](#log-incoming-messages)
- [Log outgoing messages](#log-outgoing-messages)
- [References & Full Examples](#references--full-examples)

## Setup

* Create a free account at [Botimize](http://botimize.io) to get an API key. Or you can talk to our botimize helper [Facebook Messenger Helper](http://m.me/botimize.helper) or [Telegram Helper](http://t.me/botimize.helper) to create a public project.
* Install botimize SDK with `pip`:

  ```shell
  pip install botimize
  ```

## Usage

### Initialization

Use Botimize API key to create a new botimize object, and `<PLATFORM>` should be `facebook`, `telegram`, `line` or `generic`.

  ```python
  from botimize import Botimize
  ```
  ```python
  botimize = botimize.Botimize(<YOUR-API-KEY>, <PLATFORM>)
  ```
  ```python
  botimize = botimize.Botimize('NS1W0O5YCIDH9HJOGNQQWP5NU7YJ0S0S', 'facebook')
  ```

### Log incoming messages:

To log incoming message is very easy, just put the body received from platform webhook into `log_incoming()`.

#### Facebook / Telegram / LINE
  ```python
  botimize.log_incoming(request.body)
  ```

#### Generic
  ```python
  incoming_log = {
    'sender': {
      'id': 'UNIQUE_USER_ID',
      'name': 'USER_SCREEN_NAME'
    },
    'content': {
      'type': 'CONTENT_TYPE', #'text', 'image', 'audio', 'video', 'file', 'location'
      'text': 'CONTENT_TEXT'
    }
  }
  botimize.log_incoming(incoming_log)
  ```

### Log outgoing messages

This is a little different from `log_incoming()` because outgoing messages have token for sending message to client. **"Fortunately"**, there are three platforms and have three differents ways to authorize by using token. **"Unfortunately"**, one easy way is all Botimize needs.

#### Facebook 
  ```python
  outgoing_log = {
    'recipient': { 'id': '1487766407960998' },
    'message': 'hello facebook messenger',
    'accessToken': 'EAAXUgsVmiP8BAMcRWxLa1N5RycMzZBfjwiekoqCik6pZASPsnmkJtG29gp5QXdyMaKfFg0iZCIDlqhfhTZCLqRKuM4hUCfdZBcxl8GzKgZA0AwI8syxG49M9OaZCsjyZC8FPg30yIRDFG5hp9jNNtvqtWW0KKzB9a59rTkZBsgz2oe4QZDZD'
  }
  botimize.log_outgoing(outgoing_log)
  ```

#### Telegram
  ```python
  outgoing_log = {
    'chat_id': '161696362',
    'text': 'hello telegram',
    'token': '308726257:AAHnmJpvkAepqirk82ZOrgtF6Hz2ijbRavA',
  }
  botimize.log_outgoing(outgoing_log)
  ```

#### LINE
  ```python
  outgoing_log = {
    'replyToken': '9bd439c6961346d7b2ec4184469b9946',
    'messages': [{
      'type': 'text',
      'text': 'hello, this is a message from LINE chatbot',
    }],
    'channelAccessToken': 'GxvuC0QfatJ0/Bv5d3DoVbUcfVd6MXLj9QY8aFHSqCOdkfjD1I5dtbKZBNMbmLmwKox1Ktd0Kcwfsxm9S5OmIwQoChcV1gPlK/1CI8cUe3eqaG/UrqL65y1Birb6rnssT0Acaz+7Lr7V2WVnwrQdB04t89/1O/w1cDnyilFU=',
  }
  botimize.log_outgoing(outgoing_log)
  ```

#### Generic
  ```python
  outgoing_log = {
    'receiver': {
      'id': 'UNIQUE_USER_ID',
      'name': 'USER_SCREEN_NAME'
    },
    'content': {
      'type': 'CONTENT_TYPE', #'text', 'image', 'audio', 'video', 'file', 'location'
      'text': 'CONTENT_TEXT'
    }
  }
  botimize.log_outgoing(outgoing_log)
  ```

## References & Full Examples

### References
* [facebook-incoming-message](https://developers.facebook.com/docs/messenger-platform/webhook-reference#format)
* [facebook-outgoing-message](https://developers.facebook.com/docs/messenger-platform/send-api-reference#request)
* [telegram-incoming-message](https://core.telegram.org/bots/api#getting-updates)
* [telegram-outgoing-message](https://core.telegram.org/bots/api#sendmessage)
* [line-incoming-message](https://devdocs.line.me/en/#webhook-event-object)
* [line-outgoing-message](https://devdocs.line.me/en/?shell#reply-message)

### Full Examples
* [line-python-bot](https://github.com/botimize/line-python-bot)
* [telegram-node-bot](https://github.com/botimize/telegram-node-bot)
* [telegram-python-bot](https://github.com/botimize/telegram-python-bot)
* [messenger-node-bot](https://github.com/botimize/messenger-node-bot)
* [messenger-python-bot](https://github.com/botimize/messenger-python-bot)
