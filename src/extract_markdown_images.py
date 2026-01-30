import re

def extract_markdown_images(text):

    img_tuples = []

    alts = re.findall(r"(?<=!\[)([^\]]+)", text)
    links = re.findall(r"(?<=\()([^\)]+)", text)

    for i in range(len(alts)):
        img_tuples.append((alts[i], links[i]))

    return img_tuples
