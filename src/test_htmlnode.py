import unittest
from htmlnode import HTMLNode

def test_props_to_html_empty(self):
    node = HTMLNode(props= "")
    self.assertEqual(node.props_to_html(), "")

def test_props_to_html_none(self):
    node = HTMLNode(props= None)
    self.assertEqual(node.props_to_html(), "")

def test_props_to_html(self):
    node = HTMLNode(props= {
    "href": "https://www.google.com",
    "target": "_blank",
})
    self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

def test_repr(self):
    node = HTMLNode("h1", "This is a heading", None)
    self.assertEqual(
        "HTMLNode(h1, This is a heading, None)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()