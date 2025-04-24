# Module `cli`

---

### Function `cli`

docgen: generate docs & summarize code

---

### Function `generate`

Generate Markdown docs from comments & docstrings

---

### Function `summarize`

Summarize a .py or .ipynb file using OpenAI

---

### Function `full`

Generate and summarize code into a single markdown

---

### Function `load_file`

---

### Function `clean_markdown`

---

### Function `evaluate_markdown`

---

### Function `evaluate`

Evaluate generated markdown files against reference text

---

# Module `config`

---

# Module `evaluate`

---

### Function `load_file`

---

### Function `clean_markdown`

---

### Function `evaluate`

---

# Module `generator`

docgen/generator.py

---

## Class `MarkdownGenerator`

---

### Function `render`

---

# Module `parser`

docgen/parser.py

---

## Class `DocItem`

---

### Function `extract_comments`

Map ending line number → collected comment block above it.

---

### Function `parse_file`

---

# Module `summarize`

---

### Function `read_code_from_file`

Read a Python (.py) or Jupyter notebook (.ipynb) file and return its code as a single string.
- .py: returns the entire file.
- .ipynb: concatenates all code-cell sources, separated by blank lines.

---

### Function `split_code_by_function_or_class`

Split the full code into top‑level chunks, each beginning with a `def ` or `class `.
Returns up to `max_chunks` segments to avoid overly long prompts.

---

### Function `build_combined_prompt`

Build a single user prompt for the LLM by enumerating each chunk.
Prepends a header comment "# Chunk i" to each segment for clarity.

---

### Function `summarize_code_file`

Orchestrates the full summarization:
  1. Reads code from the given file.
  2. Splits into manageable chunks.
  3. Builds a combined prompt.
  4. Calls the OpenAI API to get a summary.
  5. Returns the cleaned summary text.
