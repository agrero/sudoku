# Example
import unittest

class testSuite(unittest.TestLoader):
    
    def __init__(self):
        super.__init__(self)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    newSuite = unittest.TestSuite(TestList)
    runner = unittest.TextTestRunner()
    runner.run(suite())