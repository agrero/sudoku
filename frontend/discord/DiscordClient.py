import discord
import requests

from fastapi.encoders import jsonable_encoder

from sudoku.pydantic.models import CommandIn
from sudoku.helper.api_helper import get_command

from sudoku.classes.game.Board import Board

# could split into api client and pure discord client
class CustomClient(discord.Client):
    """
    Docstrings Here
    
    $h: Discord Bot Command Prompt
    """
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    # this should come from an inherited message handler object
    async def on_message(self, message, url='http://0.0.0.0:8000'):

        if message.author == self.user:
            return
        
        # should make this a command with a listening decorator
        if message.content.startswith('$h'):
            # parse commands
            commands = get_command(message.content[2:])
            post = requests.post(
                url=f'{url}/{commands[0]}',
                headers={'Content-Type':'application/json'},
                json=jsonable_encoder(
                    CommandIn(
                        commands=commands,
                        user=message.author.name,
                        message_id=message.id,
                        guild_id=message.guild.id
                    )
                ),
            ) # this could by some generic pydantic object that works as
            # a universal printer of sorts

            board = Board()
            board.board = post.json()['solved_board']
            response = board.pretty_rep()
            
            await message.channel.send(response) # send message
