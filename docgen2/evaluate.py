import os
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge
from bert_score import score

rouge = Rouge()

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def clean_markdown(md):
    # Keep only content likely to be the function/class/module docstring
    lines = [line for line in md.splitlines() if not line.startswith('#') and not line.startswith('---')]
    return " ".join(lines).strip()

def evaluate(reference_dir, markdown_dir, limit=None):
    results = []
    filenames = [f for f in os.listdir(reference_dir) if f.endswith("_reference.txt")]
    
    if limit:
        filenames = filenames[:limit]

    for fname in filenames:
        base = fname.replace("_reference.txt", "")
        ref_path = os.path.join(reference_dir, fname)
        md_path = os.path.join(markdown_dir, base + ".md")

        if not os.path.exists(md_path):
            print(f"⚠️ Missing .md file for: {base}")
            continue

        reference = load_file(ref_path)
        generated = clean_markdown(load_file(md_path))

        if not generated.strip():
            print(f"⚠️ Empty generated markdown for: {base}")
            continue

        bleu = sentence_bleu([reference.split()], generated.split())
        rouge_score = rouge.get_scores(generated, reference)[0]["rouge-l"]["f"]
        _, _, bert_f1 = score([generated], [reference], lang="en", verbose=False)

        results.append({
            "file": base,
            "BLEU": bleu,
            "ROUGE-L": rouge_score,
            "BERTScore F1": bert_f1.mean().item()
        })

    return pd.DataFrame(results)