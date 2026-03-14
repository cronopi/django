
class Elem:
    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr or {}
        self.tag_type = tag_type
        self.content = []

