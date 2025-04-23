import os
import re
import io
import nbformat
import openai

from docgen.config import (
    MAX_CODE_CHUNKS,
    OPENAI_API_KEY,
    OPENAI_MODEL,
    OPENAI_TEMPERATURE,
    OPENAI_MAX_TOKENS,
)

# ──────────────────────────────────────────────────────────────────────────────
# Initialize OpenAI client with the API key from config
# ──────────────────────────────────────────────────────────────────────────────
client = openai.OpenAI(api_key=OPENAI_API_KEY)


def read_code_from_file(file_path: str) -> str:
    """
    Read a Python (.py) or Jupyter notebook (.ipynb) file and return its code as a single string.
    - .py: returns the entire file.
    - .ipynb: concatenates all code-cell sources, separated by blank lines.
    """
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".py":
        # Read .py file, ignore any decoding errors
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    elif ext == ".ipynb":
        # Read notebook and extract code cells
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            nb = nbformat.read(f, as_version=4)
            # Join each code cell’s source with two newlines
            return "\n\n".join(
                cell.source
                for cell in nb.cells
                if cell.cell_type == "code"
            )

    else:
        # Unsupported file type
        raise ValueError("Unsupported format. Only .py and .ipynb allowed.")


def split_code_by_function_or_class(
    code: str,
    max_chunks: int = MAX_CODE_CHUNKS
) -> list[str]:
    """
    Split the full code into top‑level chunks, each beginning with a `def ` or `class `.
    Returns up to `max_chunks` segments to avoid overly long prompts.
    """
    # Use regex lookahead to split right before each `def ` or `class `
    chunks = re.split(r'\n(?=def |class )', code)
    return chunks[:max_chunks]


def build_combined_prompt(chunks: list[str]) -> str:
    """
    Build a single user prompt for the LLM by enumerating each chunk.
    Prepends a header comment "# Chunk i" to each segment for clarity.
    """
    # Label each chunk and join with double newlines for readability
    chunked = "\n\n".join(f"# Chunk {i+1}\n{c}" for i, c in enumerate(chunks))

    # Instruction + all code chunks
    return (
        "You are a helpful AI assistant. Summarize the following code chunks.\n\n"
        f"{chunked}\n\n"
        "Provide a single, clear summary of the overall purpose."
    )


def summarize_code_file(file_path: str) -> str:
    """
    Orchestrates the full summarization:
      1. Reads code from the given file.
      2. Splits into manageable chunks.
      3. Builds a combined prompt.
      4. Calls the OpenAI API to get a summary.
      5. Returns the cleaned summary text.
    """
    # 1) Ensure file exists
    if not os.path.isfile(file_path):
        return "Error: File not found."

    # 2) Load and chunk the code
    code = read_code_from_file(file_path)
    chunks = split_code_by_function_or_class(code)

    # 3) Create the prompt for the LLM
    prompt = build_combined_prompt(chunks)

    # 4) Query the OpenAI ChatCompletion endpoint
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You summarize codebases."},
            {"role": "user",   "content": prompt}
        ],
        temperature=OPENAI_TEMPERATURE,
        max_tokens=OPENAI_MAX_TOKENS
    )

    # 5) Return the summary (strip any leading/trailing whitespace)
    return resp.choices[0].message.content.strip()
