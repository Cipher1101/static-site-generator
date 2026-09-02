from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_files_recursive
from generatepage import generate_pages_recursive
import sys


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
if len(sys.argv) >= 2:
    basepath = sys.argv[0]
else:
    basepath = "/"


def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

main()