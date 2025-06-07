from unittest import TestCase
from extractmarkdownlinks import extract_markdown_links

class TestExtractMarkdownLinks(TestCase):
  def test_with_two(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

    actual = extract_markdown_links(text)
    expected = [
      ("to boot dev", "https://www.boot.dev"),
      ("to youtube", "https://www.youtube.com/@bootdotdev")
    ]

    self.assertListEqual(expected, actual)

  def test_with_one_link_and_one_image(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and ![rick roll](https://i.imgur.com/aKaOqIh.gif)"

    actual = extract_markdown_links(text)
    expected = [("to boot dev", "https://www.boot.dev")]

    self.assertListEqual(expected, actual)
