import unittest
from utils import is_capitalized, full_upper, full_lower, has_root

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
