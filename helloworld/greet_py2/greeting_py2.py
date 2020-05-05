# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).


def greet_py2(name):
    exec "x = 'hello, {}'.format(name)"
    return x  # noqa
