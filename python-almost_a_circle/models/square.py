#!/usr/bin/python3
"""comments"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """comments"""

    def __init__(self, size, x=0, y=0, id=None):
        """comments"""

        super().__init__(id, x, y, width, height)
    
    def __str__(self):
        """comments"""

        id = self.id
        a = self.x
        b = self.y
        c = self.width
        return(f"[Square] ({id}) {a:d}/{b:d} - {c:d}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
