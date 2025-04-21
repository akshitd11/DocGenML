# docgen/parser.py
import ast
import tokenize
from pathlib import Path
from dataclasses import dataclass
import io

@dataclass
class DocItem:
    name: str
    type: str           # "module", "class", or "function"
    lineno: int
    docstring: str
    comments: str       # any leading #‑comments


def extract_comments(src: str) -> dict[int, str]:
    """
    Map ending line number → collected comment block above it.
    """
    comments: dict[int, str] = {}
    buffer: list[str] = []
    last_line: int | None = None

    # Create a callable readline for generate_tokens
    reader = io.StringIO(src).readline

    # tokenize.generate_tokens wants a function, not an iterator
    for tok_type, tok_str, start, _, _ in tokenize.generate_tokens(reader):
        if tok_type == tokenize.COMMENT:
            # strip leading “# ” and trailing whitespace
            buffer.append(tok_str.lstrip("# ").rstrip())
            last_line = start[0]
        else:
            # whenever we hit a non-comment, flush any buffered comments 
            if buffer and last_line is not None:
                comments[last_line] = "\n".join(buffer)
                buffer = []
                last_line = None

    # In case file ends with comments:
    if buffer and last_line is not None:
        comments[last_line] = "\n".join(buffer)

    return comments


def parse_file(path: Path) -> list[DocItem]:
    src = path.read_text(encoding="utf-8", errors="ignore")
    comments_map = extract_comments(src)
    tree = ast.parse(src)
    out: list[DocItem] = []

    # Module‑level
    module_doc = ast.get_docstring(tree) or ""
    out.append(DocItem(name=path.stem,
                       type="module",
                       lineno=1,
                       docstring=module_doc,
                       comments=comments_map.get(1, "")))

    for node in ast.walk(tree):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            name = node.name
            kind = "class" if isinstance(node, ast.ClassDef) else "function"
            doc = ast.get_docstring(node) or ""
            # capture any #‑comments that end right before this def
            c = comments_map.get(node.lineno - 1, "")
            out.append(DocItem(name=name,
                               type=kind,
                               lineno=node.lineno,
                               docstring=doc,
                               comments=c))
    return sorted(out, key=lambda d: d.lineno)
