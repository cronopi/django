
class Elem:
    def __init__(self, tag, attr, content, tag_type):
        self.tag = tag
        self.attr = attr or {}
        self.tag_type = tag_type
        self.content = []

