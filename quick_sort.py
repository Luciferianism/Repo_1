from random import *
from os import *
# Python modules can get access to code from another module by importing the file/function (in case of file it is reffered as inheritance)
# The import function is similar to #include <file_name> in C/C++. It is very good way to import module as {from module import *} This is the
# best way for invoking the import machinery. 

def creating_array(size=10,max=50):
    x = randint(0,max)
    print(f"{x}")