import unittest
from docgen.generator import MarkdownGenerator
from docgen.parser import DocItem


class TestMarkdownGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = MarkdownGenerator()

    def test_render_single_module(self):
        items = [
            DocItem(
                name="test_module",
                type="module",
                lineno=1,
                docstring="This is the module docstring.",
                comments="This module handles testing."
            )
        ]
        md = self.generator.render(items)
        self.assertIn("# Module `test_module`", md)
        self.assertIn("This module handles testing.", md)
        self.assertIn("This is the module docstring.", md)
        self.assertIn("---", md)

    def test_render_class_and_function(self):
        items = [
            DocItem(
                name="MyClass",
                type="class",
                lineno=10,
                docstring="This class does something.",
                comments=""
            ),
            DocItem(
                name="my_function",
                type="function",
                lineno=20,
                docstring="This function helps.",
                comments="Helper function comment"
            )
        ]
        md = self.generator.render(items)
        self.assertIn("## Class `MyClass`", md)
        self.assertIn("This class does something.", md)
        self.assertIn("### Function `my_function`", md)
        self.assertIn("This function helps.", md)
        self.assertIn("Helper function comment", md)
        self.assertEqual(md.count("---"), 2)

    def test_render_empty_fields(self):
        items = [
            DocItem(
                name="empty_item",
                type="function",
                lineno=1,
                docstring="",
                comments=""
            )
        ]
        md = self.generator.render(items)
        self.assertIn("### Function `empty_item`", md)
        self.assertTrue("---" in md)


if __name__ == "__main__":
    unittest.main()
