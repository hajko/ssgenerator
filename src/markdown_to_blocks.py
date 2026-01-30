def markdown_to_blocks(markdown):
    nn_split = markdown.split("\n\n")
    blocks = [block.strip() for block in nn_split if block.strip() != ""]
    return blocks
