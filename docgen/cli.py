import click
from pathlib import Path
import os
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge
from bert_score import score

from .parser import parse_file
from .generator import MarkdownGenerator
from .summarize import summarize_code_file

rouge = Rouge()

@click.group()
def cli():
    """docgen: generate docs & summarize code"""
    pass

@cli.command()
@click.argument("src", type=click.Path(exists=True))
@click.argument("out", type=click.Path())
def generate(src, out):
    """Generate Markdown docs from comments & docstrings"""
    src_path = Path(src)
    files = list(src_path.rglob("*.py")) if src_path.is_dir() else [src_path]
    items = []
    for f in files:
        items.extend(parse_file(f))
    md = MarkdownGenerator().render(items)
    Path(out).write_text(md, encoding="utf-8", errors="ignore")
    click.echo(f"Docs written to {out}")

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
    """Generate and summarize code into a single markdown"""
    src_path = Path(src)
    files = list(src_path.rglob("*.py")) + list(src_path.rglob("*.ipynb")) if src_path.is_dir() else [src_path]

    items = []
    for f in files:
        if f.suffix == ".py":
            items.extend(parse_file(f))
    md_docs = MarkdownGenerator().render(items)

    summary_sections = []
    for f in files:
        summary_sections.append(f"## Summary of `{f.name}`\n")
        summary_sections.append(summarize_code_file(f))

    combined_md = md_docs + "\n\n---\n\n" + "\n\n".join(summary_sections)
    Path(out).write_text(combined_md, encoding="utf-8", errors="ignore")
    click.echo(f"Docs and summaries written to {out}")

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def clean_markdown(md):
    lines = [line for line in md.splitlines() if not line.startswith('#') and not line.startswith('---')]
    return " ".join(lines).strip()

def evaluate_files(reference_file, generated_file):
    """Compare two markdown files and return BLEU, ROUGE-L, and BERTScore F1."""
    if not os.path.exists(reference_file):
        raise FileNotFoundError(f"Reference file not found: {reference_file}")
    if not os.path.exists(generated_file):
        raise FileNotFoundError(f"Generated file not found: {generated_file}")

    reference = load_file(reference_file)
    generated = clean_markdown(load_file(generated_file))

    if not generated.strip():
        raise ValueError("⚠️ Empty or invalid generated markdown after cleaning.")

    bleu = sentence_bleu([reference.split()], generated.split())
    rouge_score = rouge.get_scores(generated, reference)[0]["rouge-l"]["f"]
    _, _, bert_f1 = score([generated], [reference], lang="en", verbose=False)

    return pd.DataFrame([{
        "BLEU": bleu,
        "ROUGE-L": rouge_score,
        "BERTScore F1": bert_f1.mean().item()
    }])

@cli.command()
@click.argument("reference_file", type=click.Path(exists=True))
@click.argument("generated_file", type=click.Path(exists=True))
def evaluate(reference_file, generated_file):
    """Evaluate a generated markdown file against a reference markdown file"""
    try:
        df = evaluate_files(reference_file, generated_file)
        click.echo(df.to_markdown(index=False))
    except Exception as e:
        click.echo(f"❌ Error: {e}")

if __name__ == "__main__":
    cli()

main = cli  # for console entry point
