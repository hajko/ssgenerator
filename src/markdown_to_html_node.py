import re

from block_to_block_type import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        match blocktype:
            case BlockType.PARAGRAPH:
                paragraph_text = " ".join(block.split("\n"))
                paragraph_node = ParentNode("p", text_to_children(paragraph_text))
                children_nodes.append(paragraph_node)
            case BlockType.HEADING:
                match = re.match(r"^#+", block)
                heading_level = match.end()
                heading_tag = f"h{heading_level}"
                content = block[heading_level:].lstrip()
                heading_node = ParentNode(heading_tag, text_to_children(content))
                children_nodes.append(heading_node)
            case BlockType.CODE:
                # remove the ``` lines
                lines = block.split("\n")
                inner_lines = lines[1:-1]
                code_text = (
                    "\n".join(inner_lines) + "\n"
                )  # note final newline to match test
                text_node = TextNode(code_text, TextType.CODE)
                code_child = text_node_to_html_node(text_node)
                pre_node = ParentNode("pre", [code_child])
                children_nodes.append(pre_node)
            case BlockType.QUOTE:
                lines = block.split("\n")
                cleaned_lines = [line.lstrip("> ").rstrip() for line in lines]
                quote_text = " ".join(cleaned_lines)
                quote_node = ParentNode("blockquote", text_to_children(quote_text))
                children_nodes.append(quote_node)
            case BlockType.UNORDERED_LIST:
                list_items = []
                li = process_list_items(block)
                for item in li:
                    list_items.append(ParentNode("li", text_to_children(item)))
                children_nodes.append(ParentNode("ul", list_items))
            case BlockType.ORDERED_LIST:
                list_items = []
                li = process_list_items(block)
                for item in li:
                    list_items.append(ParentNode("li", text_to_children(item)))
                children_nodes.append(ParentNode("ol", list_items))

    return ParentNode("div", children_nodes)


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children_nodes = []
    for textnode in textnodes:
        children_nodes.append(text_node_to_html_node(textnode))
    return children_nodes


def process_list_items(block):
    items = []
    for line in block.split("\n"):
        line = line.strip()
        if not line:
            continue

        # unordered list
        if line.startswith("- ") or line.startswith("* "):
            items.append(line[2:])
            continue

        # ordered list
        m = re.match(r"^\d+\.\s+(.*)$", line)
        if m:
            items.append(m.group(1))
            continue

        # fallback
        items.append(line)

    return items
