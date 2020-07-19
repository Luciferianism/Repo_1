from os import *
global i
i = "this will be global"

class enacal(object):
    x = "This is a class level/ variable"
    def __init__(self) -> None:
        pass

    def foo(self):
        d = "This is a non static level var, Have to create a class constructor to access this var"
        return d

    def foo_2(self):
        pass

