import discord

from frontend.discord.children.ClientHandler import ClientHandler



class CustomClient(discord.Client):
    """
    Docstrings Here
    
    $s: Discord Bot Command Prompt

    I think eventually this will swallow a more condensed
    Client Handler class
    """
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, 
                         message, 
                         url='http://0.0.0.0:8000', 
                         handler=ClientHandler()) -> None:
        
        """
        On Message Response method

        listens to all discord messages accessible to the bot
        sends commands to listed api url & sends a message in the same
        discord channel as a response. Ignores messages without $s command
        prompt in the user message.
        
        message: discord message class containing message content as well as
            ownership details. 
        url: url for api call
        handler: message response handler class

        returns: None
        """
        
        if message.author == self.user:
            return

        if message.content.startswith('$s'):
            response = await handler.get_boardstate(message, url)
            await message.channel.send(response.json()['puzzle'])

