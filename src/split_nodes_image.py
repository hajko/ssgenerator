from extract_markdown_images import extract_markdown_images
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or old_node.text == "":
            new_nodes.append(old_node)
        else:
            img_tuples = extract_markdown_images(old_node.text)
            if len(img_tuples) == 0:
                new_nodes.append(old_node)
                continue
            text_to_process = old_node.text
            for img_tuple in img_tuples:
                img_alt = img_tuple[0]
                img_link = img_tuple[1]
                sections = text_to_process.split(f"![{img_alt}]({img_link})", 1)
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_link))
                if len(sections) > 1:
                    text_to_process = sections[1]
            if sections[1] != "":
                new_nodes.append(TextNode(sections[1], TextType.TEXT))
    return new_nodes
