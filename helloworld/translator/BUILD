# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
python_library(
    name="lib",
)

# This target sets the metadata for all the Python test files in this directory.
python_tests(
    name="tests",
)

# This target allows us to build a `.whl` bdist and a `.tar.gz` sdist by auto-generating
#  `setup.py`. See https://www.pantsbuild.org/docs/python-distributions.
#
# Because this target has no source code, Pants cannot infer dependencies. We depend on `:lib`,
#  which means we'll include all the non-test Python files in this directory, and any of
#  their dependencies.
python_distribution(
    name="dist",
    dependencies=[":lib"],
    setup_py_commands=["bdist_wheel", "sdist"],
    provides=setup_py(
        name='helloworld.util',
        version='0.0.1',
        description='Greeting library utilities.',
    ),
)
