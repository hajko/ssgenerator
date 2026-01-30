import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        markdown = "### Heading Level 3"
        block_type = block_to_block_type(markdown)
        self.assertEqual(
            BlockType.HEADING,
            block_type,
        )

    def test_code(self):
        markdown = """
```
this is a multi-line
code block
```
"""
        block_type = block_to_block_type(markdown.strip())
        self.assertEqual(
            BlockType.CODE,
            block_type,
        )

    def test_quote(self):
        markdown = """
> this is a multi-line
> quote block
"""
        block_type = block_to_block_type(markdown.strip())
        self.assertEqual(
            BlockType.QUOTE,
            block_type,
        )

    def test_unordered_list(self):
        markdown = """
- this is an
- unordered list
- of things
"""
        block_type = block_to_block_type(markdown.strip())
        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_type,
        )

    def test_ordered_list(self):
        markdown = """
1. this is an
2. ordered list
3. of things
"""
        block_type = block_to_block_type(markdown.strip())
        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_type,
        )

    def test_paragraph(self):
        markdown = """
1. this is an
2. ordered list
4. of things, or is it?
"""
        block_type = block_to_block_type(markdown.strip())
        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type,
        )


if __name__ == "__main__":
    unittest.main()
