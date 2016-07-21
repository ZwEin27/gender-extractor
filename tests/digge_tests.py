import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# input_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'sparql-queries.json'))
# output_ = os.path.expanduser(os.path.join(TEST_DATA_DIR, 'sparql-queries-parsed.json'))

import json

class TestDIGGEMethods(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_extract(self):
        pass

    

if __name__ == '__main__':
    def run_main_test():
        suite = unittest.TestSuite()
        suite.addTest(TestSQParserMethods('test_extract'))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()



