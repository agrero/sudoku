from sudoku.helper.api_helper import get_command
import requests

from sudoku.schemas.api import CommandIn
from fastapi.encoders import jsonable_encoder

from sudoku.classes.game.Board import Board


# MANIUPLATIONS SHOULD HAPPEN NOT HERE
# ALSO TRY AND SLIM THIS DOWN AND MAKE IT PART OF THE CUSTOMCLIENT
class ClientHandler:
    def __init__(self) -> None:

        # GET api calls
        self.get_methods = ['get_keys', 'puzzle', 'bt_predict']
        self.post_methods = ['set_tile', 'make_keys', 'create_user']

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
        
        if commands[0] in self.get_methods:
            post = requests.get(
                url=f'{url}/{'/'.join(commands)}', #URL should unwrap all commands
                headers={'Content-Type':'application/json'},
                json=jsonable_encoder(
                    CommandIn(
                        commands=commands,
                        user=message.author.name,
                        user_id=message.author.id,
                        message_id=message.id,
                        guild_id=message.guild.id
                )))
            return post

        elif commands[0] in self.post_methods:
            post = requests.post(
                url=f'{url}/{'/'.join(commands)}', #URL should unwrap all commands
                headers={'Content-Type':'application/json'},
                json=jsonable_encoder(
                    CommandIn(
                        commands=commands,
                        user=message.author.name,
                        user_id=message.author.id,
                        message_id=message.id,
                        guild_id=message.guild.id
                )))
            
            return post
        

    async def send_board(self, message, url:str) -> None:
        """
        sends board state to discord utilizing get_boardstate
        method.

        message: a message in the form of an on_message discord 
            response
        url: api url

        returns: None
        """
        # post to get boardstate 
        post = self.get_boardstate(message=message, url=url)
        await message.channel.send(Board(
            board=post.json()['solved_board']
        ).pretty_rep())

