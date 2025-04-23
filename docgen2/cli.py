# docgen/cli.py

import click
from pathlib import Path

from .parser import parse_file
from .generator import MarkdownGenerator
from .summarize import summarize_code_file

@click.group()
def cli():
    """docgen: generate docs & summarize code"""
    pass

# @cli.command()
# @click.argument("src", type=click.Path(exists=True))
# @click.argument("out", type=click.Path())
# def generate(src, out):
#     """Generate individual Markdown docs for each Python file"""
#     src_path = Path(src)
#     out_path = Path(out)
#     out_path.mkdir(parents=True, exist_ok=True)

#     files = list(src_path.rglob("*.py")) if src_path.is_dir() else [src_path]

#     gen = MarkdownGenerator()

#     for f in files:
#         try:
#             items = parse_file(f)
#             md = gen.render(items)
#             md_file = out_path / (f.stem + ".md")
#             md_file.write_text(md, encoding="utf-8", errors="ignore")
#             click.echo(f"✅ {f.name} → {md_file.name}")
#         except Exception as e:
#             click.echo(f"❌ Failed to generate docs for {f.name}: {e}")


@cli.command()
@click.argument("file_path", type=click.Path(exists=True))
def summarize(file_path):
    """Summarize a .py or .ipynb file using OpenAI"""
    summary = summarize_code_file(file_path)
    click.echo(summary)

@cli.command(name="full")
@click.argument("src", type=click.Path(exists=True))
@click.argument("out", type=click.Path())
def full(src, out):
    """
    Generate Markdown docs for all .py files under SRC,
    summarize every .py and .ipynb there, and write
    a single Markdown file to OUT.
    """
    src_path = Path(src)
    # Gather all .py and .ipynb files
    if src_path.is_dir():
        py_files    = list(src_path.rglob("*.py"))
        ipynb_files = list(src_path.rglob("*.ipynb"))
        files = py_files + ipynb_files
    else:
        files = [src_path]

    # 1) Generate docs for .py files
    items = []
    for f in files:
        if f.suffix == ".py":
            items.extend(parse_file(f))
    md_docs = MarkdownGenerator().render(items)

    # 2) Summarize each file
    summary_sections = []
    for f in files:
        summary_sections.append(f"## Summary of `{f.name}`\n")
        summary_sections.append(summarize_code_file(f))

    # 3) Combine and write out
    combined_md = (
        md_docs
        + "\n\n---\n\n"
        + "\n\n".join(summary_sections)
    )
    Path(out).write_text(combined_md, encoding="utf-8", errors="ignore")
    click.echo(f"Docs and summaries written to {out}")

if __name__ == "__main__":
    cli()

# Alias for console‑script entry point
main = cli
