import unittest

from htmlnode import HTMLnode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_output(self):
        node = HTMLnode(tag="a", value="Hello world", props={"href": "https://www.google.com"})
        expected_output = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_default_parameters(self):
        # Create an HTMLNode instance without providing any arguments
        node = HTMLnode()
        
        # Assert that each attribute defaults to None
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_parameters_with_only_tag(self):
        node = HTMLnode(tag="p")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr_method(self):
        node = HTMLnode(tag="a", value="Hello world", props={"href": "https://www.google.com"})
        self.assertEqual(node.__repr__(), "HTMLnode(a, Hello world, children: None, {'href': 'https://www.google.com'})")

if __name__ == '__main__':
    unittest.main()
