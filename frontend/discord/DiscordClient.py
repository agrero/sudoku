import discord
# import requests

# from fastapi.encoders import jsonable_encoder

# from sudoku.pydantic.models import CommandIn
# # from sudoku.helper.api_helper import get_command

from frontend.discord.children.ClientHandler import ClientHandler

# could split into api client and pure discord client
class CustomClient(discord.Client):
    """
    Docstrings Here
    
    $h: Discord Bot Command Prompt

    I think eventually this will swallow a more condensed
    Client Handler class
    """
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    # this should come from an inherited message handler object

    async def on_message(self, message, 
                         url='http://0.0.0.0:8008', 
                         handler=ClientHandler()):
        
        if message.author == self.user:
            return

        if message.content.startswith('$s'):

            await handler.get_boardstate(message, url)

