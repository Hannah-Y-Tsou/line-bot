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

app = Flask(__name__)

line_bot_api = LineBotApi('SuIqtfuMWcrRa1ZtnXybwhx6qb5NWgXXOCjGLJgZgUFvCp4OcJNz5HimGes1peKkUq2CLasmzc3/As4woWTlbIsdG9F05ORKIp2oFBM0XuKp2BocRfkiHqhAPiJ0L238K1kmqQ/paNoFA/CYMSXvmQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8176d81992dfe486f0bc33852b35500b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '說啥'

    if msg == '想你'
        r = '那還不快來抱抱我'
    elif msg == 'bae'
        r = '怎啦'
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()