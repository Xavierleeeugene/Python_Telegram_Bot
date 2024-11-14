
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config
import asyncio
import json

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from pymongo import MongoClient

# Initialize Telegram bot
bot = Bot(token=config.TELEGRAM_BOT_API_KEY, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Initialize MongoDB client and collection
client = MongoClient(config.MONGO_URI)
db = client['telegram_bot']
subscribers_collection = db['subscribers']

# Save New Chat ID 
def save_chat_id(chat_id):
    if not subscribers_collection.find_one({"chat_id": chat_id}):
        subscribers_collection.insert_one({"chat_id": chat_id})

# Chat ID Subscribers Retrieval
def get_all_chat_ids():
    return [sub['chat_id'] for sub in subscribers_collection.find()]


# COMMANDS

# Insert all possible commands that the user can give to the bot here
@dp.message(Command("subscribe"))
async def subscribe_command(message: types.Message):

    # Command Logic
    chat_id = message.chat.id
    save_chat_id(chat_id)

    # Bot reply in response to command
    await message.reply("Hello! Thank you for subscribing!")
    print(f"User Subscribe: {chat_id}")

@dp.message(Command("unsubscribe"))
async def unsubscribe_command(message: types.Message):

    # Command Logic
    chat_id = message.chat.id
    if subscribers_collection.find_one({"chat_id": chat_id}) is not None:
        subscribers_collection.delete_many({"chat_id": chat_id})
        await message.reply(f"You have unsubscribed to the bot.")
    else:
        await message.reply(f"You are not subscribed to the bot.")

    print(f"User Unsubscribed: {chat_id}")

@dp.message(Command("check_subscription"))
async def check_subscription_command(message: types.Message):

    # Command Logic
    chat_id = message.chat.id
    if subscribers_collection.find_one({"chat_id": chat_id}) is not None:
        await message.reply(f"You are currently subscribed to the bot with chat_id: {chat_id}")
    else:
        await message.reply("You are currently not subscribed to the bot. To subscribe, type /subscribe")

    print(f"User Status Check: {chat_id}")

@dp.message(Command("dummy"))
async def dummy_command(message: types.Message):
    # Logic
    dummy = "I am a Dummy Command"
    # Bot reply in response to command
    await message.reply(dummy)

# MAIN FUNCTION
async def run_telegram_bot():
    print("Running Telegram Bot")
    await dp.start_polling(bot)

async def main():
    # If you have 2 async functions to run:
    # await asyncio.gather(run_auto_update(), run_telegram_bot())
    
    # If you have just 1 async function to run:
    await run_telegram_bot()
    
if __name__ == '__main__':
    asyncio.run(main())