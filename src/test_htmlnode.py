import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"class": "my-class", "id": "my-id"})
        expected = ' class="my-class" id="my-id"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode(tag="div", value="Hello", children=[], props={"class": "my-class"})
        expected = "HTMLNode(tag=div, value=Hello, children=[], props={'class': 'my-class'})"
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()  

if __name__ == "__main__":
    unittest.main()