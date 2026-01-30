from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            text_portions = old_node.text.split(delimiter)

            if len(text_portions) == 1:  # there are no delimiters
                new_nodes.append(old_node)
                continue

            if len(text_portions) % 2 == 0:  # if there are delimiters, there must be an odd number of portions
                raise Exception("invalid markdown format")

            for index, portion in enumerate(text_portions):

                if index % 2 == 0:
                    portion_node = TextNode(portion, TextType.TEXT)
                else:
                    portion_node = TextNode(portion, text_type)

                new_nodes.append(portion_node)

    return new_nodes
