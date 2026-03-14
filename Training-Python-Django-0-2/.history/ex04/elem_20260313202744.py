
class Elem:                    # Creamos una clase llamada Elem
    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        # Parámetros del builder:
        self.tag = tag              # Nombre de la etiqueta (ej: 'div', 'body', 'h1')
        self.attr = attr or {}      # Atributos HTML (ej: {'src': 'imagen.jpg'})
        self.tag_type = tag_type    # Tipo: 'simple' o 'double'
        self.content = []           # Lista para guardar el contenido
