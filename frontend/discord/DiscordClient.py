import discord
import requests

from fastapi.encoders import jsonable_encoder

from sudoku.pydantic.models import CommandIn
from sudoku.helper.api_helper import get_command

from sudoku.classes.game.Board import Board

from frontend.discord.children.ClientHandler import ClientHandler

# could split into api client and pure discord client
class CustomClient(discord.Client):
    """
    Docstrings Here
    
    $h: Discord Bot Command Prompt
    """
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    # this should come from an inherited message handler object
    async def on_message(self, message, 
                         url='http://0.0.0.0:8000', 
                         handler=ClientHandler()):

        # DELETE ME 
        board = Board()

        if message.author == self.user:
            return
        
        if message.content.startswith('$h'):
            await handler.post_solvehandler(message, url)


        # this will need to utilize the api but do what it says below
        if message.content.startswith('$s'):
            await handler.get_boardstate(message, url)
            

            if message.content[0] == 'set':
                # send to api
                board.set_tile(
                    message.content[3], # number
                    message.content[2], # row
                    message.content[1]  # column
                )
                # handle api response (should save in db with each move)
                await message.channel.send(board.board)
            
            if message.content[0] == 'load':
                # send to api
                # # lookup user name in db
                # # return last saved game
                # handle response
                pass
