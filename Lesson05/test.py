import unittest
import os
import sys


if __name__ == '__main__':
    TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # add root server folder to the search path
    # sys.path.insert(0, TOP_DIR)
    # find all tests
    TEST_SUITE = unittest.defaultTestLoader.discover('GEODistance', pattern='test_*.py')
    # execute all tests
    unittest.TextTestRunner(verbosity=2).run(TEST_SUITE)
