#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()
MDB = "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn"
API_ID = "23449041"
API_HASH = "22263bf0807d45f0fc9bac99471fec1b"
BOT_TOKEN = "7366478096:AAHbr0dqd7HgR6kyeJyjr3EvdenMYZY__6A"
SESSION = "BAFlzdEAozQolx1LHYhfrL0leS-yZz8ZxvHj2ehU-VJnjY6PA_7xp1OVWW38mZi-Tl73AeBdPB0YJadMw-IQIAcUkrU1iNdog07w8R-GRFem2e_8FLu1YHbCJPJfktM3vbxAhdWZT5vqCJvXmrn-usZCXOdDS1xuZ1VzMusK8Mod6OUY71jB1A9kJ6W_sg-lnZC2IlBicEr2KDAN9DZsEDc-hbWPl9B6LrX4Yl7ZmhiWIsvz2OsFP9Vg7VoZPz8IRd4YGD2LUcN8Y-Cn9DSG_qSNx2-PQDrQgj9bb3uxitXfO-94-7qwrFVOtaeGmVwZULMvoGHoP1f2MmEUwzlUjUlDMkQcpwAAAAGIjIX8AA"
FORCESUB = "ultrasaves"
AUTH = "6585878012"
MONGODB = "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn"
OWN = 6585878012 # edit this
GROUP = -1002002312606 # edit this
OWNER_ID = int(config("OWNER_ID", default=OWN))
LOG_GROUP = int(config("LOG_GROUP", default=GROUP))

SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
