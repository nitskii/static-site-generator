from unittest import TestCase, main
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
      parent_node.to_html(),
      "<div><span><b>grandchild</b></span></div>",
    )

  def test_to_html_without_tag(self):
    node = ParentNode(None, None)
    try:
      node.to_html()
    except ValueError as error: 
      self.assertEqual(str(error), "Parent node must have a tag")

  def test_to_html_without_children(self):
    node = ParentNode("div", None)

    try:
      node.to_html()
    except ValueError as error: 
      self.assertEqual(str(error), "Parent node must have at least 1 child")

    node = ParentNode("div", [])

    try:
      node.to_html()
    except ValueError as error: 
      self.assertEqual(str(error), "Parent node must have at least 1 child")
