# Module `cli`

docgen/cli.py

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

Generate Markdown docs for all .py files under SRC,
summarize every .py and .ipynb there, and write
a single Markdown file to OUT.

---

# Module `config`

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


The codebase is a command-line tool for generating Markdown documentation from Python files and summarizing their contents using OpenAI. It consists of commands for generating docs, summarizing individual files, and creating a combined Markdown file with docs and summaries for multiple files.

## Summary of `config.py`


This code chunk loads environment variables from a .env file and assigns default values to variables related to OpenAI API key, model, temperature, maximum tokens, and maximum code chunks.

## Summary of `generator.py`


The code defines a MarkdownGenerator class that generates Markdown documentation for items like modules, classes, and functions based on their type, name, comments, and docstrings.

## Summary of `parser.py`


The code snippets define a Python module for parsing code files to extract documentation items like module, class, and function definitions along with their docstrings and leading comments. The `parse_file` function reads a file, extracts comments, and uses abstract syntax trees to identify and collect relevant information about module, class, and function definitions before returning a sorted list of `DocItem` instances.

## Summary of `summarize.py`


The provided code snippets form a system that reads Python code from files, splits the code into manageable chunks based on functions or classes, creates a combined prompt for an AI model, queries the OpenAI API to summarize the code, and returns the cleaned summary text. The system utilizes various functions such as reading code from files, splitting code into chunks, building prompts, and interacting with the OpenAI ChatCompletion endpoint to generate summaries of codebases.

## Summary of `__init__.py`


I'm sorry, but you haven't provided any code chunks for me to summarize. Please provide the code you'd like me to summarize.