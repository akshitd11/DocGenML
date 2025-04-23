import unittest
from pathlib import Path
from textwrap import dedent
from docgen import parser
from docgen.parser import DocItem


class TestParser(unittest.TestCase):

    def test_extract_comments_basic(self):
        src = dedent("""\
            # Top level comment
            # Another comment

            def foo():
                pass

            # Comment before bar
            def bar():
                pass
        """)
        comments = parser.extract_comments(src)

        # ✅ Updated to reflect actual line-to-comment mapping
        self.assertIn(1, comments)
        self.assertEqual(comments[1], "Top level comment")
        self.assertIn(2, comments)
        self.assertEqual(comments[2], "Another comment")
        self.assertIn(7, comments)
        self.assertEqual(comments[7], "Comment before bar")

    def test_parse_file_module_and_defs(self):
        src = dedent('''\
            """Module docstring"""
            # Module-level comment

            class MyClass:
                """Class docstring"""
                def method(self):
                    """Method docstring"""
                    pass

            # Before func
            def my_func():
                """Function docstring"""
                pass
        ''')
        temp_path = Path("temp_test_file.py")
        temp_path.write_text(src, encoding="utf-8")

        try:
            items = parser.parse_file(temp_path)
            self.assertEqual(len(items), 4)

            module_item = next(i for i in items if i.type == "module")
            self.assertEqual(module_item.docstring, "Module docstring")

            class_item = next(i for i in items if i.name == "MyClass")
            self.assertEqual(class_item.docstring, "Class docstring")

            func_item = next(i for i in items if i.name == "my_func")
            self.assertEqual(func_item.docstring, "Function docstring")
            self.assertIn("Before func", func_item.comments)

        finally:
            temp_path.unlink()


if __name__ == "__main__":
    unittest.main()
