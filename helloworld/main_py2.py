# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import green

from helloworld.greet_py2.greeting_py2 import greet_py2


def say_hello_py2():
    print green(greet_py2("Python 2"))


if __name__ == "__main__":
    say_hello_py2()
