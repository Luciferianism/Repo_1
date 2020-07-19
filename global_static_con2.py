from global_static_con1 import *
from os import *
class base(enacal):
    def __init__(self) -> None:
        pass


def main():
    print(f"{i}")
    print(f"This will be a static variable which will get printed now, no need to create a class constructor. {base.x}")
    obj = base()
    print(f"{obj.foo()}")

if __name__ == "__main__":
    print(f"Starting Execution........")
    main()
    print(f"Execution has finished...........")