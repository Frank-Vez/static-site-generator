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
     ...


if __name__ == "__main__":
    unittest.main()
