# docgen/cli.py
import click
from pathlib import Path
from .parser import parse_file
from .formatter import get_formatter
from .summarize import summarize_code_file

@click.group()
def cli():
    """docgen: generate docs & summarize code"""
    pass

@cli.command()
@click.argument("src", type=click.Path(exists=True))
@click.argument("out", type=click.Path())
@click.option("--format", "-f", default="markdown", help="Output format: markdown, html, pdf, latex")
def generate(src, out, format):
    """Generate docs from comments & docstrings"""
    src_path = Path(src)
    files = list(src_path.rglob("*.py")) if src_path.is_dir() else [src_path]
    
    items = []
    for f in files:
        items.extend(parse_file(f))
    
    formatter = get_formatter(format)
    output = formatter.render(items)
    
    # Handle binary vs text output
    if format.lower() == 'pdf':
        Path(out).write_bytes(output)
    else:
        Path(out).write_text(output, encoding="utf-8", errors="ignore")
    
    click.echo(f"Docs written to {out} in {format} format")

@cli.command()
@click.argument("file_path", type=click.Path(exists=True))
def summarize(file_path):
    """Summarize a .py or .ipynb file using OpenAI"""
    summary = summarize_code_file(file_path)
    click.echo(summary)

@cli.command(name="full")
@click.argument("src", type=click.Path(exists=True))
@click.argument("out", type=click.Path())
@click.option("--format", "-f", default="markdown", help="Output format: markdown, html, pdf, latex")
def full(src, out, format):
    """
    Generate docs for all .py files under SRC, summarize every .py and .ipynb there,
    and write a single file to OUT in the specified format.
    """
    src_path = Path(src)
    # Gather all .py and .ipynb files
    if src_path.is_dir():
        py_files = list(src_path.rglob("*.py"))
        ipynb_files = list(src_path.rglob("*.ipynb"))
        files = py_files + ipynb_files
    else:
        files = [src_path]
    
    # 1) Generate docs for .py files
    items = []
    for f in files:
        if f.suffix == ".py":
            items.extend(parse_file(f))
    
    formatter = get_formatter(format)
    docs_output = formatter.render(items)
    
    # 2) Summarize each file
    summaries = []
    for f in files:
        summaries.append({
            "name": f"Summary of {f.name}",
            "docstring": summarize_code_file(f),
            "params": [],
            "returns": ""
        })
    
    # 3) Combine docs and summaries
    combined_items = items + summaries
    
    # 4) Render output
    combined_output = formatter.render(combined_items)
    
    # 5) Write to file
    if format.lower() == 'pdf':
        Path(out).write_bytes(combined_output)
    else:
        Path(out).write_text(combined_output, encoding="utf-8", errors="ignore")
    
    click.echo(f"Docs and summaries written to {out} in {format} format")

if __name__ == "__main__":
    cli()

# Alias for console-script entry point
main = cli