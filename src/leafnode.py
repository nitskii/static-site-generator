from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag=tag, value=value, props=props)

  def to_html(self):
    if self.value is None:
      raise ValueError()

    if self.tag is None:
      return self.value

    attributes = "" if self.props is None else self.props_to_html()

    return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"
