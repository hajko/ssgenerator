import os

from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, encoding="utf-8") as f:
        from_file = f.read()

    with open(template_path, encoding="utf-8") as f:
        template_file = f.read()

    html_string = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)

    with_title = template_file.replace("{{ Title }}", title, 1)
    with_content = with_title.replace("{{ Content }}", html_string, 1)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(with_content)
