from extract_markdown_links import extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or old_node.text == "":
            new_nodes.append(old_node)
        else:
            link_tuples = extract_markdown_links(old_node.text)
            if len(link_tuples) == 0:
                new_nodes.append(old_node)
                continue
            text_to_process = old_node.text
            for link_tuple in link_tuples:
                alt = link_tuple[0]
                link = link_tuple[1]
                sections = text_to_process.split(f"[{alt}]({link})", 1)
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.LINK, link))
                if len(sections) > 1:
                    text_to_process = sections[1]
            if sections[1] != "":
                new_nodes.append(TextNode(sections[1], TextType.TEXT))
    return new_nodes
