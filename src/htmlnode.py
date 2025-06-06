from functools import reduce

class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError()

  def props_to_html(self):
    if self.props is None:
      return ""

    def process(result, pair):
      key, value = pair
      return result + f" {key}=\"{value}\""

    return reduce(process, self.props.items(), "")

  def __repr__(self):
    return f"{self.__class__.__name__}:\n" + \
           f"Tag: {self.tag and f"<{self.tag}>"}\n" + \
           f"Value: {self.value and f"{self.value}"}\n" + \
           f"Children: {self.children and len(self.children)}\n" + \
           f"Props: {self.props and len(self.props)}\n"
