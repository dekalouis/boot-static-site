import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
    )

from textnode import TextNode, TextTypes

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextTypes.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.PLAIN),
                TextNode("bolded", TextTypes.BOLD),
                TextNode(" word", TextTypes.PLAIN),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextTypes.PLAIN
        )
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.PLAIN),
                TextNode("bolded", TextTypes.BOLD),
                TextNode(" word and ", TextTypes.PLAIN),
                TextNode("another", TextTypes.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextTypes.PLAIN
        )
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.PLAIN),
                TextNode("bolded word", TextTypes.BOLD),
                TextNode(" and ", TextTypes.PLAIN),
                TextNode("another", TextTypes.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextTypes.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextTypes.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.PLAIN),
                TextNode("italic", TextTypes.ITALIC),
                TextNode(" word", TextTypes.PLAIN),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextTypes.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextTypes.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextTypes.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextTypes.BOLD),
                TextNode(" and ", TextTypes.PLAIN),
                TextNode("italic", TextTypes.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextTypes.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextTypes.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.PLAIN),
                TextNode("code block", TextTypes.CODE),
                TextNode(" word", TextTypes.PLAIN),
            ],
            new_nodes,
        )

    # testing regex
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )      
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
            matches
        )

    # testing split nodes images and links
    def test_split_images(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextTypes.PLAIN,
            )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.PLAIN),
                TextNode("image", TextTypes.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextTypes.PLAIN),
                TextNode(
                    "second image", TextTypes.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
    )
        
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextTypes.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextTypes.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextTypes.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextTypes.PLAIN),
                TextNode("image", TextTypes.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextTypes.PLAIN),
                TextNode(
                    "second image", TextTypes.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextTypes.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextTypes.PLAIN),
                TextNode("link", TextTypes.LINK, "https://boot.dev"),
                TextNode(" and ", TextTypes.PLAIN),
                TextNode("another link", TextTypes.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextTypes.PLAIN),
            ],
            new_nodes,
        )

    # test text to text node    

    def test_text_to_textnodes(self):
        text = "This is **bold** text with an _italic_ word, a `code block`, an ![image](https://i.imgur.com/zjjcJKZ.png), and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextTypes.PLAIN),
                TextNode("bold", TextTypes.BOLD),
                TextNode(" text with an ", TextTypes.PLAIN),
                TextNode("italic", TextTypes.ITALIC),
                TextNode(" word, a ", TextTypes.PLAIN),
                TextNode("code block", TextTypes.CODE),
                TextNode(", an ", TextTypes.PLAIN),
                TextNode("image", TextTypes.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(", and a ", TextTypes.PLAIN),
                TextNode("link", TextTypes.LINK, "https://boot.dev"),
            ],
            nodes,
        )

    def test_text_to_textnodes_two(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextTypes.PLAIN),
                TextNode("text", TextTypes.BOLD),
                TextNode(" with an ", TextTypes.PLAIN),
                TextNode("italic", TextTypes.ITALIC),
                TextNode(" word and a ", TextTypes.PLAIN),
                TextNode("code block", TextTypes.CODE),
                TextNode(" and an ", TextTypes.PLAIN),
                TextNode("image", TextTypes.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextTypes.PLAIN),
                TextNode("link", TextTypes.LINK, "https://boot.dev"),
            ],
            nodes,
        )

if __name__ == "__main__":
    unittest.main()