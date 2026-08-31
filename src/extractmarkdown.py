import re
from textnode import TextNode, TextType, text_node_to_html_node

def extract_markdown_images(text: str) -> list[tuple]:

    matches = re.findall(r"\[(.+)\]\((.+)\)", text)
    
    return matches

def extract_markdown_links(text: str) -> list[tuple]:

    matches = re.findall(r"\[(.+)\]\((.+)\)", text)

    return matches