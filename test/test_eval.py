import unittest


class TestClass(unittest.TestCase):
    @classmethod # only called once
    def setUpClass(cls) -> None:
        print(f'SETTING UP: {cls.__module__}')

        
    @classmethod
    def tearDownClass(cls) -> None:
        print(f'\nFINISHED: {cls.__module__}\n')


