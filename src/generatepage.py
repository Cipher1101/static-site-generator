from markdownblocks import markdown_to_html_node
from extractmarkdown import extract_title
import os
from pathlib import Path

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown_content = file.read()
    with open(template_path, "r") as file:
        template_content = file.read()
    markdown_node = markdown_to_html_node(markdown_content)
    html_string = markdown_node.to_html()
    title = extract_title(markdown_content)
    temp_content = template_content.replace("{{ Title }}", title)
    final_content = temp_content.replace("{{ Content }}", html_string)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(final_content)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:

    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
    