import unittest

# python -m unittest <test_module>
# in the future will need to import config reader to get this path

if __name__ == '__main__':
    # initiate testloader
    testLoad = unittest.TestLoader()

    # recursively parse test directory for test_ methods
    newSuite = testLoad.discover(
        start_dir="test" # replace with config reader
    )

    # take loaded test directory and run tests
    runner = unittest.TextTestRunner().run(newSuite)
