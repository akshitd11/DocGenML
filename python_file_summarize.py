import os
import re
import nbformat
import openai

# 🔐 OpenAI client (v1.0+)
client = openai.OpenAI(api_key="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")

def read_code_from_file(file_path: str) -> str:
    ext = os.path.splitext(file_path)[-1]
    if ext == ".py":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".ipynb":
        with open(file_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            return "\n\n".join(cell.source for cell in nb.cells if cell.cell_type == "code")
    else:
        raise ValueError("❌ Unsupported file format. Only .py and .ipynb allowed.")

def split_code_by_function_or_class(code: str, max_chunks: int = 10) -> list:
    """
    Splits code into top-level chunks by function/class definition.
    """
    chunks = re.split(r'\n(?=def |class )', code)
    return chunks[:max_chunks]

def build_combined_prompt(chunks: list) -> str:
    """
    Combines all code chunks into one well-structured prompt.
    """
    chunked_code = "\n\n".join([f"# Chunk {i+1}\n{chunk}" for i, chunk in enumerate(chunks)])
    prompt = (
        "You are a helpful AI assistant. Analyze the following Python code chunks and summarize the overall purpose of the code.\n\n"
        f"{chunked_code}\n\n"
        "Provide a single, clear summary of what the entire code does overall."
    )
    return prompt

def summarize_code_file(file_path: str) -> str:
    """
    Reads a .py or .ipynb file, splits it into code chunks, and summarizes all at once via a single LLM call.
    """
    if not os.path.isfile(file_path):
        return "❌ Error: File not found."

    try:
        code = read_code_from_file(file_path)
        chunks = split_code_by_function_or_class(code, max_chunks=10)

        prompt = build_combined_prompt(chunks)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You summarize Python codebases."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=400
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error during summarization: {e}"

summary = summarize_code_file("Lab01_sparshmarwah.ipynb")
print(summary)