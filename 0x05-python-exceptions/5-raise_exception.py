#!/usr/bin/python3
def raise_exception():
    raise TypeError("An exception is raised")

if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
