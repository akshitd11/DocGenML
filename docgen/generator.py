# docgen/generator.py
from typing import List
from docgen.parser import DocItem

class MarkdownGenerator:
    def render(self, items: List[DocItem]) -> str:
        md = []
        for item in items:
            header = {
                "module": "# Module",
                "class": "## Class",
                "function": "### Function"
            }[item.type]
            md.append(f"{header} `{item.name}`\n")
            if item.comments:
                md.append(item.comments + "\n")
            if item.docstring:
                md.append(item.docstring + "\n")
            md.append("---\n")
        return "\n".join(md)
