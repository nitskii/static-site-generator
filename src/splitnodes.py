from textnode import TextType, TextNode
from extractmarkdownimages import extract_markdown_images
from extractmarkdownlinks import extract_markdown_links

def split_nodes_by_delimiter(old_nodes, delimiter, text_type):
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

def split_nodes_by_image(old_nodes):
  new_nodes = []

  for old_node in old_nodes:
    if old_node.text_type is not TextType.NORMAL:
      new_nodes.append(old_node)
      continue

    extracted_images = extract_markdown_images(old_node.text)

    if len(extracted_images) == 0:
      new_nodes.append(old_node)
      continue

    original_text = old_node.text

    for alt, url in extracted_images:
      parts = original_text.split(f"![{alt}]({url})", 1)

      if len(parts) != 2:
        raise ValueError("Invalid markdown")

      if parts[0] != "": 
        new_nodes.append(TextNode(parts[0], TextType.NORMAL))

      new_nodes.append(TextNode(alt, TextType.IMAGE, url))

      original_text = parts[1]

    if original_text != "":
      new_nodes.append(TextNode(original_text, TextType.NORMAL))

  return new_nodes

def split_nodes_by_link(old_nodes):
  new_nodes = []

  for old_node in old_nodes:
    if old_node.text_type is not TextType.NORMAL:
      new_nodes.append(old_node)
      continue

    extracted_links = extract_markdown_links(old_node.text)

    if len(extracted_links) == 0:
      new_nodes.append(old_node)
      continue

    original_text = old_node.text

    for text, url in extracted_links:
      parts = original_text.split(f"[{text}]({url})", 1)

      if len(parts) != 2:
        raise ValueError("Invalid markdown")

      if parts[0] != "":
        new_nodes.append(TextNode(parts[0], TextType.NORMAL))

      new_nodes.append(TextNode(text, TextType.LINK, url))

      original_text = parts[1]

    if original_text != "":
      new_nodes.append(TextNode(original_text, TextType.NORMAL))

  return new_nodes
