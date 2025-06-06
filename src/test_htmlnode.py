from unittest import TestCase, main

from htmlnode import HTMLNode

class TestHTMLNode(TestCase):
  def test_props_to_html(self):
    props = { "a": "b", "c": "d" }
    expected = " a=\"b\" c=\"d\""
    node = HTMLNode(props=props)
    actual = node.props_to_html()
    self.assertEqual(expected, actual)
