import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
                )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
                "This is text with a [link](https://www.google.com)"
                )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_markdown_no_link(self):
        matches = extract_markdown_links("This is regular text.")
        self.assertListEqual([], matches)