from textnode import TextNode, TextType
from splitnodes import (
  split_nodes_by_image,
  split_nodes_by_link,
  split_nodes_by_delimiter
)

def text_to_text_node(text):
  node = TextNode(text, TextType.NORMAL)
  
  return split_nodes_by_image(
    split_nodes_by_link(
      split_nodes_by_delimiter(
        split_nodes_by_delimiter(
          split_nodes_by_delimiter(
            [node],
            "**",
            TextType.BOLD
          ),
          "_",
          TextType.ITALIC
        ),
        "`",
        TextType.CODE
      )
    )
  )
