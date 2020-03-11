# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    # name defaults to the name of this directory, i.e., `helloworld`.
    # sources defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
    dependencies = [
        "3rdparty/python:translate",
        ":greetings",
        "src/python/util"
    ]
)


python_tests(
    name = 'tests',
    # sources defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
    dependencies = [
        ":helloworld"
    ]
)


python_binary(
    name = "main",
    entry_point = "helloworld.main",
    dependencies = [
        "3rdparty/python:ansicolors",
        ":helloworld",
    ]
)


resources(
    name = 'greetings',
    sources = ['greetings.txt'],
)
