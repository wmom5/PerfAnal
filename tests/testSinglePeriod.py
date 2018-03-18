'''
Created on Mar 18, 2018

@author: Paul
'''
import unittest
from perfanal import singleperiod as sp


class Test(unittest.TestCase):

    def testSinglePeriod(self):
        assert(sp.singlePeriod(100, 130) == 30)

    def testDivZero(self):
        with self.assertRaises(ValueError):
            sp.singlePeriod(0, 0)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testSinglePeriod']
    unittest.main()
