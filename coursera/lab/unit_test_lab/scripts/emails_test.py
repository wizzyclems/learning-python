#!/usr/bin/env python3

import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):

    def test_basic(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)



unittest.main()

