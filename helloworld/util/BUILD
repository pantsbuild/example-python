# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
    # name defaults to the name of this directory, i.e., `util`.
    # sources defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
    dependencies = [
        "//:setuptools",
        "//:translate",
        ":langs"
    ],
    provides = setup_py(
        name='helloworld.util',
        version='0.0.1',
        description='Greeting library utilities',
    ),
)


python_tests(
    name = 'tests',
    # sources defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
    dependencies = [
        ":resources_test",
        ":util",
    ]
)


resources(
    name = 'langs',
    sources = ['langs.txt'],
)


resources(
    name = 'resources_test',
    sources = ['resources_test.txt'],
)
