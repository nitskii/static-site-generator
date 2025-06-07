from unittest import TestCase
from splittextnode import split_text_node
from textnode import TextNode, TextType

class TestSplitTextNode(TestCase):
  def test_delimeter_code(self):
    node = TextNode("This is text with a `code block` part", TextType.NORMAL)
    new_nodes = split_text_node([node], "`", TextType.CODE)
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("code block", TextType.CODE),
      TextNode(" part", TextType.NORMAL),
    ]

    for i in range(0, len(expected)):
      self.assertEqual(new_nodes[i], expected[i])

  def test_delimeter_bold(self):
    node = TextNode("This is text with a **bold** word", TextType.NORMAL)
    new_nodes = split_text_node([node], "**", TextType.BOLD)
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" word", TextType.NORMAL),
    ]

    self.assertListEqual(expected, new_nodes)

  def test_delimeter_bold_and_italic(self):
    node = TextNode("This is text with a **bold** word and _italic_ word", TextType.NORMAL)
    new_nodes = split_text_node([node], "**", TextType.BOLD)
    new_nodes = split_text_node(new_nodes, "_", TextType.ITALIC)
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" word and ", TextType.NORMAL),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word", TextType.NORMAL)
    ]

    self.assertListEqual(expected, new_nodes)
