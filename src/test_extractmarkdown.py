import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links, extract_title
from generatepage import generate_page

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

    def text_extract_title(self):
        matches = extract_title("# Hello")
        self.assertEqual("Hello", matches)

    def test_extract_title_h4(self):
        matches = "#### Hello"
        self.assertRaises(Exception, extract_title, matches)

    def test_extract_title_from_block(self):
        matches = extract_title("""# This is the title
        
        We only care about the title, but let's assume that we have more text.
        
        **We can even have some bold text.**
        
        Hopefully it will make:
        
        - No
        - Difference
        - At
        - All""")
        self.assertEqual("This is the title", matches)
