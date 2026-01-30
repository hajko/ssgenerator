import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    props1 = {
        "href": "https://www.google.com",
        "target": "_blank",
    }

    props2 = {
        "href": "https://www.yahoo.com",
        "target": "_blank",
    }

    def test_eq(self):
        node1 = HTMLNode(tag="p", value="This is an HTML node", props=self.props1)
        node2 = HTMLNode(tag="p", value="This is an HTML node", props=self.props1)
        self.assertEqual(node1, node2)

    def test_neq1(self):
        node1 = HTMLNode(tag="p", value="This is an HTML node", props=self.props1)
        node2 = HTMLNode(tag="p", value="This is an HTML nood", props=self.props1)
        self.assertNotEqual(node1, node2)

    def test_neq2(self):
        node1 = HTMLNode(tag="p", value="This is an HTML node", props=self.props1)
        node2 = HTMLNode(tag="p", value="This is an HTML node", props=self.props2)
        self.assertNotEqual(node1, node2)

    def test_neq3(self):
        node1 = HTMLNode(tag="p", value="This is an HTML node", props=self.props2)
        node2 = HTMLNode(tag="a", value="This is an HTML node", props=self.props2)
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
