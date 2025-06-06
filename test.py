import unittest
from main import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):
    def test_single_match(self):
        self.assertEqual(boyer_moore_search("hello world", "world"), [6])

    def test_multiple_matches(self):
        self.assertEqual(boyer_moore_search("abababab", "ab"), [0, 2, 4, 6])

    def test_no_match(self):
        self.assertEqual(boyer_moore_search("abcdefg", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(boyer_moore_search("abcdef", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(boyer_moore_search("", "abc"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(boyer_moore_search("short", "longerneedle"), [])

    def test_overlap(self):
        self.assertEqual(boyer_moore_search("aaaaa", "aa"), [0, 1, 2, 3])

if __name__ == "__main__":
    unittest.main()