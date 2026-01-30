import re


def extract_title(markdown):
    title = re.findall(r"(?<=#).+", markdown)
    if len(title) == 0:
        raise Exception("no title")
    return title[0].strip()
