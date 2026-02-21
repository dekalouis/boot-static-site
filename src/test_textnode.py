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

if __name__ == "__main__":
    unittest.main()