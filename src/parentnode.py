from functools import reduce
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("Parent node must have a tag")

    if self.children is None or len(self.children) == 0:
      raise ValueError("Parent node must have at least 1 child")

    def process(result, child):
      return result + child.to_html()

    children_html = reduce(process, self.children, "")

    return f"<{self.tag}>{children_html}</{self.tag}>"
    