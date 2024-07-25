import discord
import requests

from fastapi.encoders import jsonable_encoder

from sudoku.api.pydantic.models import CommandIn
from sudoku.api_helper import get_command


class CustomClient(discord.Client):
    """
    Docstrings Here
    
    $h: Discord Bot Command Prompt
    """
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    # this should come from an inherited message handler object
    async def on_message(self, message, url='http://0.0.0.0:8000'):
        
        # this could be a wrapper 
        # Listener().command_listen()
        # if command line start:
            # return command

        if message.author == self.user:
            return
        
        # should make this a command with a listening decorator
        if message.content.startswith('$h'):
            post = requests.post(
                url=f'{url}/test',
                headers={'Content-Type':'application/json'},
                json=jsonable_encoder(
                    CommandIn(
                        commands=get_command(message.content[2:]),
                        user=message.author.name,
                        message_id=message.id,
                        guild_id=message.guild.id
                    )
                ),
            )

            await message.channel.send(post.json()) # send message
