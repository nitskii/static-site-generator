from unittest import TestCase
from blocktoblocktype import block_to_block_type, BlockType

class TestBlockToBlockType(TestCase):
  def test_heading(self):
    heading = "### This is a heading"

    actual = block_to_block_type(heading)
    
    self.assertEqual(BlockType.HEADING, actual)

    heading = "# This is a heading"

    actual = block_to_block_type(heading)
    
    self.assertEqual(BlockType.HEADING, actual)

    heading = "###### This is a heading"

    actual = block_to_block_type(heading)
    
    self.assertEqual(BlockType.HEADING, actual)

  def test_code(self):
    code = "```This is code```"

    actual = block_to_block_type(code)
    
    self.assertEqual(BlockType.CODE, actual)

    code = "```\nThis is code\n```"

    actual = block_to_block_type(code)
    
    self.assertEqual(BlockType.CODE, actual)

  def test_quote(self):
    quote = ">This\n>is\n>a\n>quote"

    actual = block_to_block_type(quote)
    
    self.assertEqual(BlockType.QUOTE, actual)

    quote = ">This is a quote"

    actual = block_to_block_type(quote)
    
    self.assertEqual(BlockType.QUOTE, actual)

  def test_unordered_list(self):
    unordered_list = "- This is \n- unordered\n- list"

    actual = block_to_block_type(unordered_list)
    
    self.assertEqual(BlockType.UNORDERED_LIST, actual)

  def test_ordered_list(self):
    ordered_list = "1. This is \n2. unordered\n3. list"

    actual = block_to_block_type(ordered_list)
    
    self.assertEqual(BlockType.ORDERED_LIST, actual)


  def test_paragraph(self):
    paragraph = "This is a paragraph"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "###This is not a heading"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "####### This is not a heading"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "```This is not code"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "This is not code```"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "``This is not code``"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = ">This is not a\nquote"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "- This is not \nunordered \n- list"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "-This is not unordered list"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "1.This is not ordered list"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "1. This is not\nordered list"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)

    paragraph = "1. This is not\n3. ordered list"

    actual = block_to_block_type(paragraph)
    
    self.assertEqual(BlockType.PARAGRAPH, actual)
