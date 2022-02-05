#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width
    
    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        if len(args) > 1:
            myArg = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, myArg[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return self.__dict__