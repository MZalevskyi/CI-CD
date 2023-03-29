import unittest
from main import words_sentences
class TestWordsSentences(unittest.TestCase):

    def test_word_count(self):
        result = words_sentences("Text.txt")
        self.assertEqual(result['words'], 10)

    def test_sentence_count(self):
        result = words_sentences("Text.txt")
        self.assertEqual(result['sentences'], 2)


if __name__ == '__main__':
    unittest.main()