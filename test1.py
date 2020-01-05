#!/bin/env python
import deploymgmt
import unittest 
from unittest.mock import patch


class testsuite1(unittest.TestCase):

    @patch('clientlib.info.getinfo')
    def testcase1(self, mock1):
        t1 = deploymgmt.classifier("deploy")
        assert t1 == "Deploying"
        # assert mock1.called

    @patch('clientlib.info.destroy')
    def testcase2(self, mock2):
        t1 = deploymgmt.classifier("delete")
        assert t1 == "Deleting"
        assert mock2.called

    @patch('deploymgmt.info')
    def testcase3(self, mock3):
        t1 = deploymgmt.classifier("reconfig")
        assert t1 == "reconfigure"
        assert mock3.called


if __name__ == "__main__":
    unittest.main()
