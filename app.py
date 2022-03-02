from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
import schedule
import time

load_dotenv()
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]


app = App(token=SLACK_BOT_TOKEN)


def task():
    app.client.chat_postMessage(channel='#simple-bot-test',text="heyy how r u??")

schedule.every().day.at("12:12").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)