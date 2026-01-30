import os
import shutil

from generate_page import generate_page


def main():
    copydir("static", "public")

    dir_path_content = "./content"
    dir_path_public = "./public"
    template_path = "./template.html"

    for root, dirs, files in os.walk(dir_path_content):
        if "index.md" in files:
            input_md = os.path.join(root, "index.md")
            rel_path = os.path.relpath(root, dir_path_content)
            output_dir = os.path.join(dir_path_public, rel_path)
            output_html = os.path.join(output_dir, "index.html")
            generate_page(input_md, template_path, output_html)


def copydir(src, dst):
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    src_items = os.listdir(src)
    for item in src_items:
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst)
            continue
        if os.path.isdir(item_path):
            dst_path = os.path.join(dst, item)
            copydir(item_path, dst_path)


main()
