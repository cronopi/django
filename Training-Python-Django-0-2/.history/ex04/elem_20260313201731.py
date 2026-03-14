#!/usr/bin/env python3
# coding: utf-8

class Text(str):
    """
    Clase que representa texto en HTML.
    Hereda de str y automáticamente escapa caracteres especiales
    y convierte saltos de línea a <br /> para HTML.
    """
    
    def __new__(cls, content=''):
        """
        __new__() es necesario porque str es inmutable.
        Este método procesa el contenido ANTES de crear la instancia.
        """
        # Convertir a string por si es número u otro tipo
        content = str(content)
        
        # Paso 1: Escapar & primero (para no escapar los & de los otros escapes)
        content = content.replace('&', '&amp;')
        
        # Paso 2: Escapar caracteres especiales de HTML
        content = content.replace('<', '&lt;')
        content = content.replace('>', '&gt;')
        content = content.replace('"', '&quot;')
        
        # Paso 3: Reemplazar saltos de línea con <br /> para HTML
        content = content.replace('\n', '\n<br />\n')
        
        # Crear la instancia de str con el contenido procesado
        return str.__new__(cls, content)


class Elem:
    """
    Clase que representa un elemento HTML (como <div>, <body>, <h1>, etc.)
    Puede contener otros Elem o Text, y genera automáticamente el HTML.
    """
    
    class ValidationError(Exception):
        """Excepción personalizada para errores de validación de contenido"""
        pass
    
    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        """
        Constructor del elemento HTML.
        
        Args:
            tag (str): Nombre de la etiqueta HTML (default: 'div')
            attr (dict): Diccionario de atributos HTML (default: {})
            content: Contenido del elemento (Text, Elem, lista, o None)
            tag_type (str): 'simple' para self-closing tags o 'double' para tags con cierre
        """
        # Inicializar atributos
        self.tag = tag
        self.attr = attr if attr is not None else {}
        self.tag_type = tag_type
        self.content = []  # Lista para almacenar el contenido válido
        
        # Si se proporciona contenido inicial, agregarlo con validación
        if content is not None:
            self.add_content(content)
    
    def add_content(self, content):
        """
        Agrega contenido al elemento. Solo acepta Text o Elem.
        Si es una lista, valida que todos los items sean Text o Elem.
        
        Args:
            content: Text, Elem, o lista de Text/Elem
            
        Raises:
            ValidationError: Si el contenido no es válido
        """
        
        # Si es una lista, procesar cada elemento
        if isinstance(content, list):
            for item in content:
                # Validar que sea Text o Elem
                if not isinstance(item, (Text, Elem)):
                    raise Elem.ValidationError(
                        f"Content must be Text or Elem, got {type(item).__name__}"
                    )
                
                # No agregar Text vacío (optimización)
                if isinstance(item, Text) and str(item) == '':
                    continue
                
                self.content.append(item)
        
        # Si es un item único
        elif isinstance(content, (Text, Elem)):
            # No agregar Text vacío
            if isinstance(content, Text) and str(content) == '':
                return
            
            self.content.append(content)
        
        # Si no es válido, lanzar excepción
        else:
            raise Elem.ValidationError(
                f"Content must be Text or Elem, got {type(content).__name__}"
            )
    
    def __str__(self):
        """
        Genera el código HTML completo del elemento.
        
        Returns:
            str: El HTML renderizado (con indentación correcta para anidados)
        """
        
        # Paso 1: Construir string de atributos
        attr_str = ''
        for key, value in self.attr.items():
            attr_str += f' {key}="{value}"'
        
        # Paso 2: Tags simples (self-closing, como <img />)
        if self.tag_type == 'simple':
            return f'<{self.tag}{attr_str} />'
        
        # Paso 3: Tags dobles sin contenido (como <div></div>)
        if not self.content:
            return f'<{self.tag}{attr_str}></{self.tag}>'
        
        # Paso 4: Tags dobles con contenido
        # Indentar cada línea del contenido con 2 espacios
        content_lines = []
        for item in self.content:
            item_str = str(item)
            
            # Por cada línea del item, agregarla indentada
            for line in item_str.split('\n'):
                content_lines.append('  ' + line)
        
        # Juntar todo: apertura + contenido indentado + cierre
        content_str = '\n' + '\n'.join(content_lines) + '\n'
        return f'<{self.tag}{attr_str}>{content_str}</{self.tag}>'
