#!/usr/bin/python3
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()

u = User()
print(u.id)
