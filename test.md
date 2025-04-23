
# Documentation


## cli








## cli


docgen: generate docs & summarize code







## generate


Generate docs from comments & docstrings







## summarize


Summarize a .py or .ipynb file using OpenAI







## full


Generate docs for all .py files under SRC, summarize every .py and .ipynb there,
and write a single file to OUT in the specified format.







## config








## formatter








## BaseFormatter


Base class for all formatters







## render


Convert parsed items into the target format







## get_template


Load a Jinja2 template from the templates directory







## MarkdownFormatter


Format parsed items as Markdown







## render








## HtmlFormatter


Format parsed items as HTML







## render








## LaTeXFormatter


Format parsed items as LaTeX







## render








## PDFFormatter


Format parsed items as PDF (via ReportLab)







## render








## get_formatter


Factory function to get the appropriate formatter







## generator








## MarkdownGenerator








## render








## parser








## DocItem








## extract_comments


Map ending line number → collected comment block above it.







## parse_file








## summarize








## read_code_from_file


Read a Python (.py) or Jupyter notebook (.ipynb) file and return its code as a single string.
- .py: returns the entire file.
- .ipynb: concatenates all code-cell sources, separated by blank lines.







## split_code_by_function_or_class


Split the full code into top‑level chunks, each beginning with a `def ` or `class `.
Returns up to `max_chunks` segments to avoid overly long prompts.







## build_combined_prompt


Build a single user prompt for the LLM by enumerating each chunk.
Prepends a header comment "# Chunk i" to each segment for clarity.







## summarize_code_file


Orchestrates the full summarization:
  1. Reads code from the given file.
  2. Splits into manageable chunks.
  3. Builds a combined prompt.
  4. Calls the OpenAI API to get a summary.
  5. Returns the cleaned summary text.







## __init__








## Summary of cli.py


The codebase provides a command-line interface (CLI) tool named "docgen" that can generate documentation from code comments and docstrings, as well as summarize Python (.py) and Jupyter notebook (.ipynb) files using OpenAI. The tool allows users to specify the output format (markdown, html, pdf, latex) and can process individual files or directories containing multiple files. The generated documentation and summaries can be written to a specified output file in the chosen format.







## Summary of config.py


This code chunk imports necessary libraries, loads environment variables from a .env file, and sets default values for variables related to OpenAI API key, model, temperature, max tokens, and maximum code chunks.







## Summary of formatter.py


The codebase contains a document generation system with different formatters for Markdown, HTML, LaTeX, and PDF formats. Each formatter inherits from a base class and implements a `render` method to convert parsed items into the respective format. There is also a factory function to get the appropriate formatter based on the desired output format.







## Summary of generator.py


The code defines a MarkdownGenerator class with a render method that generates Markdown documentation for a list of DocItem objects based on their type, name, comments, and docstring.







## Summary of parser.py


The provided codebase is a Python module that contains functions and data structures for parsing and extracting documentation information from Python source code files. The code includes functionalities to parse files, extract comments, and create data structures to store documentation details such as name, type, line number, docstring, and comments for modules, classes, and functions within the source code.







## Summary of summarize.py


The code provided is a script that reads Python or Jupyter notebook files, splits the code into manageable chunks based on functions or classes, builds a combined prompt for an AI model, utilizes the OpenAI API to summarize the code, and returns the cleaned summary text. The goal is to automate the process of summarizing codebases by interacting with the OpenAI ChatCompletion endpoint.







## Summary of __init__.py


I'm sorry, but you haven't provided any code chunks for me to summarize. If you provide me with code, I'd be happy to help summarize it for you.






