import re

def extract_markdown_links(text):

    link_tuples = []

    anchors = re.findall(r"(?<=\[)([^\]]+)", text)
    urls = re.findall(r"(?<=\()([^\)]+)", text)

    for i in range(len(anchors)):
        link_tuples.append((anchors[i], urls[i]))

    return link_tuples
