# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
#
# * `name` defaults to the name of this directory, i.e., `helloworld`.
# * `sources` defaults to ['*.py', '!*_test.py', '!test_*.py', '!conftest.py'].
# * Pants cannot infer dependencies on resources targets, so we explicitly add it.
python_library(
    dependencies=[":config_file"],
)

# This target teaches Pants about our JSON file, which allows for other targets to depend on it.
resources(
    name="config_file",
    sources=["config.json"],
)

# This target allows us to bundle our app into a PEX binary file via
#  `./pants package`. We can also run it with `./pants run`. See
#  https://www.pantsbuild.org/docs/python-package-goal and
#  https://www.pantsbuild.org/docs/python-run-goal.
pex_binary(
    name="pex_binary",
    entry_point="main.py",
)

# This target allows us to create an AWS Lambda binary via `./pants package`.
#  See https://www.pantsbuild.org/docs/awslambda-python.
#
# Note: This has sdist dependencies, so it must be built on Linux.
python_awslambda(
    name="awslambda",
    handler="awslambda.py:handler",
    runtime="python3.7",
)
