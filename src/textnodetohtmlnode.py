from textnode import TextType
from htmlnode import HTMLNode

def text_node_to_html_node(text_node):
  match text_node.text_type:
    case TextType.NORMAL:
      return HTMLNode(value=text_node.text)
    case TextType.BOLD:
      return HTMLNode("b", text_node.text)
    case TextType.ITALIC:
      return HTMLNode("i", text_node.text)
    case TextType.CODE:
      return HTMLNode("code", text_node.text)
    case TextType.LINK:
      props = { "href": text_node.url }
      return HTMLNode("a", text_node.text, props=props)
    case TextType.IMAGE:
      props = {
        "src": text_node.url,
        "alt": text_node.text
      }
      return HTMLNode("img", "", props=props)
    case _:
      raise ValueError("Invalid text type")
