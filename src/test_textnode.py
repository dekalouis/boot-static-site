import unittest

from textnode import TextNode, TextTypes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextTypes.BOLD)
        node2 = TextNode("This is a text node", TextTypes.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is an italic text node", TextTypes.ITALIC)
        node2 = TextNode("This is a different text node", TextTypes.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextTypes.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, **bold**, None)")

    def test_no_link_url(self):
        node = TextNode("This is a text node", TextTypes.LINK)
        self.assertEqual(node.url, None)

    # text to html node tests
    def test_text(self):
        node = TextNode("This is a text node", TextTypes.PLAIN)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    
    def test_bold(self):
        node = TextNode("bold", TextTypes.BOLD)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold")

    def test_link(self):
        node = TextNode("Click", TextTypes.LINK, "https://example.com")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("alt", TextTypes.IMAGE, "https://img.com/a.png")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://img.com/a.png", "alt": "alt"})


if __name__ == "__main__":
    unittest.main()