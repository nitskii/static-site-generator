import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_neq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALIC)
    self.assertNotEqual(node, node2)

  def test_url_is_none(self):
    node = TextNode("Text", TextType.NORMAL)
    self.assertEqual(node.url, None)

  def test_url_is_defined(self):
    expected_url = "https://google.com"
    node = TextNode("Text", TextType.LINK, expected_url)
    self.assertEqual(expected_url, node.url)

if __name__ == "__main__":
  unittest.main()
