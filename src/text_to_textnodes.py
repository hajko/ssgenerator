from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    after_bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    after_italic = split_nodes_delimiter(after_bold, "_", TextType.ITALIC)
    after_code = split_nodes_delimiter(after_italic, "`", TextType.CODE)
    after_image = split_nodes_image(after_code)
    after_link = split_nodes_link(after_image)
    return after_link
