# bot.py
import os
import discord

from dotenv import load_dotenv

from frontend.discord.DiscordClient import CustomClient

# ah what another good looking candidate for some data validation 
# using pydantic models
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_ROOT')
API_URL = os.getenv('URL_ROOT')

intents = discord.Intents.default()
intents.message_content = True

client = CustomClient(intents=intents)

if __name__ == '__main__':
    client.run(TOKEN)

