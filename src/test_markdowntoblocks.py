from unittest import TestCase
from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(TestCase):
  def test_single_block(self):
    markdown = "This is a block"
    blocks = markdown_to_blocks(markdown)
    expected = ["This is a block"]

    self.assertListEqual(expected, blocks)

  def test_multiple_blocks(self):
    markdown = "This is a block\n\nThis is another block"
    blocks = markdown_to_blocks(markdown)
    expected = ["This is a block", "This is another block"]

    self.assertListEqual(expected, blocks)

  def test_empty_block(self):
    markdown = "This is a block\n\n     \n\n\nThis is another block"
    blocks = markdown_to_blocks(markdown)
    expected = ["This is a block", "This is another block"]

    self.assertListEqual(expected, blocks)
    
    markdown = "This is a block\n\n\nThis is another block"
    blocks = markdown_to_blocks(markdown)
    expected = ["This is a block", "This is another block"]

    self.assertListEqual(expected, blocks)
    
    markdown = "This is a block\n\nThis is another block\n\n"
    blocks = markdown_to_blocks(markdown)
    expected = ["This is a block", "This is another block"]

    self.assertListEqual(expected, blocks)

  def test_multiline_blocks(self):
    markdown = "This is a block\n\nThis is another block\nmultiline"
    blocks = markdown_to_blocks(markdown)
    expected = ["This is a block", "This is another block\nmultiline"]

    self.assertListEqual(expected, blocks)
