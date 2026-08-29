class HTMLNode:
    def __init__(self, 
                 tag: str | None=None, 
                 value: str | None=None, 
                 children: list[HTMLNode] | None=None, 
                 props: dict[str, str] | str | None=None
                 ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:

        html_statement = ""

        if self.props is not None and self.props != "":
            for key in self.props:
                html_statement += f' {key}="{self.props[key]}"'
            return html_statement
        else:
            return ""

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, children: None=None, props: dict[str, str] | str | None = None) -> None:
        super().__init__(tag, value, children, props)

    def to_html(self):

        return_prop = ""

        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value

        
        if self.props is None:
            
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.props is not None:
            for key in self.props:
                return_prop += f' {key}="{self.props[key]}"'
            return f"<{self.tag}{return_prop}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"