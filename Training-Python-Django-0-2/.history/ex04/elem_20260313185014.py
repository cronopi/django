class Elem:
    """
    A class to represent HTML elements and generate their HTML code.
    """

    class TagException(Exception):
        """Exception raised for errors related to HTML tags."""
        pass

    def __init__(self, name, attributes=None, type="double"):
        """
        Initialize an HTML element.

        Args:
            name (str): The name of the HTML tag (e.g., 'div', 'p', 'img')
            attributes (dict): Optional dictionary of HTML attributes
            type (str): Either "simple" for self-closing tags or "double" for paired tags

        Raises:
            TagException: If attributes is not a dict or None
        """
        if attributes is not None and not isinstance(attributes, dict):
            raise Elem.TagException("attributes must be a dictionary")

        self.name = name
        self.attributes = attributes if attributes else {}
        self.type = type
        self.content = []

    def __str__(self):
        """
        Return the HTML representation of the element.

        Returns:
            str: The HTML code for the element
        """
        # Build the attributes string
        attr_str = ""
        if self.attributes:
            attr_str = " " + " ".join([f'{key}="{value}"' for key, value in self.attributes.items()])

        # Build the content string
        content_str = "".join([str(item) for item in self.content])

        # Generate HTML based on type
        if self.type == "simple":
            return f"<{self.name}{attr_str} />"
        else:  # type == "double"
            return f"<{self.name}{attr_str}>{content_str}</{self.name}>"

    def add_content(self, content):
        """
        Add content to the element.

        Args:
            content: Can be a string or another Elem object
        """
        self.content.append(content)
