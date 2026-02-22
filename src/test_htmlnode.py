import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>",)

    def test_to_html_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_invalid_child(self):
        parent_node = ParentNode("div", ["not a node"])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "my-class"})
        expected = "ParentNode(tag=div, children=[LeafNode(tag=span, value=child, props=None)], props={'class': 'my-class'})"   

if __name__ == "__main__":
    unittest.main()