import unittest

# @TODO(mark): Implement this!
class TestMain(unittest.TestCase):

    def test_can_finish(self):
        self.assertEqual(5, 5, 'FOO')

    def test_can_repeat(self):
        self.assertEqual(5, 5, 'FOO')

    def test_can_ask_many(self):
        self.assertEqual(5, 5, 'FOO')

if __name__ == '__main__':
    unittest.main()
