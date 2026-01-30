import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    props1 = {
        "href": "https://www.google.com",
    }

    props2 = {
        "src": "url/of/image.jpg",
    }

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", props=self.props1)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is bold text")
        self.assertEqual(node.to_html(), "<b>This is bold text</b>")

if __name__ == "__main__":
    unittest.main()
