from textnode import TextType, TextNode

def split_text_node(old_nodes, delimiter, text_type):
  new_nodes = []

  for old_node in old_nodes:
    if old_node.text_type is not TextType.NORMAL:
      new_nodes.append(old_node)
      continue

    parts = old_node.text.split(delimiter)

    if len(parts) % 2 == 0:
      raise ValueError("Invalid markdown")

    for i in range(len(parts)):
      if parts[i] == "": continue

      if i % 2 == 0:
        new_nodes.append(TextNode(parts[i], TextType.NORMAL))
      else:
        new_nodes.append(TextNode(parts[i], text_type))

  return new_nodes
