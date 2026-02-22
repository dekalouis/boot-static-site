from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextTypes(Enum):
    PLAIN = "plain"
    BOLD = "**bold**"
    ITALIC = "_italic_"
    CODE = "`code`"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextTypes(text_type)
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextTypes.PLAIN:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextTypes.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextTypes.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextTypes.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextTypes.LINK:
        if not text_node.url:
            raise ValueError("Link text nodes must have a url")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextTypes.IMAGE:
        if not text_node.url:
            raise ValueError("Image text nodes must have a url")
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")
    