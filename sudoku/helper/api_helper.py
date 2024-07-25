

def get_command(command_str: str) -> list:
    """
    command_str: command as a string with command prompt removed
    
    returns: list of commands to be executed in order 
    """
    return [i for i in command_str.split(' ') if i != '']