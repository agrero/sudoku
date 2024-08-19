from sqlalchemy.orm import Session

import string
from random import randint

# generate keys


def generate_keys(number:int, key_length=64) -> list[str]:
    """
    generates a set of keys utilizing a randomly indexed
    ascii_letter from the string module

    52 = len ascii_letter
    
    number: number of keys to generate

    returns: list of strings
    """

    return [
        ''.join([string.ascii_letters[randint(0, 51)] 
                 for i in range(key_length)])
        for j in range(number)
    ]
