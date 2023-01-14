# -*- coding: utf-8 -*-
"""Module providingFunction printing python version."""
import unittest

from .context import sample


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        """Function printing python version."""
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()
