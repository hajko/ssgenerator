import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_block_type(markdown):
    if re.match(r"^#{1,6} .+", markdown):
        return BlockType.HEADING
    elif re.match(r"^```\n(.+\n)+```", markdown):
        return BlockType.CODE
    elif re.match(r"^(> .+\n)+", markdown):
        return BlockType.QUOTE
    elif re.match(r"^(- .+\n)+", markdown):
        return BlockType.UNORDERED_LIST
    elif re.match(r"^(\d. .+\n)+", markdown):
        lines = markdown.strip().split("\n")
        is_ordered_list = True
        for i, line in enumerate(lines):
            is_ordered_list = is_ordered_list and line.startswith(f"{i + 1}. ")
        if is_ordered_list:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
