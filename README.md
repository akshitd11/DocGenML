
# 📚 CodeDocGen

**CodeDocGen** is a Python package that automates the process of generating documentation from code by extracting docstrings and comments. It produces clean, human-readable documentation in **Markdown**, and can optionally evaluate its quality using NLP metrics like BLEU, ROUGE, and BERTScore.



## 🚀 Features

- ✅ Extracts documentation from `.py` files
- 🤖 Summarizes code using OpenAI
- 📘 Outputs Markdown files (extendable to HTML, LaTeX, PDF)
- 🔁 Keeps docs synced with codebase (great for CI)
- 📊 Evaluate doc quality using BLEU, ROUGE-L, BERTScore
- 🔌 Easy CLI interface with pluggable entry point

---

## 🔧 Installation

```bash
pip install -e .
```

> Make sure you are in the root directory of the project when running the above command.

---

## 📦 Usage

Once installed, use the `docgen` CLI directly from your terminal:

### 🛠️ 1. Generate Documentation

Generate Markdown docs from a `.py` file or an entire directory of `.py` files.

```bash
docgen generate <src_path> <output_md_file>
```

- `<src_path>`: A single `.py` file or a folder of `.py` files
- `<output_md_file>`: Destination `.md` file

**Example:**
```bash
docgen generate ./src/ ./docs/api.md
```

---

### 🧠 2. Summarize Code

Summarize a `.py` or `.ipynb` file using OpenAI (requires API key setup).

```bash
docgen summarize <file_path>
```

**Example:**
```bash
docgen summarize notebook.ipynb
```

---

### 🧩 3. Full Docs + Summaries

Generate both documentation and OpenAI summaries for all `.py` and `.ipynb` files in a folder.

```bash
docgen full <src_path> <output_md_file>
```

**Example:**
```bash
docgen full ./src ./docs/combined.md
```

---

### 📊 4. Evaluate Markdown Quality

Evaluate how well a generated `.md` file matches a reference `.md` using:

- BLEU
- ROUGE-L
- BERTScore

```bash
docgen evaluate <reference_file.md> <generated_file.md>
```

**Example:**
```bash
docgen evaluate ./docs/ref_output.md ./docs/generated_output.md
```

---

## 🧪 Development

To install all dependencies for development:

```bash
pip install -r requirements.txt
```

Dependencies include:

- `click`
- `pandas`
- `nltk`
- `rouge`
- `bert-score`
- `openai` (if using summarization)

---

## 📂 Project Structure

```
docgen/
│
├── cli.py             # Main CLI interface
├── parser.py          # Parses Python code for docstrings/comments
├── generator.py       # Converts parsed data to Markdown
├── summarize.py       # Summarizes code with OpenAI
├── __init__.py
```

---

## 🔐 OpenAI Setup (Optional)

To use the summarization feature, export your OpenAI API key:

```bash
export OPENAI_API_KEY=your_key_here  # macOS/Linux
set OPENAI_API_KEY=your_key_here     # Windows
```

---

## 📄 License

MIT License

---
