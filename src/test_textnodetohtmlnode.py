from unittest import TestCase
from textnodetohtmlnode import text_node_to_html_node
from textnode import TextType, TextNode

class TestTextNodeToHTMLNode(TestCase):
  def test_normal(self):
    text = "This is a normal text node"
    text_node = TextNode(text, TextType.NORMAL)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, text)

  def test_bold(self):
    text = "This is a bold text node"
    text_node = TextNode(text, TextType.BOLD)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, text)

  def test_link(self):
    text, url = "This is a link node", "https://google.com"
    text_node = TextNode(text, TextType.LINK, url)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, text)
    self.assertEqual(html_node.props["href"], url)

  def test_image(self):
    text, url = "This is an image node", "https://google.com"
    text_node = TextNode(text, TextType.IMAGE, url)
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, "img")
    self.assertEqual(html_node.value, "")
    self.assertEqual(html_node.props["src"], url)
    self.assertEqual(html_node.props["alt"], text)

  def test_invalid_text_type(self):
    text_node = TextNode("text", "binary")
    try:
      text_node_to_html_node(text_node)
    except ValueError as error:
      self.assertEqual(str(error), "Invalid text type")
