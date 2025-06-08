from unittest import TestCase
from splitnodes import (
  split_nodes_by_delimiter,
  split_nodes_by_image,
  split_nodes_by_link
)
from textnode import TextNode, TextType

class TestSplitNodes(TestCase):
  def test_split_by_delimeter_code(self):
    node = TextNode("This is text with a `code block` part", TextType.NORMAL)
    new_nodes = split_nodes_by_delimiter([node], "`", TextType.CODE)
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("code block", TextType.CODE),
      TextNode(" part", TextType.NORMAL),
    ]

    for i in range(0, len(expected)):
      self.assertEqual(new_nodes[i], expected[i])

  def test_split_by_delimeter_bold(self):
    node = TextNode("This is text with a **bold** word", TextType.NORMAL)
    new_nodes = split_nodes_by_delimiter([node], "**", TextType.BOLD)
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" word", TextType.NORMAL),
    ]

    self.assertListEqual(expected, new_nodes)

  def test_split_by_delimeter_bold_and_italic(self):
    node = TextNode("This is text with a **bold** word and _italic_ word", TextType.NORMAL)
    new_nodes = split_nodes_by_delimiter([node], "**", TextType.BOLD)
    new_nodes = split_nodes_by_delimiter(new_nodes, "_", TextType.ITALIC)
    expected = [
      TextNode("This is text with a ", TextType.NORMAL),
      TextNode("bold", TextType.BOLD),
      TextNode(" word and ", TextType.NORMAL),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word", TextType.NORMAL)
    ]

    self.assertListEqual(expected, new_nodes)

  def test_split_by_image(self):
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_by_image([node])
    expected = [
      TextNode("This is text with an ", TextType.NORMAL),
      TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
      TextNode(" and another ", TextType.NORMAL),
      TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
    ]

    self.assertListEqual(expected, new_nodes)

    text = "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) with text at the end"
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_by_image([node])
    expected = [
      TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
      TextNode(" and another ", TextType.NORMAL),
      TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
      TextNode(" with text at the end", TextType.NORMAL)
    ]

    self.assertListEqual(expected, new_nodes)

    text = "![image](https://i.imgur.com/zjjcJKZ.png)"
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_by_image([node])
    expected = [TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")]

    self.assertListEqual(expected, new_nodes)

  def test_split_by_link(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_by_link([node])
    expected = [
      TextNode("This is text with a link ", TextType.NORMAL),
      TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
      TextNode(" and ", TextType.NORMAL),
      TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
    ]

    self.assertListEqual(expected, new_nodes)

    text = "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) at the end"
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_by_link([node])
    expected = [
      TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
      TextNode(" and ", TextType.NORMAL),
      TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
      TextNode(" at the end", TextType.NORMAL)
    ]

    self.assertListEqual(expected, new_nodes)

    text = "[to boot dev](https://www.boot.dev)"
    node = TextNode(text, TextType.NORMAL)
    new_nodes = split_nodes_by_link([node])
    expected = [TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")]

    self.assertListEqual(expected, new_nodes)
