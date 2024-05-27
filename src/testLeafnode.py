import unittest

from leafnode import Leafnode

class testLeafNode(unittest.TestCase):

  def test__init(self):
    node = Leafnode(tag = "a",value = "This is a leafnode",children = "fuck ff", props={"href": "https://www.google.com"})
    self.assertEqual(node.tag, "a")
    self.assertEqual(node.value, "This is a leafnode")
    self.assertIsNone(node.children)
    self.assertEqual(node.props, {"href": "https://www.google.com"})

  def test_stringrepr(self):
     node1 = Leafnode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
     node2 = Leafnode(tag="p",value="This is a paragraph of text.")

     self.assertEqual(node2.to_html(), "<p>This is a paragraph of text.</p>")
     self.assertEqual(node1.to_html(), '<a href="https://www.google.com">Click me!</a>')



if __name__ == "__main__":
    unittest.main()
