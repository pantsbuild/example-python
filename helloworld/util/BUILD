# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# See https://www.pantsbuild.org/docs/python-setup-py-goal.
python_distribution(
  name="dist",
  # Because this has no source code, Pants cannot infer dependencies.
  dependencies=[":util"],
  setup_py_commands=["bdist_wheel", "sdist"],
  provides=setup_py(
      name='helloworld.util',
      version='0.0.1',
      description='Greeting library utilities.',
  ),
)

# `name` defaults to the name of this directory, i.e., `util`.
# `sources` defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
python_library(
  # Pants cannot infer dependencies on Protobuf, so we explicitly add it.
  dependencies=[
      "helloworld/util/proto",
  ],
)

python_tests(
    name='tests',
    # `sources` defaults to ['*_test.py', 'test_*.py', 'conftest.py'].
    # Pants cannot infer dependencies on `resources` targets, so we explicitly add it.
    dependencies=[
        ":config_loader_test_data",
    ],
)

resources(
    name='config_loader_test_data',
    sources=['config_loader_test_data.json'],
)
