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

---

# Module `__init__`

---


---

## Summary of `cli.py`


This codebase is a command-line utility for generating Markdown documentation from Python files, summarizing code using OpenAI, and evaluating the generated Markdown against reference text. It includes commands for generating documentation, summarizing code, combining documentation and summaries, cleaning Markdown text, and evaluating Markdown files. The utility uses libraries like click, pandas, nltk, rouge, and bert_score for various tasks.

## Summary of `config.py`


This code chunk imports necessary modules, loads environment variables from a .env file, and sets default values for variables related to OpenAI API key, model, temperature, max tokens, and maximum code chunks allowed.

## Summary of `evaluate.py`


The code snippets consist of functions and imports used for evaluating the quality of generated markdown files against reference texts. The code involves loading files, cleaning markdown content, and calculating evaluation metrics such as BLEU, ROUGE-L, and BERTScore F1 for each pair of reference and generated markdown files.

## Summary of `generator.py`


The code consists of a markdown generator class that takes a list of DocItem objects and renders them into markdown format, including headers based on the item type, comments, and docstrings.

## Summary of `parser.py`


The codebase consists of a Python module for parsing source code files to extract documentation items such as module, class, and function definitions along with their associated docstrings and comments. It includes functions for extracting comments, parsing source files, and generating structured documentation items from the code.

## Summary of `summarize.py`


The code provided includes functions to read code from Python or Jupyter notebook files, split the code into chunks based on functions or classes, build a combined prompt for a language model, and summarize code files using the OpenAI API. The `summarize_code_file` function orchestrates the entire process by handling file reading, chunking, prompt creation, API querying, and returning the cleaned summary text. This codebase aims to automate the summarization of code files by leveraging OpenAI's language model capabilities.

## Summary of `__init__.py`


I'm sorry, but you have not provided any code chunks for me to summarize. Could you please provide the code chunks so that I can assist you in summarizing them?