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
    # Keep only lines likely to be actual content, not headers or dividers
    lines = [line for line in md.splitlines() if not line.startswith('#') and not line.startswith('---')]
    return " ".join(lines).strip()

def evaluate(reference_file, generated_file):
    """
    Compare two markdown files (reference vs generated) and return BLEU, ROUGE-L, and BERTScore F1.
    """
    if not os.path.exists(reference_file):
        raise FileNotFoundError(f"Reference file not found: {reference_file}")
    if not os.path.exists(generated_file):
        raise FileNotFoundError(f"Generated file not found: {generated_file}")

    reference = load_file(reference_file)
    generated = clean_markdown(load_file(generated_file))

    if not generated.strip():
        raise ValueError("⚠️ Empty or invalid generated markdown after cleaning.")

    # Evaluation Metrics
    bleu = sentence_bleu([reference.split()], generated.split())
    rouge_score = rouge.get_scores(generated, reference)[0]["rouge-l"]["f"]
    _, _, bert_f1 = score([generated], [reference], lang="en", verbose=False)

    return pd.DataFrame([{
        "BLEU": bleu,
        "ROUGE-L": rouge_score,
        "BERTScore F1": bert_f1.mean().item()
    }])
