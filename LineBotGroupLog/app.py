from __future__ import unicode_literals
from flask import Flask, request
import configparser
import requests
import os
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, ImageMessage, AudioMessage, FileMessage, TextSendMessage
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get("line-bot", "channel_access_token"))
handler = WebhookHandler(config.get("line-bot", "channel_secret"))
line_bot_api.set_webhook_endpoint(config.get("line-bot", "WEBHOOK_URL") + "/callback")
app = Flask(__name__)


@app.route("/")
def test():
    return 'OK', 200



@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return 'Invalid signature', 400

    return 'OK', 200


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    message_text = event.message.text
    current_time = datetime.now()
    with open("messages.txt", "a") as f:
        f.write(f"{str(current_time)}\t{message_text}\n")
    return 'OK', 200


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    message_id = event.message.id
    message_content = line_bot_api.get_message_content(message_id)
    save_path = os.path.join("images", f"{message_id}.jpg")
    with open(save_path, 'wb') as f:
        for chunk in message_content.iter_content():
            f.write(chunk)
    return 'OK', 200


@handler.add(MessageEvent, message=AudioMessage)
def handle_audio_message(event):
    message_id = event.message.id
    message_content = line_bot_api.get_message_content(message_id)
    save_path = os.path.join("audios", f"{message_id}.m4a")
    with open(save_path, 'wb') as f:
        for chunk in message_content.iter_content():
            f.write(chunk)
    return 'OK', 200


@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    message_id = event.message.id
    message_content = line_bot_api.get_message_content(message_id)
    file_name = event.message.file_name
    save_path = os.path.join("files", file_name)
    with open(save_path, 'wb') as f:
        for chunk in message_content.iter_content():
            f.write(chunk)
    return 'OK', 200


def reply_message(reply_token, message_text):
    line_bot_api.reply_message(
        reply_token,
        TextMessage(text=message_text)
    )


def push_message(user_id, message):
    text_message = TextSendMessage(text=message)
    line_bot_api.push_message(user_id, messages=text_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
