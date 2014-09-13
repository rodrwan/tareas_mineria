import unittest
from utils import is_capitalized, full_upper, full_lower, has_root, sin_cat

class isCapitalized(unittest.TestCase):
    def test_is_capitalized(self):
        word_for_test = "Was"
        result = is_capitalized(word_for_test)
        self.assertEqual(1, result)
    def test_is_not_capitalized(self):
        word_for_test = "WAs"
        result = is_capitalized(word_for_test)
        self.assertEqual(0, result)
    def test_is_capitalized_one_letter(self):
        word_for_test = "I"
        result = is_capitalized(word_for_test)
        self.assertEqual(1, result)

class fullUpper(unittest.TestCase):
    def test_is_upper(self):
        word_for_test = "WAS"
        result = full_upper(word_for_test)
        self.assertEqual(1, result)
    def test_is_not_upper(self):
        word_for_test = "WAs"
        result = full_upper(word_for_test)
        self.assertEqual(0, result)

class fullLower(unittest.TestCase):
    def test_is_lower(self):
        word_for_test = "was"
        result = full_lower(word_for_test)
        self.assertEqual(1, result)
    def test_is_not_lower(self):
        word_for_test = "WAs"
        result = full_upper(word_for_test)
        self.assertEqual(0, result)

class hasRoot(unittest.TestCase):
    def test_has_root(self):
        word_for_test = "was"
        result = has_root(word_for_test)
        self.assertEqual(1, result)
    def test_has_not_root(self):
        word_for_test = "I"
        result = has_root(word_for_test)
        self.assertEqual(0, result)

class sinCat(unittest.TestCase):
    def test_sin_cat_root(self):
        word_for_test = "was"
        text = "I think you have bought the cover story this is propaganda , absolutely opposite the truth , the man was trying to rebuild the western alliance in the threat of rising german aggression ! ."
        entities = ['/PERSON', '/LOCATION', '/ORGANIZATION']
        result = sin_cat(word_for_test, text, entities)
        self.assertEqual('VBD', result)

if __name__ == '__main__':
    unittest.main()

