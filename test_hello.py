import unittest
from main import hello

class TestHello(unittest.TestCase):
    def test_hello_valid_name(self):
        self.assertEqual(hello("Мир"), "Привет, Мир!")

    def test_hello_empty_name(self):
        with self.assertRaises(ValueError):
            hello("")

    def test_hello_whitespace_name(self):
        with self.assertRaises(ValueError):
            hello("   ")

    def test_hello_special_characters(self):
        self.assertEqual(hello("😊"), "Привет, 😊!")

if __name__ == "__main__":
    unittest.main()