#!/usr/bin/python3
"""comments"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """comments"""

    def __init__(self, size, x=0, y=0, id=None):
        """comments"""

        super().__init__(size, size, x, y, id)

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

    def update(self, *args, **kwargs):
        """comments"""

        if args:
            ats = ['id', 'size', 'x', 'y']
            for c in range(len(args)):
                setattr(self, ats[c], args[c])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """comments"""

        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
