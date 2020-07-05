import unittest
from unittest.mock import patch
import requests
import translate


class TestMainFunctions(unittest.TestCase):
    def setUp(self):
        self.translated_text = translate.translate_text()
        print(self.translated_text)

    def test_translate_text(self):
        self.assertEqual('Привет мир', self.translated_text['text'][0])
        self.assertEqual('200', str(self.translated_text['code']))
    
    def test_too_many_arg(self):
        self.assertRaises(TypeError, translate.translate_text(), ('ru', 'en'))

if __name__ == "__main__":
    unittest.main()