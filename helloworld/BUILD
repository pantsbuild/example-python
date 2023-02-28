# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
python_sources(
    name="lib",
)

# This target allows us to bundle our app into a PEX binary file via
#  `pants package`. We can also run it with `pants run`. See
#  https://www.pantsbuild.org/docs/python-package-goal and
#  https://www.pantsbuild.org/docs/python-run-goal.
pex_binary(
    name="pex_binary",
    entry_point="main.py",
)
