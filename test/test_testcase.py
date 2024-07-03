import unittest
from setUp import *

class TestClass(unittest.TestCase):
    @classmethod # only called once
    def setUpClass(cls) -> None:
        print(f'testing: {cls.__module__}')
        cls.var1 = 1
        cls.var2 = 2
        
    @classmethod
    def tearDownClass(cls) -> None:
        print(f'finished testing: {cls.__module__}')

    def test_add(self):
        self.assertEqual(self.var1 + self.var1, self.var2)
        self.assertFalse(self.var1 + self.var1 == 3)

    def test_sub(self):
        self.assertEqual(1-1, 0)
