from sudoku.helper.api_helper import get_command
import requests

from sudoku.schemas.api import CommandIn
from fastapi.encoders import jsonable_encoder

from sudoku.classes.game.Board import Board


# MANIUPLATIONS SHOULD HAPPEN NOT HERE
# ALSO TRY AND SLIM THIS DOWN AND MAKE IT PART OF THE CUSTOMCLIENT
class ClientHandler:

    async def get_boardstate(self, message, url:str) -> requests.Response:
        """
        Unpack Commands and send 
        a request to the database API

        message: a message in the form of an on_message discord 
            response
        url: string url to send 

        returns: requests.Response
        """

        commands = get_command(message.content[2:])
        post = requests.post(
            url=f'{url}/{'/'.join(commands)}', #URL should unwrap all commands
            headers={'Content-Type':'application/json'},
            json=jsonable_encoder(
                CommandIn(
                    commands=commands,
                    user=message.author.name,
                    message_id=message.id,
                    guild_id=message.guild.id
            )))
        
        return post

    async def send_board(self, message, url:str):
        
        # post to get boardstate 
        post = self.get_boardstate(message=message, url=url)
        await message.channel.send(Board(
            board=post.json()['solved_board']
        ).pretty_rep())

