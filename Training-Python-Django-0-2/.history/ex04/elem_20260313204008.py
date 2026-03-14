
class Elem:
    def __init__(self, tag, attr, content, tag_type):
        self.tag = tag
        self.attr = attr if attr is not None else {}
        self.tag_type = tag_type
        self.content = []

