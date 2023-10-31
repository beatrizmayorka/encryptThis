import unittest
from encrypt import encryptThis

class TestEncrypt(unittest.TestCase):

    def test_encryptThis(self):
        self.assertEqual(encryptThis("Hello"), '72olle')

    def test_encryptThis_short_word(self):
        self.assertEqual(encryptThis("good"), '103doo')

    def test_encryptThis_multiple_words(self):
        self.assertEqual(encryptThis("hello world"), '104olle 119drlo')

    def test_encryptThis_single_letter_word(self):
        self.assertEqual(encryptThis("A"), '65')

    def test_encryptThis_empty_message(self):
        self.assertEqual(encryptThis(""), '')

if __name__ == '__main__':
    unittest.main()