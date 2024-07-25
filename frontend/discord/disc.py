# bot.py
import os

import discord
from dotenv import load_dotenv

from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
from typing import List, Optional

import requests


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True


class CommandIn(BaseModel):
    commands: list[str] 
    user: str
    message_id: int
    guild_id: int

class CustomClient(discord.Client):
    """
    Docstrings Here
    
    $h: Discord Bot Command Prompt
    """
    async def on_ready(self):
        for guild in self.guilds:
            if guild.name == GUILD:
                break
        print(f'{self.user} has connected to Discord!')
        print(f'{guild.name} (id: {guild.id})')

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')

    # this should come from an inherited message handler object
    async def on_message(self, message, url='http://0.0.0.0:8000'):
        # this could be a wrapper 
        if message.author == client.user:
            return
        
        if message.content.startswith('$h'):
            commands = [i for i in message.content[2:].split(' ') if i != '']
            commandin = CommandIn(
                    commands = commands,
                    user = message.author.name,
                    message_id = message.id,
                    guild_id = message.guild.id,
                )

            post = requests.post(
                url=f'{url}/test',
                json=jsonable_encoder(commandin),
                headers={'Content-Type':'application/json'}
            )

            await message.channel.send(post.json()) # send message

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