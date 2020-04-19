import unittest
import threading_examples

class TestThread(unittest.TestCase):

    def test_add(self):
        result = threading_examples.add(10,5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = threading_examples.subtract(10,5)
        self.assertEqual(result, 5)