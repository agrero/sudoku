# bot.py
import os
import discord

from dotenv import load_dotenv

from frontend.discord.DiscordClient import *

# ah what another good looking candidate for some data validation 
# using pydantic models
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_ROOT')
API_URL = os.getenv('URL_ROOT')

intents = discord.Intents.default()
intents.message_content = True


# await message.channel.send('hello') # send message

client = CustomClient(intents=intents)

if __name__ == '__main__':
    client.run(TOKEN)

# #{
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     },
#     "importance": 5
# }