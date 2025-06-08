from enum import Enum
from re import match
from functools import reduce

class BlockType(Enum):
  PARAGRAPH="paragraph"
  HEADING="heading"
  CODE="code"
  QUOTE="quote"
  UNORDERED_LIST="unordered_list"
  ORDERED_LIST="ordered_list"

def block_to_block_type(block):
  startsWithHashtag = match(r"#{1,6} \w+", block)
  if startsWithHashtag: return BlockType.HEADING

  enclosedInBackticks = block.startswith('```') and block.endswith('```')
  if enclosedInBackticks: return BlockType.CODE

  block_lines = block.split("\n")

  def lineIsQuote(previousLinesPassed, line):
    return line.startswith(">") and previousLinesPassed

  eachLineIsQuote = reduce(lineIsQuote, block_lines, True)
  if eachLineIsQuote: return BlockType.QUOTE

  def lineIsUnorderedListItem(previousLinesPassed, line):
    return line.startswith("- ") and previousLinesPassed

  eachLineIsUnorderedListItem = reduce(lineIsUnorderedListItem, block_lines, True)
  if eachLineIsUnorderedListItem: return BlockType.UNORDERED_LIST

  line_number = 1
  eachLineIsOrderedListItem = True
  for line in block_lines:
    if not line.startswith(f"{line_number}. "):
      eachLineIsOrderedListItem = False
      break
    line_number += 1
  if eachLineIsOrderedListItem: return BlockType.ORDERED_LIST

  return BlockType.PARAGRAPH
