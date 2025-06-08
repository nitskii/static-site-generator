def markdown_to_blocks(markdown):
  blocks = markdown.split("\n\n")
  blocks = map(str.strip, blocks)
  blocks = filter(lambda b: b != "", blocks)

  return list(blocks)
