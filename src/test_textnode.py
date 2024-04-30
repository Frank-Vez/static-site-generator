import unittest

from textnode import Textnode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = Textnode("This is a text node", "bold","https://www.boot.dev" )
        node2 = Textnode("This is a text node", "bold","https://www.boot.dev")
        self.assertEqual(node, node2)
    def test_eq1(self):
        node = Textnode("This isnt a text node", "bold","https://www.boot.dev" )
        node2 = Textnode("This is a text node", "bold","https://www.boot.dev")
        self.assertIsNot(node, node2)


if __name__ == "__main__":
    unittest.main()