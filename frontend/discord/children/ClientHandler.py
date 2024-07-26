from sudoku.helper.api_helper import get_command
import requests

from sudoku.pydantic.models import CommandIn
from fastapi.encoders import jsonable_encoder

from sudoku.classes.game.Board import Board

class ClientHandler:

    async def post_solvehandler(self, message, url):
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
            )))
        
        board = Board()
        board.board = post.json()['solved_board']
        response = board.pretty_rep()

        await message.channel.send(response)

    async def get_boardstate(self, message, url):
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
        
        await message.channel.send(post.json())