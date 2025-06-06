from unittest import TestCase, main

from leafnode import LeafNode

class TestLeafNode(TestCase):
  def test_to_html(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    node = LeafNode("a", "link", { "href": "https://google.com" })
    self.assertEqual(node.to_html(), "<a href=\"https://google.com\">link</a>")
