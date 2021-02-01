# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
#
# * `name` defaults to the name of this directory, i.e., `greet`.
# * `sources` defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
# * `dependencies` are inferred.
python_library()

# This target sets the metadata for all the Python test files in this directory.
#
# * `sources` defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
# * `dependencies` are inferred.
python_tests(name='tests')
