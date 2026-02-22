class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
        # Self-closing tags (like img, br, hr) don't need a value
        if self.tag in ("img", "br", "hr"):
            return f"<{self.tag}{self.props_to_html()} />"
        # Regular tags must have a value
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        children_html = ""
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
        # if not isinstance(self.children, list):
        #     raise ValueError("Parent node children must be a list")
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError("Parent node children must be HTMLNode instances")
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
    

