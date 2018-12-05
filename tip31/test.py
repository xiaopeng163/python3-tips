f = open('test1.txt', 'w')
f.write('hello, world')
f.close()

f = open('test2.txt', 'w')

try:
    f.write('hello world')
finally:
    f.close()

with open('test3.txt', 'w') as f:
    f.write('helloworld')

# with statement context manager
# https://docs.python.org/3/reference/datamodel.html#object.__enter__

class MyFile:

    def __init__(self, name):
        self.name = name
        self.file = None
    
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

with MyFile('test4.txt') as f:
    f.write('hello hello')


# contextlib
# https://docs.python.org/3/library/contextlib.html

from contextlib import contextmanager

@contextmanager
def open_file(name):
    # Code to acquire resource, e.g.:
    f = open(name, 'w')
    try:
        yield f
    finally:
        # Code to release resource, e.g.:
        f.close()


with open_file('test5.txt') as f:
    f.write('new new new\n')
    f.write('new new new')
