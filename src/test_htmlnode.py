import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
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
            "HTMLNode(h1, This is a heading, None, None)", repr(node)
            )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "This is a heading!")
        self.assertEqual(node.to_html(), "<h1>This is a heading!</h1>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click here!", None, {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here!</a>')

class TestParentNode(unittest.TestCase):

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    if __name__ == "__main__":
        unittest.main()