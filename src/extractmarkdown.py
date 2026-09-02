import re

def extract_markdown_images(text: str) -> list[tuple]:

    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text: str) -> list[tuple]:

    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_title(markdown: str) -> str:

    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            split_markdown = line.split("# ", 1)
            clean_title = split_markdown[1].strip()
            return clean_title
    else:
        raise Exception("Invalid header formatting")