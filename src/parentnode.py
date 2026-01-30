from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("missing children")

        resulting_tag = ""
        for child in self.children:
            resulting_tag += child.to_html()
        resulting_tag = f"<{self.tag}>" + f"{resulting_tag}" + f"</{self.tag}>"
        return resulting_tag

    def __eq__(self, other):
        return (self.tag == other.tag and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.children}, {self.props})"
