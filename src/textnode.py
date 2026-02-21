from enum import Enum

class TextTypes(Enum):
    PLAIN_TEXT = "plain text"
    BOLD_TEXT = "**bold text**"
    ITALIC_TEXT = "_italic text_"
    CODE_TEXT = "`code text`"
    LINKS = "[anchor text](url)"
    IMAGES = "![alt text](url)"

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