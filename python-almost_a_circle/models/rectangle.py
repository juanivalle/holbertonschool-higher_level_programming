#!/usr/bin/python3
"""comments"""


from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """comments"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """comments"""

        area = self.__width * self.__height
        return(area)

    def display(self):
        """comments"""

        if self.__width is 0 or self.__height is 0:
            return
        else:
            for z in range(self.__y):
                print()
            for i in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

    def __str__(self):
        id = self.id
        a = self.__x
        b = self.__y
        c = self.__width
        e = self.__height
        return(f"[Rectangle] ({id}) {a:d}/{b:d} - {c:d}/{e:d}")

    def update(self, *args, **kwargs):
        """comments"""
        if args:
            ats = ['id', 'width', 'height', 'x', 'y']
            for c in range(len(args)):
                setattr(self, ats[c], args[c])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """comments"""

        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
