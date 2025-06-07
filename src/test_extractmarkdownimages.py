from unittest import TestCase
from extractmarkdownimages import extract_markdown_images

class TestExtractMarkdownImages(TestCase):
  def test_with_two(self):
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

    actual = extract_markdown_images(text)
    expected = [
      ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
      ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
    ]

    self.assertListEqual(expected, actual)

  def test_with_one_link_and_one_image(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and ![rick roll](https://i.imgur.com/aKaOqIh.gif)"

    actual = extract_markdown_images(text)
    expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]

    self.assertListEqual(expected, actual)