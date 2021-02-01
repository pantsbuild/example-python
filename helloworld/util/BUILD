# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
#
# * `name` defaults to the name of this directory, i.e., `util`.
# * `sources` defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
# * `dependencies` are inferred.
python_library()

# This target sets the metadata for all the Python test files in this directory.
#
# * `sources` defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
# * Pants cannot infer dependencies on `resources` targets, so we explicitly add the dep.
python_tests(
    name='tests',
    dependencies=[":test_data"],
)

# This target teaches Pants about our JSON file, which allows for other targets to depend on it.
resources(
    name='test_data',
    sources=['*_test_data.json'],
)

# This target allows us to build a `.whl` bdist and a `.tar.gz` sdist by auto-generating
#  `setup.py`. See https://www.pantsbuild.org/docs/python-distributions.
#
# Because this target has no source code, Pants cannot infer dependencies. We depend on `:util`,
#  which means we'll include all the non-test Python files in this directory, and any of
#  their dependencies.
python_distribution(
    name="dist",
    dependencies=[":util"],
    setup_py_commands=["bdist_wheel", "sdist"],
    provides=setup_py(
        name='helloworld.util',
        version='0.0.1',
        description='Greeting library utilities.',
    ),
)
