import discord

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
                         url='http://0.0.0.0:8000', 
                         handler=ClientHandler()):
        
        if message.author == self.user:
            return

        if message.content.startswith('$s'):
            
            response = await handler.get_boardstate(message, url)
            await message.channel.send(response.json()['puzzle'])

