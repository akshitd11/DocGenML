import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
from textwrap import dedent
import os

from docgen import summarize


class TestSummarizeModule(unittest.TestCase):

    def setUp(self):
        # Create dummy .py and .ipynb files
        self.test_py = Path("test_code.py")
        self.test_py.write_text(dedent("""\
            # Sample Python File
            def foo():
                return 'foo'

            class Bar:
                def bar_method(self):
                    return 'bar'
        """))

        self.test_ipynb = Path("test_notebook.ipynb")
        self.test_ipynb.write_text("""{
            "cells": [
                {
                    "cell_type": "code",
                    "source": ["def add(a, b):", "    return a + b"],
                    "metadata": {},
                    "outputs": []
                }
            ],
            "metadata": {},
            "nbformat": 4,
            "nbformat_minor": 2
        }""")

    def tearDown(self):
        self.test_py.unlink()
        self.test_ipynb.unlink()

    def test_read_code_from_py_file(self):
        content = summarize.read_code_from_file(str(self.test_py))
        self.assertIn("def foo", content)
        self.assertIn("class Bar", content)

    def test_read_code_from_ipynb_file(self):
        content = summarize.read_code_from_file(str(self.test_ipynb))
        self.assertIn("def add", content)

    def test_split_code_by_function_or_class(self):
        code = dedent("""\
            def a(): pass

            class B:
                def b(): pass

            def c(): pass
        """)
        chunks = summarize.split_code_by_function_or_class(code)
        self.assertEqual(len(chunks), 3)
        self.assertTrue(chunks[0].strip().startswith("def a"))

    def test_build_combined_prompt_format(self):
        chunks = ["def x(): pass", "class Y: pass"]
        prompt = summarize.build_combined_prompt(chunks)
        self.assertIn("# Chunk 1", prompt)
        self.assertIn("def x():", prompt)
        self.assertIn("# Chunk 2", prompt)
        self.assertIn("class Y:", prompt)

    @patch("docgen.summarize.client.chat.completions.create")
    def test_summarize_code_file_with_mock(self, mock_openai_call):
        # Mock OpenAI response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Mocked summary output."
        mock_openai_call.return_value = mock_response

        result = summarize.summarize_code_file(str(self.test_py))
        self.assertEqual(result, "Mocked summary output.")

    def test_summarize_code_file_invalid_path(self):
        result = summarize.summarize_code_file("non_existent_file.py")
        self.assertIn("Error: File not found.", result)


if __name__ == "__main__":
    unittest.main()
