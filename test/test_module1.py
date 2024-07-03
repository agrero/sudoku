# maybe setting this to be the module in main() will work

# python -m unittest <test_module>

import unittest

class TestClass(unittest.TestCase):


    def setUp(self):
        print('Setup')
        self.var1 = 1
        self.var2 = 2

    def tearDown(self) -> None:
        print('Teardown')

    def test_add(self):
        self.assertEqual(self.var1 + self.var1, self.var2)

if __name__ == '__main__':
    unittest.main()