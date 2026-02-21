# print("hello world")
from textnode import TextNode, TextTypes

def main():
    node = TextNode("This is some anchor text", TextTypes.LINK.value, url="https://www.example.com")
    print(node)


main()